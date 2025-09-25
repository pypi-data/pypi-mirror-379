#!/usr/bin/env python3
"""
AWS Blogs Search Validation System
Prevents incorrect information by validating search results.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Tuple
import json
from datetime import datetime

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger("aws-blogs-search-validator")

class SearchValidator:
    """Validates search results to prevent incorrect information."""
    
    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        
        # Known test cases for validation
        self.test_cases = [
            {
                'query': 'Introducing AWS Gateway Load Balancer – Easy Deployment, Scalability, and High Availability for Partner Appliances',
                'expected_url': 'https://aws.amazon.com/blogs/aws/introducing-aws-gateway-load-balancer-easy-deployment-scalability-and-high-availability-for-partner-appliances/',
                'category': 'aws',
                'should_exist': True
            },
            {
                'query': 'Partners Group Strategic Cloud Transformation',
                'expected_category': 'alps',
                'should_exist': True
            },
            {
                'query': 'Non-existent blog post about fake AWS service',
                'should_exist': False
            }
        ]
    
    async def validate_search_system(self, search_function) -> Dict[str, Any]:
        """Validate the search system against known test cases."""
        results = {
            'total_tests': len(self.test_cases),
            'passed': 0,
            'failed': 0,
            'test_results': [],
            'overall_status': 'UNKNOWN'
        }
        
        for i, test_case in enumerate(self.test_cases):
            logger.info(f"Running test case {i+1}/{len(self.test_cases)}: {test_case['query'][:50]}...")
            
            test_result = await self._run_test_case(search_function, test_case)
            results['test_results'].append(test_result)
            
            if test_result['passed']:
                results['passed'] += 1
            else:
                results['failed'] += 1
        
        results['success_rate'] = results['passed'] / results['total_tests']
        results['overall_status'] = 'PASS' if results['success_rate'] >= 0.8 else 'FAIL'
        
        return results
    
    async def _run_test_case(self, search_function, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Run a single test case."""
        query = test_case['query']
        should_exist = test_case['should_exist']
        
        try:
            # Run the search
            search_results = await search_function(query, limit=10)
            
            test_result = {
                'query': query,
                'expected_exists': should_exist,
                'found_results': len(search_results),
                'passed': False,
                'details': {},
                'timestamp': datetime.now().isoformat()
            }
            
            if should_exist:
                # Test case expects results
                if search_results:
                    # Validate specific expectations
                    if 'expected_url' in test_case:
                        found_expected_url = any(
                            result.get('url') == test_case['expected_url'] 
                            for result in search_results
                        )
                        test_result['passed'] = found_expected_url
                        test_result['details']['expected_url_found'] = found_expected_url
                    elif 'expected_category' in test_case:
                        found_expected_category = any(
                            result.get('category') == test_case['expected_category']
                            for result in search_results
                        )
                        test_result['passed'] = found_expected_category
                        test_result['details']['expected_category_found'] = found_expected_category
                    else:
                        # Just check if any results were found
                        test_result['passed'] = True
                else:
                    test_result['passed'] = False
                    test_result['details']['error'] = 'No results found when results were expected'
            else:
                # Test case expects no results
                test_result['passed'] = len(search_results) == 0
                if search_results:
                    test_result['details']['error'] = f'Found {len(search_results)} results when none were expected'
            
            test_result['details']['results'] = [
                {
                    'title': result.get('title', ''),
                    'url': result.get('url', ''),
                    'category': result.get('category', ''),
                    'similarity_score': result.get('similarity_score', 0)
                }
                for result in search_results[:3]  # Top 3 results
            ]
            
        except Exception as e:
            test_result = {
                'query': query,
                'expected_exists': should_exist,
                'found_results': 0,
                'passed': False,
                'details': {'error': str(e)},
                'timestamp': datetime.now().isoformat()
            }
        
        return test_result
    
    async def validate_url_accessibility(self, urls: List[str]) -> Dict[str, Any]:
        """Validate that URLs are accessible."""
        results = {
            'total_urls': len(urls),
            'accessible': 0,
            'inaccessible': 0,
            'url_results': []
        }
        
        for url in urls:
            try:
                response = await self.client.head(url)
                accessible = response.status_code == 200
                
                results['url_results'].append({
                    'url': url,
                    'accessible': accessible,
                    'status_code': response.status_code
                })
                
                if accessible:
                    results['accessible'] += 1
                else:
                    results['inaccessible'] += 1
                    
            except Exception as e:
                results['url_results'].append({
                    'url': url,
                    'accessible': False,
                    'error': str(e)
                })
                results['inaccessible'] += 1
        
        return results
    
    def generate_validation_report(self, validation_results: Dict[str, Any]) -> str:
        """Generate a human-readable validation report."""
        report = []
        report.append("=" * 60)
        report.append("AWS BLOGS SEARCH VALIDATION REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Overall status
        status = validation_results['overall_status']
        status_emoji = "✅" if status == "PASS" else "❌"
        report.append(f"Overall Status: {status_emoji} {status}")
        report.append(f"Success Rate: {validation_results['success_rate']:.1%}")
        report.append(f"Tests Passed: {validation_results['passed']}/{validation_results['total_tests']}")
        report.append("")
        
        # Individual test results
        report.append("INDIVIDUAL TEST RESULTS:")
        report.append("-" * 40)
        
        for i, test in enumerate(validation_results['test_results'], 1):
            status_emoji = "✅" if test['passed'] else "❌"
            report.append(f"{i}. {status_emoji} {test['query'][:60]}...")
            
            if not test['passed']:
                report.append(f"   Error: {test['details'].get('error', 'Unknown error')}")
            
            if test['details'].get('results'):
                report.append(f"   Found {len(test['details']['results'])} results:")
                for result in test['details']['results']:
                    report.append(f"   - {result['title'][:50]}... (Score: {result['similarity_score']:.2f})")
            
            report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS:")
        report.append("-" * 40)
        
        if validation_results['success_rate'] < 0.8:
            report.append("❌ Search system needs improvement:")
            report.append("   - Implement comprehensive category coverage")
            report.append("   - Add multiple parsing strategies")
            report.append("   - Improve similarity matching algorithms")
            report.append("   - Add fallback search mechanisms")
        else:
            report.append("✅ Search system is performing well")
            report.append("   - Continue monitoring with regular validation")
            report.append("   - Consider adding more test cases")
        
        return "\n".join(report)

class SearchQualityMonitor:
    """Monitors search quality over time."""
    
    def __init__(self):
        self.metrics = {
            'total_searches': 0,
            'successful_searches': 0,
            'failed_searches': 0,
            'average_results_per_search': 0,
            'common_failed_queries': [],
            'performance_metrics': []
        }
    
    def record_search(self, query: str, results: List[Dict[str, Any]], execution_time: float):
        """Record search metrics."""
        self.metrics['total_searches'] += 1
        
        if results:
            self.metrics['successful_searches'] += 1
        else:
            self.metrics['failed_searches'] += 1
            self.metrics['common_failed_queries'].append(query)
        
        # Update averages
        total_results = sum(len(r) for r in [results])
        self.metrics['average_results_per_search'] = (
            (self.metrics['average_results_per_search'] * (self.metrics['total_searches'] - 1) + len(results)) 
            / self.metrics['total_searches']
        )
        
        self.metrics['performance_metrics'].append({
            'query': query,
            'results_count': len(results),
            'execution_time': execution_time,
            'timestamp': datetime.now().isoformat()
        })
        
        # Keep only recent metrics (last 100)
        if len(self.metrics['performance_metrics']) > 100:
            self.metrics['performance_metrics'] = self.metrics['performance_metrics'][-100:]
        
        # Keep only recent failed queries (last 20)
        if len(self.metrics['common_failed_queries']) > 20:
            self.metrics['common_failed_queries'] = self.metrics['common_failed_queries'][-20:]
    
    def get_quality_report(self) -> Dict[str, Any]:
        """Get quality metrics report."""
        if self.metrics['total_searches'] == 0:
            return {'status': 'No searches recorded'}
        
        success_rate = self.metrics['successful_searches'] / self.metrics['total_searches']
        
        return {
            'success_rate': success_rate,
            'total_searches': self.metrics['total_searches'],
            'average_results': self.metrics['average_results_per_search'],
            'recent_failed_queries': self.metrics['common_failed_queries'][-10:],
            'status': 'GOOD' if success_rate > 0.8 else 'NEEDS_IMPROVEMENT',
            'recommendations': self._generate_recommendations(success_rate)
        }
    
    def _generate_recommendations(self, success_rate: float) -> List[str]:
        """Generate recommendations based on metrics."""
        recommendations = []
        
        if success_rate < 0.5:
            recommendations.append("CRITICAL: Search system has very low success rate")
            recommendations.append("Implement comprehensive search overhaul")
        elif success_rate < 0.8:
            recommendations.append("Search system needs improvement")
            recommendations.append("Add more fallback mechanisms")
        else:
            recommendations.append("Search system performing well")
            recommendations.append("Continue monitoring")
        
        return recommendations