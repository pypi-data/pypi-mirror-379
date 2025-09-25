#!/usr/bin/env python3
"""
Improved AWS Blogs Search System
Addresses critical design flaws and provides robust search capabilities.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urljoin, urlparse
import re
from difflib import SequenceMatcher
import json
from datetime import datetime, timedelta

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger("aws-blogs-improved-search")

class ImprovedAWSBlogsSearch:
    """Robust AWS Blogs search with multiple fallback strategies."""
    
    def __init__(self, client: httpx.AsyncClient, base_url: str, known_categories: List[str]):
        self.client = client
        self.base_url = base_url
        self.blog_base_url = f"{base_url}/blogs/"
        self.known_categories = known_categories
        
        # Cache for performance
        self._category_cache = {}
        self._cache_expiry = {}
        self.cache_duration = timedelta(hours=1)
        
        # Multiple parsing strategies
        self.title_selectors = [
            # Primary selectors
            'h2.blog-post-title a',
            'h3.blog-post-title a', 
            '.blog-post-title a',
            # Fallback selectors
            'h2 a[href*="/blogs/"]',
            'h3 a[href*="/blogs/"]',
            'a[href*="/blogs/"][title]',
            # Generic selectors
            'a[href*="/blogs/"]'
        ]
        
        # URL patterns for different blog structures
        self.url_patterns = [
            "{base}/blogs/{category}/",
            "{base}/blog/{category}/",
            "{base}/security/blog/" if "{category}" == "security" else None
        ]
    
    async def comprehensive_search(self, query: str, category: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Multi-strategy search with comprehensive coverage and fallback mechanisms.
        """
        results = []
        query_normalized = self._normalize_query(query)
        
        # Strategy 1: Direct URL construction and verification
        potential_urls = self._generate_potential_urls(query)
        for url in potential_urls:
            if await self._verify_url_exists(url):
                blog_post = await self._extract_blog_post(url)
                if blog_post and self._matches_query(blog_post, query_normalized):
                    results.append(blog_post)
                    if len(results) >= limit:
                        return results
        
        # Strategy 2: Category-specific search (if category provided)
        if category:
            category_results = await self._search_in_category(query_normalized, category, limit - len(results))
            results.extend(category_results)
            if len(results) >= limit:
                return results[:limit]
        
        # Strategy 3: Comprehensive multi-category search
        if len(results) < limit:
            multi_category_results = await self._search_all_categories(query_normalized, limit - len(results))
            results.extend(multi_category_results)
        
        # Strategy 4: Fuzzy search fallback
        if len(results) < limit:
            fuzzy_results = await self._fuzzy_search_fallback(query_normalized, limit - len(results))
            results.extend(fuzzy_results)
        
        # Strategy 5: Sitemap search (last resort)
        if len(results) < limit:
            sitemap_results = await self._sitemap_search(query_normalized, limit - len(results))
            results.extend(sitemap_results)
        
        return self._deduplicate_and_rank(results, query_normalized)[:limit]
    
    def _normalize_query(self, query: str) -> Dict[str, Any]:
        """Normalize query for better matching."""
        return {
            'original': query,
            'lower': query.lower(),
            'slug': re.sub(r'[^\w\s-]', '', query.lower()).replace(' ', '-'),
            'words': query.lower().split(),
            'keywords': self._extract_keywords(query)
        }
    
    def _extract_keywords(self, query: str) -> List[str]:
        """Extract important keywords from query."""
        # Remove common words and extract technical terms
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were'}
        words = re.findall(r'\b\w+\b', query.lower())
        return [word for word in words if word not in stop_words and len(word) > 2]
    
    def _generate_potential_urls(self, query: str) -> List[str]:
        """Generate potential URLs based on query patterns."""
        urls = []
        
        # Pattern 1: Direct slug construction
        slug = re.sub(r'[^\w\s-]', '', query.lower()).replace(' ', '-')
        slug = re.sub(r'-+', '-', slug).strip('-')
        
        for category in ['aws', 'compute', 'architecture', 'developer', 'machine-learning']:
            urls.append(f"{self.blog_base_url}{category}/{slug}/")
        
        # Pattern 2: Common AWS announcement patterns
        if query.lower().startswith('introducing'):
            aws_slug = slug.replace('introducing-', '')
            urls.append(f"{self.blog_base_url}aws/{aws_slug}/")
            urls.append(f"{self.blog_base_url}aws/introducing-{aws_slug}/")
        
        return urls
    
    async def _verify_url_exists(self, url: str) -> bool:
        """Verify if a URL exists without fetching full content."""
        try:
            response = await self.client.head(url)
            return response.status_code == 200
        except:
            return False
    
    async def _extract_blog_post(self, url: str) -> Optional[Dict[str, Any]]:
        """Extract blog post information from URL."""
        try:
            response = await self.client.get(url)
            if response.status_code != 200:
                return None
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title using multiple strategies
            title = self._extract_title(soup)
            if not title:
                return None
            
            # Extract other metadata
            excerpt = self._extract_excerpt(soup)
            date = self._extract_date(soup)
            category = self._extract_category(url, soup)
            
            return {
                'title': title,
                'url': url,
                'excerpt': excerpt,
                'date': date,
                'category': category,
                'similarity_score': 1.0  # Direct URL match
            }
        except Exception as e:
            logger.error(f"Error extracting blog post from {url}: {e}")
            return None
    
    def _extract_title(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract title using multiple strategies."""
        # Strategy 1: Meta tags
        title_meta = soup.find('meta', property='og:title')
        if title_meta:
            return title_meta.get('content', '').strip()
        
        # Strategy 2: Title tag
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text().strip()
            # Clean up common suffixes
            title = re.sub(r'\s*\|\s*AWS.*$', '', title)
            return title
        
        # Strategy 3: H1 tags
        h1 = soup.find('h1')
        if h1:
            return h1.get_text().strip()
        
        return None
    
    def _extract_excerpt(self, soup: BeautifulSoup) -> str:
        """Extract excerpt/description."""
        # Try meta description first
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            return meta_desc.get('content', '').strip()
        
        # Try first paragraph
        first_p = soup.find('p')
        if first_p:
            return first_p.get_text().strip()[:200] + "..."
        
        return ""
    
    def _extract_date(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract publication date."""
        # Try various date selectors
        date_selectors = [
            'time[datetime]',
            '.date',
            '.publish-date',
            '[data-date]'
        ]
        
        for selector in date_selectors:
            date_elem = soup.select_one(selector)
            if date_elem:
                return date_elem.get('datetime') or date_elem.get_text().strip()
        
        return None
    
    def _extract_category(self, url: str, soup: BeautifulSoup) -> str:
        """Extract category from URL or content."""
        # Extract from URL
        url_parts = url.split('/blogs/')
        if len(url_parts) > 1:
            category_part = url_parts[1].split('/')[0]
            return category_part
        
        return "unknown"
    
    async def _search_in_category(self, query_normalized: Dict[str, Any], category: str, limit: int) -> List[Dict[str, Any]]:
        """Search within a specific category with robust parsing."""
        results = []
        
        # Get category URL
        category_url = f"{self.blog_base_url}{category}/"
        
        try:
            # Check cache first
            cache_key = f"{category}_{hash(str(query_normalized))}"
            if self._is_cache_valid(cache_key):
                return self._category_cache[cache_key][:limit]
            
            response = await self.client.get(category_url)
            if response.status_code != 200:
                return results
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Use multiple parsing strategies
            for selector in self.title_selectors:
                if len(results) >= limit:
                    break
                
                elements = soup.select(selector)
                for element in elements:
                    if len(results) >= limit:
                        break
                    
                    title = element.get_text(strip=True)
                    href = element.get('href')
                    
                    if not title or not href:
                        continue
                    
                    # Normalize URL
                    if not href.startswith('http'):
                        href = urljoin(self.base_url, href)
                    
                    # Calculate similarity
                    similarity = self._calculate_comprehensive_similarity(query_normalized, title)
                    
                    if similarity > 0.3:  # Lower threshold for broader matching
                        results.append({
                            'title': title,
                            'url': href,
                            'category': category,
                            'similarity_score': similarity,
                            'excerpt': ""  # Will be filled later if needed
                        })
            
            # Cache results
            self._category_cache[cache_key] = results
            self._cache_expiry[cache_key] = datetime.now() + self.cache_duration
            
        except Exception as e:
            logger.error(f"Error searching in category {category}: {e}")
        
        return results[:limit]
    
    async def _search_all_categories(self, query_normalized: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
        """Search across all known categories."""
        results = []
        
        # Prioritize categories based on query content
        prioritized_categories = self._prioritize_categories(query_normalized)
        
        for category in prioritized_categories:
            if len(results) >= limit:
                break
            
            category_results = await self._search_in_category(query_normalized, category, limit - len(results))
            results.extend(category_results)
        
        return results
    
    def _prioritize_categories(self, query_normalized: Dict[str, Any]) -> List[str]:
        """Prioritize categories based on query content."""
        keywords = query_normalized['keywords']
        
        # Category keyword mapping
        category_keywords = {
            'aws': ['aws', 'amazon', 'introducing', 'announcement'],
            'machine-learning': ['ai', 'ml', 'machine', 'learning', 'bedrock', 'sagemaker'],
            'compute': ['ec2', 'lambda', 'compute', 'serverless'],
            'networking-and-content-delivery': ['load', 'balancer', 'gateway', 'vpc', 'network'],
            'architecture': ['architecture', 'design', 'pattern'],
            'security': ['security', 'firewall', 'protection'],
            'developer': ['developer', 'development', 'api'],
            'containers': ['container', 'docker', 'kubernetes', 'ecs', 'eks']
        }
        
        # Score categories based on keyword matches
        category_scores = {}
        for category, cat_keywords in category_keywords.items():
            score = sum(1 for keyword in keywords if any(ck in keyword for ck in cat_keywords))
            if score > 0:
                category_scores[category] = score
        
        # Sort by score and add remaining categories
        prioritized = sorted(category_scores.keys(), key=lambda x: category_scores[x], reverse=True)
        remaining = [cat for cat in self.known_categories if cat not in prioritized]
        
        return prioritized + remaining
    
    def _calculate_comprehensive_similarity(self, query_normalized: Dict[str, Any], title: str) -> float:
        """Calculate comprehensive similarity score."""
        title_lower = title.lower()
        
        # Exact match
        if query_normalized['lower'] == title_lower:
            return 1.0
        
        # Substring match
        if query_normalized['lower'] in title_lower:
            return 0.9
        
        # Keyword matching
        keyword_matches = sum(1 for keyword in query_normalized['keywords'] if keyword in title_lower)
        keyword_score = keyword_matches / len(query_normalized['keywords']) if query_normalized['keywords'] else 0
        
        # Sequence matching
        sequence_score = SequenceMatcher(None, query_normalized['lower'], title_lower).ratio()
        
        # Combined score
        return max(keyword_score * 0.7 + sequence_score * 0.3, sequence_score)
    
    def _matches_query(self, blog_post: Dict[str, Any], query_normalized: Dict[str, Any]) -> bool:
        """Check if blog post matches the query."""
        title = blog_post.get('title', '').lower()
        excerpt = blog_post.get('excerpt', '').lower()
        
        # Check for keyword matches
        for keyword in query_normalized['keywords']:
            if keyword in title or keyword in excerpt:
                return True
        
        # Check for partial matches
        return self._calculate_comprehensive_similarity(query_normalized, title) > 0.3
    
    async def _fuzzy_search_fallback(self, query_normalized: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
        """Fuzzy search fallback using different strategies."""
        # This would implement additional fuzzy matching strategies
        # For now, return empty list
        return []
    
    async def _sitemap_search(self, query_normalized: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
        """Search using sitemap as last resort."""
        # This would implement sitemap-based search
        # For now, return empty list
        return []
    
    def _deduplicate_and_rank(self, results: List[Dict[str, Any]], query_normalized: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Remove duplicates and rank results by relevance."""
        seen_urls = set()
        unique_results = []
        
        for result in results:
            url = result.get('url', '')
            if url not in seen_urls:
                seen_urls.add(url)
                unique_results.append(result)
        
        # Sort by similarity score
        return sorted(unique_results, key=lambda x: x.get('similarity_score', 0), reverse=True)
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cache entry is still valid."""
        return (cache_key in self._category_cache and 
                cache_key in self._cache_expiry and 
                datetime.now() < self._cache_expiry[cache_key])