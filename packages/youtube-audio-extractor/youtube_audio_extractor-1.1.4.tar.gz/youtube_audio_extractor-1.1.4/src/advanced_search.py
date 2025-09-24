"""Advanced search functionality for YouTube Audio Extractor."""

import re
import time
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import yt_dlp

from .utils import VideoInfo, sanitize_filename
from .errors import SearchError


@dataclass
class SearchFilters:
    """Search filters for advanced YouTube search."""
    query: str
    channel: Optional[str] = None
    date_after: Optional[datetime] = None
    date_before: Optional[datetime] = None
    min_views: Optional[int] = None
    max_views: Optional[int] = None
    min_duration: Optional[int] = None
    max_duration: Optional[int] = None
    include_keywords: Optional[List[str]] = None
    exclude_keywords: Optional[List[str]] = None
    sort_by: str = "relevance"  # relevance, date, view_count, rating
    limit: int = 10
    language: Optional[str] = None
    region: Optional[str] = None


@dataclass
class SearchResult:
    """Search result data structure."""
    video_id: str
    title: str
    channel: str
    duration: int
    view_count: int
    upload_date: datetime
    description: str
    url: str
    thumbnail: str
    rating: Optional[float] = None
    tags: Optional[List[str]] = None


class AdvancedSearch:
    """Advanced YouTube search functionality."""
    
    def __init__(self):
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'default_search': 'ytsearch',
        }
    
    def search(self, filters: SearchFilters) -> List[SearchResult]:
        """
        Perform advanced YouTube search with filters.
        
        Args:
            filters: Search filters to apply
            
        Returns:
            List of search results
            
        Raises:
            SearchError: If search fails
        """
        try:
            # Build search query
            search_query = self._build_search_query(filters)
            
            # Configure yt-dlp options
            ydl_opts = self.ydl_opts.copy()
            ydl_opts['default_search'] = f'ytsearch{filters.limit}:{search_query}'
            
            # Add date filters if specified
            if filters.date_after or filters.date_before:
                ydl_opts['daterange'] = self._build_date_range(filters.date_after, filters.date_before)
            
            # Perform search
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                results = ydl.extract_info(search_query, download=False)
                
                if not results or 'entries' not in results:
                    return []
                
                # Process results
                search_results = []
                for entry in results['entries']:
                    if not entry:
                        continue
                    
                    result = self._process_search_entry(entry, filters)
                    if result and self._matches_filters(result, filters):
                        search_results.append(result)
                
                # Sort results
                search_results = self._sort_results(search_results, filters.sort_by)
                
                return search_results[:filters.limit]
                
        except Exception as e:
            raise SearchError(f"Search failed: {e}")
    
    def _build_search_query(self, filters: SearchFilters) -> str:
        """Build search query from filters."""
        query_parts = [filters.query]
        
        # Add channel filter
        if filters.channel:
            query_parts.append(f"channel:{filters.channel}")
        
        # Add duration filters
        if filters.min_duration:
            query_parts.append(f"after {filters.min_duration}s")
        if filters.max_duration:
            query_parts.append(f"before {filters.max_duration}s")
        
        # Add view count filters
        if filters.min_views:
            query_parts.append(f"view_count>={filters.min_views}")
        if filters.max_views:
            query_parts.append(f"view_count<={filters.max_views}")
        
        # Add include keywords
        if filters.include_keywords:
            for keyword in filters.include_keywords:
                query_parts.append(f'"{keyword}"')
        
        # Add exclude keywords
        if filters.exclude_keywords:
            for keyword in filters.exclude_keywords:
                query_parts.append(f'-"{keyword}"')
        
        return " ".join(query_parts)
    
    def _build_date_range(self, date_after: Optional[datetime], date_before: Optional[datetime]) -> str:
        """Build date range string for yt-dlp."""
        if date_after and date_before:
            return f"{date_after.strftime('%Y%m%d')}:{date_before.strftime('%Y%m%d')}"
        elif date_after:
            return f"{date_after.strftime('%Y%m%d')}:"
        elif date_before:
            return f":{date_before.strftime('%Y%m%d')}"
        else:
            return ""
    
    def _process_search_entry(self, entry: Dict[str, Any], filters: SearchFilters) -> Optional[SearchResult]:
        """Process a search result entry."""
        try:
            # Extract basic information
            video_id = entry.get('id', '')
            title = entry.get('title', '')
            channel = entry.get('uploader', '')
            duration = entry.get('duration', 0)
            view_count = entry.get('view_count', 0)
            description = entry.get('description', '')
            thumbnail = entry.get('thumbnail', '')
            
            # Parse upload date
            upload_date = None
            if 'upload_date' in entry:
                try:
                    upload_date = datetime.strptime(entry['upload_date'], '%Y%m%d')
                except ValueError:
                    pass
            
            # Build URL
            url = f"https://www.youtube.com/watch?v={video_id}"
            
            # Extract rating if available
            rating = None
            if 'average_rating' in entry:
                rating = entry['average_rating']
            
            # Extract tags if available
            tags = None
            if 'tags' in entry:
                tags = entry['tags']
            
            return SearchResult(
                video_id=video_id,
                title=title,
                channel=channel,
                duration=duration,
                view_count=view_count,
                upload_date=upload_date,
                description=description,
                url=url,
                thumbnail=thumbnail,
                rating=rating,
                tags=tags
            )
            
        except Exception as e:
            print(f"Error processing search entry: {e}")
            return None
    
    def _matches_filters(self, result: SearchResult, filters: SearchFilters) -> bool:
        """Check if a result matches the search filters."""
        # Duration filters
        if filters.min_duration and result.duration < filters.min_duration:
            return False
        if filters.max_duration and result.duration > filters.max_duration:
            return False
        
        # View count filters
        if filters.min_views and result.view_count < filters.min_views:
            return False
        if filters.max_views and result.view_count > filters.max_views:
            return False
        
        # Date filters
        if filters.date_after and result.upload_date and result.upload_date < filters.date_after:
            return False
        if filters.date_before and result.upload_date and result.upload_date > filters.date_before:
            return False
        
        # Channel filter
        if filters.channel and filters.channel.lower() not in result.channel.lower():
            return False
        
        # Include keywords
        if filters.include_keywords:
            text_to_search = f"{result.title} {result.description}".lower()
            for keyword in filters.include_keywords:
                if keyword.lower() not in text_to_search:
                    return False
        
        # Exclude keywords
        if filters.exclude_keywords:
            text_to_search = f"{result.title} {result.description}".lower()
            for keyword in filters.exclude_keywords:
                if keyword.lower() in text_to_search:
                    return False
        
        return True
    
    def _sort_results(self, results: List[SearchResult], sort_by: str) -> List[SearchResult]:
        """Sort search results."""
        if sort_by == "date":
            return sorted(results, key=lambda x: x.upload_date or datetime.min, reverse=True)
        elif sort_by == "view_count":
            return sorted(results, key=lambda x: x.view_count, reverse=True)
        elif sort_by == "rating":
            return sorted(results, key=lambda x: x.rating or 0, reverse=True)
        elif sort_by == "duration":
            return sorted(results, key=lambda x: x.duration)
        else:  # relevance (default)
            return results
    
    def search_by_channel(self, channel_name: str, limit: int = 10, 
                         date_after: Optional[datetime] = None) -> List[SearchResult]:
        """Search for videos by a specific channel."""
        filters = SearchFilters(
            query="",
            channel=channel_name,
            date_after=date_after,
            limit=limit,
            sort_by="date"
        )
        return self.search(filters)
    
    def search_trending(self, category: str = "music", limit: int = 10) -> List[SearchResult]:
        """Search for trending videos in a category."""
        filters = SearchFilters(
            query=f"trending {category}",
            limit=limit,
            sort_by="view_count"
        )
        return self.search(filters)
    
    def search_recent_uploads(self, channel_name: str, days: int = 7, 
                            limit: int = 10) -> List[SearchResult]:
        """Search for recent uploads from a channel."""
        date_after = datetime.now() - timedelta(days=days)
        return self.search_by_channel(channel_name, limit, date_after)
    
    def search_popular_music(self, genre: str = None, year: int = None, 
                           limit: int = 10) -> List[SearchResult]:
        """Search for popular music videos."""
        query_parts = ["music"]
        
        if genre:
            query_parts.append(genre)
        
        if year:
            query_parts.append(str(year))
        
        filters = SearchFilters(
            query=" ".join(query_parts),
            min_duration=120,  # At least 2 minutes
            max_duration=600,  # At most 10 minutes
            limit=limit,
            sort_by="view_count"
        )
        return self.search(filters)
    
    def search_playlists(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for playlists (not individual videos)."""
        try:
            ydl_opts = self.ydl_opts.copy()
            ydl_opts['default_search'] = f'ytsearch{limit}:{query} playlist'
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                results = ydl.extract_info(query, download=False)
                
                if not results or 'entries' not in results:
                    return []
                
                playlists = []
                for entry in results['entries']:
                    if entry and entry.get('_type') == 'playlist':
                        playlists.append({
                            'id': entry.get('id', ''),
                            'title': entry.get('title', ''),
                            'uploader': entry.get('uploader', ''),
                            'playlist_count': entry.get('playlist_count', 0),
                            'url': entry.get('webpage_url', ''),
                            'description': entry.get('description', '')
                        })
                
                return playlists
                
        except Exception as e:
            raise SearchError(f"Playlist search failed: {e}")
    
    def get_channel_info(self, channel_url: str) -> Optional[Dict[str, Any]]:
        """Get information about a YouTube channel."""
        try:
            ydl_opts = self.ydl_opts.copy()
            ydl_opts['extract_flat'] = False
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(channel_url, download=False)
                
                if not info:
                    return None
                
                return {
                    'id': info.get('id', ''),
                    'title': info.get('title', ''),
                    'description': info.get('description', ''),
                    'subscriber_count': info.get('subscriber_count', 0),
                    'video_count': info.get('playlist_count', 0),
                    'url': info.get('webpage_url', ''),
                    'thumbnail': info.get('thumbnail', '')
                }
                
        except Exception as e:
            print(f"Error getting channel info: {e}")
            return None


def format_search_results(results: List[SearchResult]) -> str:
    """Format search results for display."""
    if not results:
        return "No results found."
    
    output = []
    for i, result in enumerate(results, 1):
        output.append(f"{i}. {result.title}")
        output.append(f"   Channel: {result.channel}")
        output.append(f"   Duration: {result.duration // 60}:{result.duration % 60:02d}")
        output.append(f"   Views: {result.view_count:,}")
        if result.upload_date:
            output.append(f"   Uploaded: {result.upload_date.strftime('%Y-%m-%d')}")
        output.append(f"   URL: {result.url}")
        output.append("")
    
    return "\n".join(output)


def create_search_filters_interactive() -> SearchFilters:
    """Create search filters interactively."""
    import click
    
    query = click.prompt("Search query", type=str)
    channel = click.prompt("Channel name (optional)", type=str, default="")
    limit = click.prompt("Number of results", type=int, default=10, min=1, max=50)
    
    # Date filters
    use_date_filter = click.confirm("Use date filter?", default=False)
    date_after = None
    date_before = None
    
    if use_date_filter:
        date_after_str = click.prompt("Date after (YYYY-MM-DD, optional)", type=str, default="")
        if date_after_str:
            try:
                date_after = datetime.strptime(date_after_str, '%Y-%m-%d')
            except ValueError:
                click.echo("Invalid date format, ignoring date filter")
        
        date_before_str = click.prompt("Date before (YYYY-MM-DD, optional)", type=str, default="")
        if date_before_str:
            try:
                date_before = datetime.strptime(date_before_str, '%Y-%m-%d')
            except ValueError:
                click.echo("Invalid date format, ignoring date filter")
    
    # View count filters
    use_view_filter = click.confirm("Use view count filter?", default=False)
    min_views = None
    max_views = None
    
    if use_view_filter:
        min_views = click.prompt("Minimum views (optional)", type=int, default=0)
        max_views = click.prompt("Maximum views (optional)", type=int, default=0)
        if min_views == 0:
            min_views = None
        if max_views == 0:
            max_views = None
    
    # Duration filters
    use_duration_filter = click.confirm("Use duration filter?", default=False)
    min_duration = None
    max_duration = None
    
    if use_duration_filter:
        min_duration = click.prompt("Minimum duration (seconds, optional)", type=int, default=0)
        max_duration = click.prompt("Maximum duration (seconds, optional)", type=int, default=0)
        if min_duration == 0:
            min_duration = None
        if max_duration == 0:
            max_duration = None
    
    # Keyword filters
    use_keyword_filter = click.confirm("Use keyword filters?", default=False)
    include_keywords = None
    exclude_keywords = None
    
    if use_keyword_filter:
        include_str = click.prompt("Include keywords (comma-separated, optional)", type=str, default="")
        if include_str:
            include_keywords = [k.strip() for k in include_str.split(',')]
        
        exclude_str = click.prompt("Exclude keywords (comma-separated, optional)", type=str, default="")
        if exclude_str:
            exclude_keywords = [k.strip() for k in exclude_str.split(',')]
    
    # Sort options
    sort_options = ["relevance", "date", "view_count", "rating", "duration"]
    sort_by = click.prompt("Sort by", type=click.Choice(sort_options), default="relevance")
    
    return SearchFilters(
        query=query,
        channel=channel or None,
        date_after=date_after,
        date_before=date_before,
        min_views=min_views,
        max_views=max_views,
        min_duration=min_duration,
        max_duration=max_duration,
        include_keywords=include_keywords,
        exclude_keywords=exclude_keywords,
        sort_by=sort_by,
        limit=limit
    )
