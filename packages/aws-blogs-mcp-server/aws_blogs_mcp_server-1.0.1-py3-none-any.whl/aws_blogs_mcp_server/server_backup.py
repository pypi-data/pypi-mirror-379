#!/usr/bin/env python3
"""
AWS Blogs MCP Server

A Model Context Protocol server that provides access to AWS blog content.
Allows searching and fetching blog posts from aws.amazon.com.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Sequence
from urllib.parse import urljoin, urlparse
import re
from difflib import SequenceMatcher

import httpx
from bs4 import BeautifulSoup
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.server.lowlevel import NotificationOptions
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
)
import mcp.server.stdio
import mcp.types as types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("aws-blogs-mcp-server")

# All real AWS blog categories extracted from aws.amazon.com/blogs
KNOWN_CATEGORIES = [
    "dotnet",
    "mt",
    "aws-insights",
    "awsmarketplace",
    "aws",
    "apn",
    "smb",
    "gametech",
    "architecture",
    "machine-learning",
    "big-data",
    "business-intelligence",
    "business-productivity",
    "enterprise-strategy",
    "aws-cloud-financial-management",
    "compute",
    "contact-center",
    "containers",
    "database",
    "desktop-and-application-streaming",
    "devops",
    "developer",
    "mobile",
    "hpc",
    "ibm-redhat",
    "industries",
    "infrastructure-and-automation",
    "iot",
    "media",
    "messaging-and-targeting",
    "modernizing-with-aws",
    "migration-and-modernization",
    "networking-and-content-delivery",
    "opensource",
    "publicsector",
    "quantum-computing",
    "robotics",
    "awsforsap",
    "spatial",
    "startups",
    "storage",
    "supply-chain",
    "training-and-certification",
    "security",  # Special case: aws.amazon.com/security/blog/
]

# Category names mapping
CATEGORY_NAMES = {
    "dotnet": ".NET on AWS",
    "mt": "AWS Cloud Operations",
    "aws-insights": "AWS Insights",
    "awsmarketplace": "AWS Marketplace",
    "aws": "AWS News",
    "apn": "AWS Partner Network",
    "smb": "AWS Smart Business",
    "gametech": "AWS for Games",
    "architecture": "Architecture",
    "machine-learning": "Artificial Intelligence",
    "big-data": "Big Data",
    "business-intelligence": "Business Intelligence",
    "business-productivity": "Business Productivity",
    "enterprise-strategy": "Cloud Enterprise Strategy",
    "aws-cloud-financial-management": "Cloud Financial Management",
    "compute": "Compute",
    "contact-center": "Contact Center",
    "containers": "Containers",
    "database": "Database",
    "desktop-and-application-streaming": "Desktop & Application Streaming",
    "devops": "DevOps & Developer Productivity",
    "developer": "Developer Tools",
    "mobile": "Front-End Web & Mobile",
    "hpc": "HPC",
    "ibm-redhat": "IBM & Red Hat",
    "industries": "Industries",
    "infrastructure-and-automation": "Integration & Automation",
    "iot": "Internet of Things",
    "media": "Media",
    "messaging-and-targeting": "Messaging & Targeting",
    "modernizing-with-aws": "Microsoft Workloads on AWS",
    "migration-and-modernization": "Migration & Modernization",
    "networking-and-content-delivery": "Networking & Content Delivery",
    "opensource": "Open Source",
    "publicsector": "Public Sector",
    "quantum-computing": "Quantum Technologies",
    "robotics": "Robotics",
    "awsforsap": "SAP",
    "spatial": "Spatial Computing",
    "startups": "Startups",
    "storage": "Storage",
    "supply-chain": "Supply Chain & Logistics",
    "training-and-certification": "Training & Certification",
    "security": "Security",
}

class AWSBlogsServer:
    """MCP Server for AWS Blogs content."""
    
    def __init__(self):
        self.base_url = "https://aws.amazon.com"
        self.blog_base_url = "https://aws.amazon.com/blogs/"
        self.blog_edition_url = "https://aws.amazon.com/blog/"  # Additional blog path
        self.security_blog_url = "https://aws.amazon.com/security/blog/"  # Special security blog
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (compatible; AWS-Blogs-MCP-Server/1.0)"
            }
        )
    
    async def close(self):
        """Clean up resources."""
        await self.client.aclose()
    
    async def search_blogs(self, query: str, category: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Search AWS blogs for posts matching the query."""
        try:
            blog_posts = []
            
            # Strategy 1: Search within a specific category if provided
            if category:
                # Convert category name to URL format
                category_slug = category.lower().replace(' ', '-').replace('&', '').replace('  ', '-')
                
                # Map display names back to URL paths
                category_path = None
                for path, display_name in CATEGORY_NAMES.items():
                    if display_name.lower() == category.lower():
                        category_path = path
                        break
                
                if not category_path:
                    # Fallback: try to match the slug
                    category_path = category_slug
                
                # Build category URLs - handle special cases
                category_urls = []
                if category_path == 'security':
                    category_urls.append(self.security_blog_url)
                else:
                    category_urls.extend([
                        f"{self.blog_base_url}{category_path}/",
                        f"{self.blog_edition_url}{category_path}/"
                    ])
                
                for category_url in category_urls:
                    try:
                        logger.info(f"Searching in category: {category_url}")
                        category_response = await self.client.get(category_url)
                        if category_response.status_code == 200:
                            category_soup = BeautifulSoup(category_response.text, 'html.parser')
                            category_posts = await self._extract_posts_from_page(category_soup, query, limit - len(blog_posts))
                            blog_posts.extend(category_posts)
                            
                            if len(blog_posts) >= limit:
                                break
                                
                    except Exception as e:
                        logger.warning(f"Could not search in category {category_url}: {e}")
            
            # Strategy 2: Use AWS blog search if available
            if len(blog_posts) < limit:
                search_urls = [
                    f"{self.blog_base_url}?s={query}",
                    f"{self.blog_edition_url}?s={query}",
                    f"https://aws.amazon.com/search/?searchPath=blog&searchQuery={query}",
                    f"https://aws.amazon.com/blogs/search/?q={query}",
                    f"https://aws.amazon.com/blog/search/?q={query}",
                    f"{self.security_blog_url}?s={query}"  # Include security blog search
                ]
                
                for search_url in search_urls:
                    try:
                        logger.info(f"Searching with URL: {search_url}")
                        response = await self.client.get(search_url)
                        
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            search_posts = await self._extract_posts_from_page(soup, query, limit - len(blog_posts))
                            blog_posts.extend(search_posts)
                            
                            if len(blog_posts) >= limit:
                                break
                                
                    except Exception as e:
                        logger.warning(f"Search URL {search_url} failed: {e}")
                        continue
            
            # Strategy 3: Fallback - search recent posts from all main blog pages
            if len(blog_posts) < limit:
                fallback_urls = [self.blog_base_url, self.blog_edition_url, self.security_blog_url]
                
                for fallback_url in fallback_urls:
                    if len(blog_posts) >= limit:
                        break
                        
                    try:
                        logger.info(f"Fallback: searching recent posts from {fallback_url}")
                        response = await self.client.get(fallback_url)
                        
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            recent_posts = await self._extract_posts_from_page(soup, query, limit - len(blog_posts))
                            blog_posts.extend(recent_posts)
                            
                    except Exception as e:
                        logger.warning(f"Fallback search failed for {fallback_url}: {e}")
            
            # Remove duplicates based on URL
            seen_urls = set()
            unique_posts = []
            for post in blog_posts:
                if post.get('url') and post['url'] not in seen_urls:
                    seen_urls.add(post['url'])
                    unique_posts.append(post)
            
            return unique_posts[:limit]
            
        except Exception as e:
            logger.error(f"Error searching blogs: {e}")
            return []
    
    async def _extract_posts_from_page(self, soup: BeautifulSoup, query: str = "", limit: int = 10) -> List[Dict[str, Any]]:
        """Extract blog posts from a page, optionally filtering by query."""
        posts = []
        
        # Improved extraction logic - more flexible and reliable
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Look for blog post patterns - check for actual blog post URLs
            is_blog_post = False
            category = ""
            
            # Check different blog URL patterns
            if '/blogs/' in href and href.count('/') >= 4:
                # Extract category from /blogs/category/post-title/ pattern
                parts = href.split('/blogs/')[-1].split('/')
                if parts and parts[0]:
                    category = CATEGORY_NAMES.get(parts[0], parts[0].replace('-', ' ').title())
                is_blog_post = True
            elif '/blog/' in href and href.count('/') >= 4:
                # Extract category from /blog/category/post-title/ pattern
                parts = href.split('/blog/')[-1].split('/')
                if parts and parts[0]:
                    category = CATEGORY_NAMES.get(parts[0], parts[0].replace('-', ' ').title())
                is_blog_post = True
            elif '/security/blog/' in href and href.count('/') >= 3:
                category = "Security"
                is_blog_post = True
            
            if is_blog_post:
                # Skip unwanted links
                if any(skip in href for skip in ['/page/', '/feed/', '/?', '#', '/category/', '/tag/', '/author/']):
                    continue
                
                # Must have meaningful title text
                if not text or len(text) < 10 or text.lower().startswith(('read more', 'continue', 'learn more', 'view all')):
                    continue
                
                # Extract additional info from parent elements
                parent = link.parent
                excerpt = ""
                date = ""
                
                if parent:
                    # Look for excerpt in nearby elements
                    for elem in parent.find_all(['p', 'div'], limit=3):
                        elem_text = elem.get_text(strip=True)
                        if elem_text and len(elem_text) > 20 and elem_text != text:
                            excerpt = elem_text[:200] + "..." if len(elem_text) > 200 else elem_text
                            break
                    
                    # Look for date
                    date_elem = parent.find(['time', 'span'], class_=lambda x: x and 'date' in str(x).lower())
                    if date_elem:
                        date = date_elem.get_text(strip=True)
                
                # Create post data
                post_data = {
                    'title': text,
                    'url': href if href.startswith('http') else f'https://aws.amazon.com{href}',
                    'excerpt': excerpt,
                    'date': date,
                    'category': category
                }
                
                # Filter by query if provided
                if not query or self._matches_query(post_data, query):
                    posts.append(post_data)
                    
                    if len(posts) >= limit:
                        break
        
        return posts
    
    async def find_similar_blogs(self, blog_idea: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Find blogs similar to the given idea with similarity scores."""
        try:
            # Get posts from multiple categories for broader coverage
            all_posts = []
            
            # Search in key categories that are most likely to have diverse content
            key_categories = [
                'architecture', 'machine-learning', 'compute', 'database', 
                'containers', 'devops', 'security', 'storage', 'mobile'
            ]
            
            for category in key_categories:
                try:
                    category_url = f"{self.blog_base_url}{category}/"
                    response = await self.client.get(category_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        posts = await self._extract_posts_from_page(soup, "", 15)  # Get more posts per category
                        all_posts.extend(posts)
                except Exception as e:
                    logger.warning(f"Could not fetch from category {category}: {e}")
                    continue
            
            # Also get recent posts from main blog pages
            for main_url in [self.blog_base_url, self.security_blog_url]:
                try:
                    response = await self.client.get(main_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        posts = await self._extract_posts_from_page(soup, "", 10)
                        all_posts.extend(posts)
                except Exception as e:
                    logger.warning(f"Could not fetch from {main_url}: {e}")
            
            # Remove duplicates based on URL
            seen_urls = set()
            unique_posts = []
            for post in all_posts:
                if post.get('url') and post['url'] not in seen_urls:
                    seen_urls.add(post['url'])
                    unique_posts.append(post)
            
            logger.info(f"Collected {len(unique_posts)} unique posts for similarity analysis")
            
            # Fetch full content for top posts (to avoid too many requests, we'll do this in batches)
            # First, do a quick similarity check on titles/excerpts to get top candidates
            quick_scored_posts = []
            for post in unique_posts:
                quick_score = self._calculate_quick_similarity(blog_idea, post)
                quick_scored_posts.append({
                    **post,
                    'quick_score': quick_score
                })
            
            # Sort by quick score and take top candidates for full content analysis
            quick_scored_posts.sort(key=lambda x: x['quick_score'], reverse=True)
            top_candidates = quick_scored_posts[:min(30, len(quick_scored_posts))]  # Analyze top 30 candidates
            
            logger.info(f"Analyzing full content for top {len(top_candidates)} candidates")
            
            # Fetch full content and calculate detailed similarity
            detailed_scored_posts = []
            for post in top_candidates:
                try:
                    # Fetch full blog post content
                    full_post_data = await self.get_blog_post(post['url'])
                    if full_post_data:
                        # Use the full content for similarity calculation
                        enhanced_post = {
                            **post,
                            'full_content': full_post_data.get('content', ''),
                            'author': full_post_data.get('author', ''),
                            'tags': full_post_data.get('tags', [])
                        }
                        
                        # Calculate detailed similarity with full content
                        similarity_score = self._calculate_detailed_similarity(blog_idea, enhanced_post)
                        is_exact_match = self._is_exact_match(blog_idea, enhanced_post)
                        
                        detailed_scored_posts.append({
                            **enhanced_post,
                            'similarity_score': similarity_score,
                            'is_exact_match': is_exact_match,
                            'match_percentage': round(similarity_score * 100, 1)
                        })
                    else:
                        # Fallback to quick similarity if full content fetch fails
                        similarity_score = post['quick_score']
                        is_exact_match = self._is_exact_match(blog_idea, post)
                        
                        detailed_scored_posts.append({
                            **post,
                            'similarity_score': similarity_score,
                            'is_exact_match': is_exact_match,
                            'match_percentage': round(similarity_score * 100, 1)
                        })
                        
                except Exception as e:
                    logger.warning(f"Could not fetch full content for {post['url']}: {e}")
                    # Fallback to quick similarity
                    similarity_score = post['quick_score']
                    is_exact_match = self._is_exact_match(blog_idea, post)
                    
                    detailed_scored_posts.append({
                        **post,
                        'similarity_score': similarity_score,
                        'is_exact_match': is_exact_match,
                        'match_percentage': round(similarity_score * 100, 1)
                    })
            
            # Sort by detailed similarity score (descending)
            detailed_scored_posts.sort(key=lambda x: x['similarity_score'], reverse=True)
            
            # Return top results
            return detailed_scored_posts[:limit]
            
        except Exception as e:
            logger.error(f"Error finding similar blogs: {e}")
            return []
    
    def _calculate_quick_similarity(self, blog_idea: str, post: Dict[str, Any]) -> float:
        """Calculate quick similarity score using only title and excerpt (for initial filtering)."""
        try:
            # Normalize inputs
            idea_lower = blog_idea.lower()
            title_lower = post.get('title', '').lower()
            excerpt_lower = post.get('excerpt', '').lower()
            category_lower = post.get('category', '').lower()
            
            # Extract words
            idea_words = set(re.findall(r'\b\w+\b', idea_lower))
            title_words = set(re.findall(r'\b\w+\b', title_lower))
            excerpt_words = set(re.findall(r'\b\w+\b', excerpt_lower))
            category_words = set(re.findall(r'\b\w+\b', category_lower))
            
            # Remove common stop words
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'how', 'what', 'when', 'where', 'why', 'who', 'which', 'this', 'that', 'these', 'those'}
            
            idea_words -= stop_words
            title_words -= stop_words
            excerpt_words -= stop_words
            category_words -= stop_words
            
            if not idea_words:
                return 0.0
            
            # Calculate similarity components
            title_intersection = idea_words.intersection(title_words)
            title_similarity = len(title_intersection) / len(idea_words) if idea_words else 0
            
            excerpt_intersection = idea_words.intersection(excerpt_words)
            excerpt_similarity = len(excerpt_intersection) / len(idea_words) if idea_words else 0
            
            category_intersection = idea_words.intersection(category_words)
            category_similarity = len(category_intersection) / len(idea_words) if idea_words else 0
            
            # Sequence similarity for title
            title_seq_similarity = SequenceMatcher(None, idea_lower, title_lower).ratio()
            
            # Weighted combination for quick scoring
            quick_score = (
                title_similarity * 0.5 +           # Title match is most important for quick filtering
                excerpt_similarity * 0.3 +        # Excerpt content
                category_similarity * 0.1 +       # Category relevance
                title_seq_similarity * 0.1        # Phrase similarity
            )
            
            return min(quick_score, 1.0)
            
        except Exception as e:
            logger.error(f"Error calculating quick similarity: {e}")
            return 0.0
    
    def _calculate_detailed_similarity(self, blog_idea: str, post: Dict[str, Any]) -> float:
        """Calculate detailed similarity score using full blog content."""
        try:
            # Normalize inputs
            idea_lower = blog_idea.lower()
            title_lower = post.get('title', '').lower()
            excerpt_lower = post.get('excerpt', '').lower()
            category_lower = post.get('category', '').lower()
            content_lower = post.get('full_content', '').lower()
            
            # Extract words from all sources
            idea_words = set(re.findall(r'\b\w+\b', idea_lower))
            title_words = set(re.findall(r'\b\w+\b', title_lower))
            excerpt_words = set(re.findall(r'\b\w+\b', excerpt_lower))
            category_words = set(re.findall(r'\b\w+\b', category_lower))
            content_words = set(re.findall(r'\b\w+\b', content_lower))
            
            # Extract tags if available
            tags_text = ' '.join(post.get('tags', [])).lower()
            tags_words = set(re.findall(r'\b\w+\b', tags_text))
            
            # Remove common stop words
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'how', 'what', 'when', 'where', 'why', 'who', 'which', 'this', 'that', 'these', 'those', 'also', 'just', 'now', 'then', 'here', 'there', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'should', 'now'}
            
            idea_words -= stop_words
            title_words -= stop_words
            excerpt_words -= stop_words
            category_words -= stop_words
            content_words -= stop_words
            tags_words -= stop_words
            
            if not idea_words:
                return 0.0
            
            # Calculate different similarity components
            
            # 1. Title similarity (highest weight)
            title_intersection = idea_words.intersection(title_words)
            title_similarity = len(title_intersection) / len(idea_words) if idea_words else 0
            
            # 2. Content similarity (very important for detailed analysis)
            content_intersection = idea_words.intersection(content_words)
            content_similarity = len(content_intersection) / len(idea_words) if idea_words else 0
            
            # 3. Excerpt similarity
            excerpt_intersection = idea_words.intersection(excerpt_words)
            excerpt_similarity = len(excerpt_intersection) / len(idea_words) if idea_words else 0
            
            # 4. Tags similarity
            tags_intersection = idea_words.intersection(tags_words)
            tags_similarity = len(tags_intersection) / len(idea_words) if idea_words else 0
            
            # 5. Category similarity
            category_intersection = idea_words.intersection(category_words)
            category_similarity = len(category_intersection) / len(idea_words) if idea_words else 0
            
            # 6. Sequence similarity for title and content
            title_seq_similarity = SequenceMatcher(None, idea_lower, title_lower).ratio()
            
            # For content, we'll check similarity with first 500 characters to avoid performance issues
            content_preview = content_lower[:500] if content_lower else ''
            content_seq_similarity = SequenceMatcher(None, idea_lower, content_preview).ratio()
            
            # 7. Technical terms matching (enhanced)
            tech_terms = {
                'aws', 'amazon', 'lambda', 'ec2', 's3', 'rds', 'dynamodb', 'cloudformation', 
                'kubernetes', 'docker', 'serverless', 'microservices', 'api', 'rest', 'graphql', 
                'machine learning', 'ai', 'ml', 'data', 'analytics', 'security', 'devops', 'cicd', 
                'terraform', 'ansible', 'jenkins', 'github', 'gitlab', 'monitoring', 'logging', 
                'vpc', 'iam', 'cloudwatch', 'sns', 'sqs', 'kinesis', 'redshift', 'athena', 
                'glue', 'sagemaker', 'bedrock', 'ecs', 'fargate', 'eks', 'ecr', 'elb', 'alb', 
                'cloudfront', 'route53', 'acm', 'waf', 'shield', 'cognito', 'amplify'
            }
            
            idea_tech_terms = idea_words.intersection(tech_terms)
            post_tech_terms = title_words.union(content_words).union(tags_words).intersection(tech_terms)
            tech_match = len(idea_tech_terms.intersection(post_tech_terms)) / max(len(idea_tech_terms), 1) if idea_tech_terms else 0
            
            # 8. Concept similarity (check for related concepts)
            concept_groups = {
                'serverless': {'lambda', 'serverless', 'functions', 'faas', 'event-driven'},
                'containers': {'docker', 'kubernetes', 'ecs', 'fargate', 'containers', 'pods'},
                'data': {'database', 'data', 'analytics', 'etl', 'warehouse', 'lake'},
                'ml': {'machine learning', 'ai', 'ml', 'model', 'training', 'inference'},
                'security': {'security', 'iam', 'authentication', 'authorization', 'encryption'},
                'monitoring': {'monitoring', 'logging', 'observability', 'metrics', 'alerts'}
            }
            
            concept_similarity = 0.0
            for concept, related_terms in concept_groups.items():
                if any(term in idea_lower for term in related_terms):
                    post_all_words = title_words.union(content_words).union(tags_words)
                    if any(term in ' '.join(post_all_words) for term in related_terms):
                        concept_similarity += 0.1
            
            concept_similarity = min(concept_similarity, 1.0)
            
            # Weighted combination for detailed scoring
            final_score = (
                title_similarity * 0.25 +          # Title match
                content_similarity * 0.35 +        # Content match (most important for detailed analysis)
                excerpt_similarity * 0.1 +         # Excerpt match
                tags_similarity * 0.1 +            # Tags match
                category_similarity * 0.05 +       # Category match
                title_seq_similarity * 0.05 +      # Title phrase similarity
                content_seq_similarity * 0.05 +    # Content phrase similarity
                tech_match * 0.03 +                # Technical terms match
                concept_similarity * 0.02          # Concept similarity
            )
            
            return min(final_score, 1.0)  # Cap at 1.0
            
        except Exception as e:
            logger.error(f"Error calculating detailed similarity: {e}")
            return 0.0
    
    def _is_exact_match(self, blog_idea: str, post: Dict[str, Any]) -> bool:
        """Check if the post is an exact or very close match to the blog idea."""
        try:
            idea_lower = blog_idea.lower().strip()
            title_lower = post.get('title', '').lower().strip()
            content_lower = post.get('full_content', '').lower()
            
            # Check for exact title match
            if idea_lower == title_lower:
                return True
            
            # Check for very high sequence similarity (95%+) with title
            seq_similarity = SequenceMatcher(None, idea_lower, title_lower).ratio()
            if seq_similarity >= 0.95:
                return True
            
            # Check if blog idea is contained in title or vice versa (with high similarity)
            if len(idea_lower) > 10 and len(title_lower) > 10:
                if idea_lower in title_lower or title_lower in idea_lower:
                    # Additional check: ensure significant word overlap
                    idea_words = set(re.findall(r'\b\w+\b', idea_lower))
                    title_words = set(re.findall(r'\b\w+\b', title_lower))
                    overlap = len(idea_words.intersection(title_words))
                    if overlap >= min(len(idea_words), len(title_words)) * 0.8:
                        return True
            
            # Check for high similarity with content (if available)
            if content_lower and len(content_lower) > 100:
                # Check if the blog idea appears as a significant phrase in the content
                if len(idea_lower) > 20 and idea_lower in content_lower:
                    return True
                
                # Check for very high word overlap with content preview
                content_preview = content_lower[:1000]  # First 1000 chars
                content_words = set(re.findall(r'\b\w+\b', content_preview))
                idea_words = set(re.findall(r'\b\w+\b', idea_lower))
                
                # Remove stop words for better matching
                stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
                idea_words -= stop_words
                content_words -= stop_words
                
                if idea_words and len(idea_words.intersection(content_words)) >= len(idea_words) * 0.9:
                    return True
            
            return False
            
        except Exception as e:
            logger.error(f"Error checking exact match: {e}")
            return False
    
    def _matches_query(self, post_data: Dict[str, Any], query: str) -> bool:
        """Check if a post matches the search query."""
        query_lower = query.lower()
        
        # Check title
        if query_lower in post_data.get('title', '').lower():
            return True
        
        # Check excerpt/description
        if query_lower in post_data.get('excerpt', '').lower():
            return True
        
        # Check tags
        tags = post_data.get('tags', [])
        if any(query_lower in tag.lower() for tag in tags):
            return True
        
        # Check category
        if query_lower in post_data.get('category', '').lower():
            return True
        
        return False
    
    async def get_blog_categories(self) -> List[str]:
        """Get available blog categories from AWS blogs."""
        try:
            # Return the comprehensive list of real AWS blog categories
            categories = []
            
            for category_path in KNOWN_CATEGORIES:
                # Get the display name from our mapping, or format the path
                display_name = CATEGORY_NAMES.get(category_path, category_path.replace('-', ' ').title())
                categories.append(display_name)
            
            # Sort categories alphabetically
            return sorted(categories)
            
        except Exception as e:
            logger.error(f"Error getting categories: {e}")
            # Return a basic fallback list
            return [
                'Architecture', 'Artificial Intelligence', 'AWS News', 'Big Data',
                'Compute', 'Containers', 'Database', 'Developer Tools', 'DevOps',
                'Machine Learning', 'Security', 'Storage'
            ]
    
    async def get_blog_post(self, url: str) -> Optional[Dict[str, Any]]:
        """Fetch full content of a specific blog post."""
        try:
            if not url.startswith('http'):
                url = urljoin(self.base_url, url)
            
            logger.info(f"Fetching blog post: {url}")
            response = await self.client.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract blog post content
            post_data = {
                'url': url,
                'title': self._extract_title(soup),
                'content': self._extract_content(soup),
                'author': self._extract_author(soup),
                'date': self._extract_date(soup),
                'tags': self._extract_tags(soup),
                'category': self._extract_category(soup),
            }
            
            return post_data
            
        except Exception as e:
            logger.error(f"Error fetching blog post {url}: {e}")
            return None
    
    async def _extract_post_data_from_link(self, link_elem) -> Optional[Dict[str, Any]]:
        """Extract post data from a blog post link element."""
        try:
            # Extract URL
            url = link_elem.get('href', '')
            if not url:
                return None
            
            if not url.startswith('http'):
                url = urljoin(self.base_url, url)
            
            # Extract title from link text or nearby elements
            title = ""
            
            # Try to get title from the link text itself
            link_text = link_elem.get_text(strip=True)
            if link_text and len(link_text) > 10:  # Reasonable title length
                title = link_text
            
            # If no good title from link text, look for nearby title elements
            if not title or len(title) < 10:
                # Look for title in parent or sibling elements
                parent = link_elem.parent
                if parent:
                    # Check for heading elements in parent
                    heading = parent.find(['h1', 'h2', 'h3', 'h4'])
                    if heading:
                        title = heading.get_text(strip=True)
                    
                    # Check for title class in parent or siblings
                    if not title:
                        title_elem = parent.find(['div', 'span', 'p'], class_=lambda x: x and 'title' in x.lower())
                        if title_elem:
                            title = title_elem.get_text(strip=True)
            
            # Extract excerpt from nearby elements
            excerpt = ""
            parent = link_elem.parent
            if parent:
                # Look for excerpt/summary/description elements
                excerpt_elem = parent.find(['p', 'div'], class_=lambda x: x and any(
                    term in x.lower() for term in ['excerpt', 'summary', 'description', 'preview']
                ))
                if excerpt_elem:
                    excerpt = excerpt_elem.get_text(strip=True)
                
                # Fallback: get first paragraph that's not the title
                if not excerpt:
                    paragraphs = parent.find_all('p')
                    for p in paragraphs:
                        p_text = p.get_text(strip=True)
                        if p_text and p_text != title and len(p_text) > 20:
                            excerpt = p_text
                            break
            
            # Extract date from nearby elements
            date = ""
            if parent:
                date_elem = parent.find(['time', 'span'], class_=lambda x: x and 'date' in x.lower())
                if date_elem:
                    date = date_elem.get_text(strip=True)
                    # Try datetime attribute if available
                    datetime_attr = date_elem.get('datetime')
                    if datetime_attr:
                        date = datetime_attr
            
            # Extract category from URL
            category = ""
            if '/blogs/' in url:
                parts = url.split('/blogs/')[-1].split('/')
                if parts and parts[0]:
                    category = CATEGORY_NAMES.get(parts[0], parts[0].replace('-', ' ').title())
            elif '/blog/' in url:
                parts = url.split('/blog/')[-1].split('/')
                if parts and parts[0]:
                    category = CATEGORY_NAMES.get(parts[0], parts[0].replace('-', ' ').title())
            elif '/security/blog/' in url:
                category = "Security"
            
            # Only return if we have at least a URL and some kind of title
            if url and (title or link_text):
                return {
                    'title': title or link_text or "Untitled Post",
                    'url': url,
                    'excerpt': excerpt,
                    'date': date,
                    'category': category,
                }
            
        except Exception as e:
            logger.error(f"Error extracting post data from link: {e}")
        
        return None
    
    async def _extract_post_data(self, container) -> Optional[Dict[str, Any]]:
        """Extract post data from a container element."""
        try:
            # Extract title
            title_elem = container.find(['h1', 'h2', 'h3'], class_=lambda x: x and 'title' in x.lower()) or \
                        container.find(['h1', 'h2', 'h3'])
            title = title_elem.get_text(strip=True) if title_elem else "No title"
            
            # Extract link
            link_elem = container.find('a', href=True)
            url = link_elem['href'] if link_elem else ""
            if url and not url.startswith('http'):
                url = urljoin(self.base_url, url)
            
            # Extract excerpt
            excerpt_elem = container.find(['p', 'div'], class_=lambda x: x and any(
                term in x.lower() for term in ['excerpt', 'summary', 'description']
            ))
            excerpt = excerpt_elem.get_text(strip=True) if excerpt_elem else ""
            
            # Extract date
            date_elem = container.find(['time', 'span'], class_=lambda x: x and 'date' in x.lower())
            date = date_elem.get_text(strip=True) if date_elem else ""
            
            if title and url:
                return {
                    'title': title,
                    'url': url,
                    'excerpt': excerpt,
                    'date': date,
                }
            
        except Exception as e:
            logger.error(f"Error extracting post data: {e}")
        
        return None
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract title from blog post page."""
        title_elem = soup.find('h1') or soup.find('title')
        return title_elem.get_text(strip=True) if title_elem else "No title"
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from blog post page."""
        # Look for main content containers with multiple strategies
        content_selectors = [
            # AWS-specific selectors
            '.aws-blog-content',
            '.blog-post-content',
            '.post-body',
            '.entry-body',
            
            # Generic blog selectors
            'article .content',
            'article .post-content',
            'article .entry-content',
            '.post-content',
            '.entry-content',
            '.blog-content',
            '.content',
            
            # Fallback selectors
            'article',
            'main',
            '.main-content',
            '#content',
            '#main'
        ]
        
        content_text = ""
        
        for selector in content_selectors:
            content_elem = soup.select_one(selector)
            if content_elem:
                # Remove unwanted elements
                for unwanted in content_elem(["script", "style", "nav", "header", "footer", "aside"]):
                    unwanted.decompose()
                
                # Remove social sharing buttons and ads
                for social in content_elem.find_all(['div', 'span'], class_=lambda x: x and any(
                    term in x.lower() for term in ['share', 'social', 'tweet', 'facebook', 'linkedin', 'ad', 'advertisement']
                )):
                    social.decompose()
                
                # Extract text with proper formatting
                content_text = content_elem.get_text(separator='\n', strip=True)
                
                # Clean up excessive whitespace
                lines = [line.strip() for line in content_text.split('\n') if line.strip()]
                content_text = '\n\n'.join(lines)
                
                if len(content_text) > 100:  # Only use if substantial content
                    break
        
        # Fallback: get all paragraph text if no main content found
        if not content_text or len(content_text) < 100:
            paragraphs = soup.find_all('p')
            paragraph_texts = []
            
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text and len(text) > 20:  # Skip very short paragraphs
                    paragraph_texts.append(text)
            
            content_text = '\n\n'.join(paragraph_texts)
        
        return content_text or "No content available"
    
    def _extract_author(self, soup: BeautifulSoup) -> str:
        """Extract author from blog post page."""
        # Multiple strategies to find author information
        author_selectors = [
            # AWS-specific author selectors
            '.author-name',
            '.post-author',
            '.blog-author',
            '.byline .author',
            '.byline a',
            
            # Generic author selectors
            '[class*="author"]',
            '[rel="author"]',
            '.byline',
            '.post-meta .author',
            '.entry-meta .author'
        ]
        
        for selector in author_selectors:
            author_elem = soup.select_one(selector)
            if author_elem:
                author_text = author_elem.get_text(strip=True)
                # Clean up common prefixes
                author_text = author_text.replace('By ', '').replace('Author: ', '').replace('Posted by ', '')
                if author_text and len(author_text) < 100:  # Reasonable author name length
                    return author_text
        
        # Fallback: look for "by" followed by a name
        text_content = soup.get_text()
        import re
        by_match = re.search(r'(?:by|By|BY)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', text_content)
        if by_match:
            return by_match.group(1)
        
        return ""
    
    def _extract_date(self, soup: BeautifulSoup) -> str:
        """Extract publication date from blog post page."""
        # Multiple strategies to find date information
        date_selectors = [
            # HTML5 time element
            'time[datetime]',
            'time',
            
            # AWS-specific date selectors
            '.post-date',
            '.publish-date',
            '.blog-date',
            '.entry-date',
            
            # Generic date selectors
            '[class*="date"]',
            '.byline .date',
            '.post-meta .date',
            '.entry-meta .date'
        ]
        
        for selector in date_selectors:
            date_elem = soup.select_one(selector)
            if date_elem:
                # Try to get datetime attribute first
                datetime_attr = date_elem.get('datetime')
                if datetime_attr:
                    return datetime_attr
                
                # Otherwise get text content
                date_text = date_elem.get_text(strip=True)
                if date_text and len(date_text) < 50:  # Reasonable date length
                    return date_text
        
        # Fallback: look for date patterns in text
        text_content = soup.get_text()
        import re
        
        # Look for common date patterns
        date_patterns = [
            r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}\b',
            r'\b\d{1,2}/\d{1,2}/\d{4}\b',
            r'\b\d{4}-\d{2}-\d{2}\b'
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, text_content)
            if match:
                return match.group(0)
        
        return ""
    
    def _extract_tags(self, soup: BeautifulSoup) -> List[str]:
        """Extract tags from blog post page."""
        tags = []
        
        # Multiple strategies to find tags
        tag_selectors = [
            # AWS-specific tag selectors
            '.post-tags',
            '.blog-tags',
            '.entry-tags',
            '.tags',
            
            # Generic tag selectors
            '[class*="tag"]',
            '.post-meta .tags',
            '.entry-meta .tags'
        ]
        
        for selector in tag_selectors:
            tag_container = soup.select_one(selector)
            if tag_container:
                # Look for tag links
                tag_links = tag_container.find_all('a')
                if tag_links:
                    tags.extend([link.get_text(strip=True) for link in tag_links if link.get_text(strip=True)])
                else:
                    # Look for comma-separated tags
                    tag_text = tag_container.get_text(strip=True)
                    if tag_text:
                        # Split by common separators
                        for separator in [',', '|', ';']:
                            if separator in tag_text:
                                tags.extend([tag.strip() for tag in tag_text.split(separator) if tag.strip()])
                                break
                        else:
                            # Single tag or space-separated
                            tags.append(tag_text)
                
                if tags:
                    break
        
        # Clean up tags
        cleaned_tags = []
        for tag in tags:
            clean_tag = tag.strip()
            if clean_tag and len(clean_tag) < 50 and clean_tag not in cleaned_tags:
                cleaned_tags.append(clean_tag)
        
        return cleaned_tags
    
    def _extract_category(self, soup: BeautifulSoup) -> str:
        """Extract category from blog post page."""
        # Multiple strategies to find category information
        category_selectors = [
            # AWS-specific category selectors
            '.post-category',
            '.blog-category',
            '.entry-category',
            
            # Generic category selectors
            '[class*="category"]',
            '.breadcrumb a:last-child',
            '.post-meta .category',
            '.entry-meta .category'
        ]
        
        for selector in category_selectors:
            category_elem = soup.select_one(selector)
            if category_elem:
                category_text = category_elem.get_text(strip=True)
                if category_text and len(category_text) < 50:
                    return category_text
        
        # Fallback: extract from URL if available
        canonical_link = soup.find('link', rel='canonical')
        if canonical_link:
            href = canonical_link.get('href', '')
            for pattern in ['/blogs/', '/blog/']:
                if pattern in href:
                    parts = href.split(pattern)[-1].split('/')
                    if parts and parts[0] and len(parts[0]) > 1:
                        return parts[0].replace('-', ' ').title()
        
        return ""


# Create the server instance
app = Server("aws-blogs-mcp-server")
blogs_server = AWSBlogsServer()


@app.list_tools()
async def handle_list_tools() -> List[Tool]:
    """List available tools."""
    return [
        Tool(
            name="search_aws_blogs",
            description="Search AWS blogs for posts matching a query",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query for blog posts"
                    },
                    "category": {
                        "type": "string",
                        "description": "Optional blog category to filter by"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="find_similar_blogs",
            description="Find AWS blogs similar to your blog idea with similarity scores and exact match detection",
            inputSchema={
                "type": "object",
                "properties": {
                    "blog_idea": {
                        "type": "string",
                        "description": "Your blog idea or topic to find similar existing posts for"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["blog_idea"]
            }
        ),
        Tool(
            name="get_blog_post",
            description="Fetch the full content of a specific AWS blog post",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL of the blog post to fetch"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="get_blog_categories",
            description="Get available AWS blog categories",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]


@app.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> List[types.TextContent]:
    """Handle tool calls."""
    try:
        if name == "search_aws_blogs":
            query = arguments.get("query", "")
            category = arguments.get("category")
            limit = arguments.get("limit", 10)
            
            results = await blogs_server.search_blogs(query, category, limit)
            
            if not results:
                return [types.TextContent(
                    type="text",
                    text=f"No blog posts found for query: {query}"
                )]
            
            # Format results
            formatted_results = []
            for post in results:
                formatted_results.append(
                    f"**{post['title']}**\n"
                    f"URL: {post['url']}\n"
                    f"Date: {post.get('date', 'N/A')}\n"
                    f"Excerpt: {post.get('excerpt', 'No excerpt available')}\n"
                )
            
            return [types.TextContent(
                type="text",
                text=f"Found {len(results)} blog posts:\n\n" + "\n---\n".join(formatted_results)
            )]
        
        elif name == "find_similar_blogs":
            blog_idea = arguments.get("blog_idea", "")
            limit = arguments.get("limit", 10)
            
            if not blog_idea:
                return [types.TextContent(
                    type="text",
                    text="Error: Blog idea is required"
                )]
            
            results = await blogs_server.find_similar_blogs(blog_idea, limit)
            
            if not results:
                return [types.TextContent(
                    type="text",
                    text=f"No similar blog posts found for idea: {blog_idea}"
                )]
            
            # Format results with similarity scores
            formatted_results = []
            exact_matches = []
            
            for i, post in enumerate(results, 1):
                match_indicator = "🎯 EXACT MATCH" if post.get('is_exact_match') else f"{post.get('match_percentage', 0)}% match"
                
                if post.get('is_exact_match'):
                    exact_matches.append(post)
                
                formatted_results.append(
                    f"**{i}. {post['title']}** ({match_indicator})\n"
                    f"URL: {post['url']}\n"
                    f"Category: {post.get('category', 'N/A')}\n"
                    f"Date: {post.get('date', 'N/A')}\n"
                    f"Excerpt: {post.get('excerpt', 'No excerpt available')[:150]}{'...' if len(post.get('excerpt', '')) > 150 else ''}\n"
                )
            
            # Create summary
            summary = f"**Blog Idea Analysis: \"{blog_idea}\"**\n\n"
            
            if exact_matches:
                summary += f"🎯 **Found {len(exact_matches)} exact match(es)!**\n\n"
            else:
                summary += f"📊 **Top {len(results)} similar posts (no exact matches found):**\n\n"
            
            return [types.TextContent(
                type="text",
                text=summary + "\n---\n".join(formatted_results)
            )]
        
        elif name == "get_blog_post":
            url = arguments.get("url", "")
            if not url:
                return [types.TextContent(
                    type="text",
                    text="Error: URL is required"
                )]
            
            post_data = await blogs_server.get_blog_post(url)
            
            if not post_data:
                return [types.TextContent(
                    type="text",
                    text=f"Could not fetch blog post from URL: {url}"
                )]
            
            # Format the blog post content
            content = f"# {post_data['title']}\n\n"
            if post_data.get('author'):
                content += f"**Author:** {post_data['author']}\n"
            if post_data.get('date'):
                content += f"**Date:** {post_data['date']}\n"
            if post_data.get('category'):
                content += f"**Category:** {post_data['category']}\n"
            if post_data.get('tags'):
                content += f"**Tags:** {', '.join(post_data['tags'])}\n"
            
            content += f"**URL:** {post_data['url']}\n\n"
            content += "## Content\n\n"
            content += post_data.get('content', 'No content available')
            
            return [types.TextContent(
                type="text",
                text=content
            )]
        
        elif name == "get_blog_categories":
            categories = await blogs_server.get_blog_categories()
            
            if not categories:
                return [types.TextContent(
                    type="text",
                    text="No blog categories found"
                )]
            
            return [types.TextContent(
                type="text",
                text=f"Available AWS blog categories:\n\n" + "\n".join(f"- {cat}" for cat in categories)
            )]
        
        else:
            return [types.TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
    
    except Exception as e:
        logger.error(f"Error in tool {name}: {e}")
        return [types.TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]


def main():
    """Main entry point for the server."""
    asyncio.run(run_server())


async def run_server():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="aws-blogs-mcp-server",
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(
                        tools_changed=False,
                        resources_changed=False,
                        prompts_changed=False,
                    ),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    main()