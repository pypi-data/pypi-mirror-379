"""Core extraction logic for YouTube content."""

import os
import time
import logging
from typing import Optional, Dict, Any, Callable
from pathlib import Path

import yt_dlp

from .utils import VideoInfo, PlaylistInfo, ExtractionOptions, sanitize_filename, create_safe_directory_name
from .progress import ProgressTracker, PlaylistProgressTracker
from .errors import ErrorHandler, NetworkError, FileSystemError, URLValidationError


class YouTubeExtractor:
    """
    Handles YouTube content extraction using yt-dlp.
    
    This class provides a high-level interface for downloading audio from YouTube
    videos and playlists. It handles URL validation, progress tracking, error recovery,
    and file organization. The extractor uses yt-dlp for downloading and provides
    comprehensive error handling with user-friendly feedback.
    
    Attributes:
        options (ExtractionOptions): Configuration options for extraction
        progress_tracker (ProgressTracker): Optional progress tracker for user feedback
        logger (logging.Logger): Logger instance for this class
        error_handler (ErrorHandler): Error handler for consistent error management
        ydl_opts (dict): Configuration options for yt-dlp
        
    Example:
        >>> options = ExtractionOptions(quality="320", output_dir="downloads")
        >>> tracker = ProgressTracker(verbose=True)
        >>> extractor = YouTubeExtractor(options, tracker)
        >>> output_path = extractor.extract_video_audio("https://youtube.com/watch?v=...")
    """
    
    def __init__(self, options: ExtractionOptions, progress_tracker: Optional[ProgressTracker] = None):
        """
        Initialize the extractor with extraction options.
        
        Sets up the YouTube extractor with the specified configuration options and
        optional progress tracking. Configures yt-dlp with appropriate settings for
        audio extraction and quality selection.
        
        Args:
            options (ExtractionOptions): Configuration options including quality,
                                       output directory, and metadata preferences
            progress_tracker (ProgressTracker, optional): Progress tracker for user
                                                         feedback during downloads
                                                         
        Example:
            >>> options = ExtractionOptions(quality="192", output_dir="~/Music")
            >>> tracker = ProgressTracker(verbose=False)
            >>> extractor = YouTubeExtractor(options, tracker)
        """
        self.options = options
        self.logger = logging.getLogger(__name__)
        self.progress_tracker = progress_tracker
        self.error_handler = ErrorHandler()
        
        # Configure yt-dlp options
        preferred_codec = getattr(self.options, 'output_format', 'mp3') or 'mp3'
        # Prefer commonly available audio-only formats first, then fallback
        # This reduces chances of "Requested format is not available" on some videos
        preferred_audio_selector = 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best'
        self.ydl_opts = {
            'format': preferred_audio_selector,
            'outtmpl': os.path.join(self.options.output_dir, self.options.format_template),
            'noplaylist': True,  # Will be overridden for playlist extraction
            'quiet': True,
            'no_warnings': True,
            # Improve format availability and connectivity robustness
            'extractor_args': {
                'youtube': {
                    # Use android client to avoid some throttling/format gating
                    'player_client': ['android']
                }
            },
            'geo_bypass': True,
            'geo_bypass_country': 'US',
            'forceipv4': True,
            # Let yt-dlp raise on errors so we can handle retries properly
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': preferred_codec,
                'preferredquality': self.options.quality,
            }],
        }

        # Attach cookies file if provided
        if getattr(self.options, 'cookie_path', None):
            # yt-dlp expects key 'cookiefile'
            self.ydl_opts['cookiefile'] = self.options.cookie_path
        
        # Add progress hook if tracker is provided
        if self.progress_tracker:
            self.ydl_opts['progress_hooks'] = [self.progress_tracker.create_yt_dlp_hook()]
    
    def get_video_info(self, url: str) -> Optional[VideoInfo]:
        """
        Retrieve video information without downloading.
        
        Extracts metadata from a YouTube video URL without downloading the actual
        content. This is useful for getting video details, validating URLs, and
        preparing for download operations.
        
        Args:
            url (str): YouTube video URL to extract information from
            
        Returns:
            VideoInfo: Object containing video metadata (title, uploader, duration,
                      upload_date, url, id) if successful
            None: If extraction fails due to network issues, invalid URL, or
                  other errors
                  
        Example:
            >>> extractor = YouTubeExtractor(options)
            >>> info = extractor.get_video_info("https://youtube.com/watch?v=dQw4w9WgXcQ")
            >>> if info:
            ...     print(f"Title: {info.title}")
            ...     print(f"Duration: {info.duration} seconds")
        """
        try:
            base_info_opts = {
                'quiet': True,
                'no_warnings': True,
                'extractor_args': {'youtube': {'player_client': ['android']}},
                'geo_bypass': True,
                'geo_bypass_country': 'US',
                'forceipv4': True,
            }
            if getattr(self.options, 'cookie_path', None):
                base_info_opts['cookiefile'] = self.options.cookie_path
            with yt_dlp.YoutubeDL(base_info_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                return VideoInfo(
                    title=info.get('title', 'Unknown Title'),
                    uploader=info.get('uploader', 'Unknown Uploader'),
                    duration=info.get('duration', 0),
                    upload_date=info.get('upload_date', ''),
                    url=url,
                    id=info.get('id', '')
                )
                
        except Exception:
            # Fallback to flat extraction to get at least title/uploader without format selection
            try:
                flat_opts = {
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': True,
                    'skip_download': True,
                    'extractor_args': {'youtube': {'player_client': ['android']}},
                    'geo_bypass': True,
                    'geo_bypass_country': 'US',
                    'forceipv4': True,
                }
                if getattr(self.options, 'cookie_path', None):
                    flat_opts['cookiefile'] = self.options.cookie_path
                with yt_dlp.YoutubeDL(flat_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if info:
                        return VideoInfo(
                            title=info.get('title', 'Unknown Title'),
                            uploader=info.get('uploader', 'Unknown Uploader'),
                            duration=info.get('duration', 0),
                            upload_date=info.get('upload_date', ''),
                            url=url,
                            id=info.get('id', '')
                        )
            except Exception as e2:
                self.logger.error(f"Failed to extract video info for {url}: {e2}")
            return None
    
    def extract_video_audio(self, url: str, max_retries: int = 3) -> Optional[str]:
        """
        Extract audio from a single YouTube video with retry logic.
        
        Downloads and extracts audio from a YouTube video, converting it to the
        specified format and quality. Includes comprehensive error handling with
        automatic retry logic for network issues and detailed user feedback.
        
        Args:
            url (str): YouTube video URL to extract audio from
            max_retries (int, optional): Maximum number of retry attempts for
                                       failed downloads. Defaults to 3.
            
        Returns:
            str: Path to the extracted audio file if successful
            None: If extraction fails after all retry attempts or encounters
                  unrecoverable errors
                  
        Raises:
            The method handles exceptions internally and returns None on failure,
            but may log errors through the progress tracker.
            
        Example:
            >>> extractor = YouTubeExtractor(options, progress_tracker)
            >>> output_path = extractor.extract_video_audio(
            ...     "https://youtube.com/watch?v=dQw4w9WgXcQ", max_retries=5
            ... )
            >>> if output_path:
            ...     print(f"Audio saved to: {output_path}")
        """
        # Validate file system before starting
        try:
            self.error_handler.validate_file_system(self.options.output_dir, required_space_mb=50)
        except FileSystemError as e:
            self.logger.error(f"File system validation failed: {e}")
            if self.progress_tracker:
                self.progress_tracker.show_error_with_suggestions(str(e), e.suggestions)
            return None
        
        # Ensure output directory exists
        try:
            os.makedirs(self.options.output_dir, exist_ok=True)
        except (OSError, PermissionError) as e:
            fs_error = self.error_handler.handle_file_system_error(e, "creating output directory", self.options.output_dir)
            self.logger.error(str(fs_error))
            if self.progress_tracker:
                self.progress_tracker.show_error_with_suggestions(str(fs_error), fs_error.suggestions)
            return None
        
        # Show stage message
        if self.progress_tracker:
            self.progress_tracker.show_stage_message("Retrieving video information")
        
        # First, get video info (non-fatal if it fails due to format availability)
        info = None
        try:
            base_info_opts = {
                'quiet': True,
                'no_warnings': True,
                'extractor_args': {'youtube': {'player_client': ['android']}},
                'geo_bypass': True,
                'geo_bypass_country': 'US',
                'forceipv4': True,
            }
            if getattr(self.options, 'cookie_path', None):
                base_info_opts['cookiefile'] = self.options.cookie_path
            with yt_dlp.YoutubeDL(base_info_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                if not info:
                    self.logger.warning(f"Could not extract video information for {url}; will continue with download fallback")
        except Exception:
            # Try flat extraction to get title/uploader for pre-download display
            try:
                flat_opts = {
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': True,
                    'skip_download': True,
                    'extractor_args': {'youtube': {'player_client': ['android']}},
                    'geo_bypass': True,
                    'geo_bypass_country': 'US',
                    'forceipv4': True,
                }
                if getattr(self.options, 'cookie_path', None):
                    flat_opts['cookiefile'] = self.options.cookie_path
                with yt_dlp.YoutubeDL(flat_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    if not info:
                        self.logger.warning("Flat metadata extraction returned no info; will proceed to download")
            except Exception as e2:
                self.logger.warning(f"Video info retrieval failed; proceeding with fallback formats: {e2}")
        
        # Show video information when available
        if self.progress_tracker:
            if info:
                title = info.get('title', 'Unknown Title')
                uploader = info.get('uploader', 'Unknown Uploader')
                duration = info.get('duration')
                self.progress_tracker.show_video_info(title, uploader, duration)
            else:
                self.progress_tracker.show_video_info('Unknown Title', 'Unknown Uploader', None)
        
        # Determine output naming strategy
        output_ext = getattr(self.options, 'output_format', 'mp3') or 'mp3'
        # If user selected mp4, treat as video download: change selector and disable audio postprocessor
        if output_ext == 'mp4':
            # Prefer best mp4 video+audio; fallback to best
            self.ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            # Remove audio-extract postprocessor for mp4
            self.ydl_opts['postprocessors'] = []
        static_output_path: Optional[str] = None
        ydl_opts_copy = self.ydl_opts.copy()
        if info:
            title = info.get('title', 'Unknown Title')
            sanitized_title = sanitize_filename(title)
            output_filename = f"{sanitized_title}.{output_ext}"
            static_output_path = os.path.join(self.options.output_dir, output_filename)
            # ensure outtmpl matches final extension chosen by ffmpeg
            base_no_ext = os.path.splitext(static_output_path)[0]
            ydl_opts_copy['outtmpl'] = base_no_ext + '.%(ext)s'
        else:
            # Defer naming to yt-dlp using the actual video title
            ydl_opts_copy['outtmpl'] = os.path.join(self.options.output_dir, "%(title)s.%(ext)s")
        
        # Prepare an initial format selector based on probed formats (if available)
        probed_selector = None
        if info and isinstance(info, dict) and 'formats' in info:
            try:
                audio_formats = [f for f in info.get('formats', []) if (f.get('vcodec') in (None, 'none')) and f.get('acodec') not in (None, 'none')]
                # Prefer m4a/aac or opus by abr (audio bitrate) descending
                def fmt_sort_key(f):
                    ext = (f.get('ext') or '')
                    ext_rank = 0 if ext == 'm4a' else 1 if ext == 'webm' else 2
                    abr = f.get('abr') or 0
                    return (- (abr or 0), ext_rank)
                if audio_formats:
                    audio_formats.sort(key=fmt_sort_key)
                    best = audio_formats[0]
                    fid = best.get('format_id')
                    if fid:
                        probed_selector = fid
            except Exception:
                probed_selector = None

        # Show download stage
        if self.progress_tracker:
            self.progress_tracker.show_stage_message("Downloading and extracting audio")
        
        # Retry logic for download with progressively relaxed format selectors
        # Try audio-first, then plain best earlier to avoid format-not-available loops
        fallback_selectors = [
            probed_selector or ydl_opts_copy.get('format') or 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best',
            'bestaudio/best',
            'best',
            'bestaudio*/*',
            'bestvideo+bestaudio/best'
        ]
        for attempt in range(max_retries + 1):
            try:
                # Set selector for this attempt
                selector_idx = min(attempt, len(fallback_selectors) - 1)
                ydl_opts_copy['format'] = fallback_selectors[selector_idx]
                if self.progress_tracker and attempt > 0:
                    self.progress_tracker.show_stage_message(
                        "Adjusting format selector",
                        fallback_selectors[selector_idx]
                    )
                # Download and extract audio; get info back for accurate filenames
                with yt_dlp.YoutubeDL(ydl_opts_copy) as download_ydl:
                    result = download_ydl.extract_info(url, download=True)

                # Resolve final output file path(s)
                candidate_paths = []
                # Prefer paths reported by yt-dlp
                try:
                    if isinstance(result, dict):
                        # Newer yt-dlp exposes requested_downloads
                        reqs = result.get('requested_downloads') or []
                        for rd in reqs:
                            fp = rd.get('filepath') or rd.get('filename')
                            if fp:
                                candidate_paths.append(fp)
                        # Fallback: derive from prepared filename
                        if not candidate_paths:
                            with yt_dlp.YoutubeDL(ydl_opts_copy) as tmp_ydl:
                                prepared = tmp_ydl.prepare_filename(result)
                                if prepared:
                                    candidate_paths.append(prepared)
                except Exception:
                    pass

                # If we had a static output path planned, check that first
                if static_output_path:
                    if os.path.exists(static_output_path):
                        self.logger.info(f"Successfully extracted audio: {static_output_path}")
                        return static_output_path
                    # Add static base to candidate checks
                    base_path = os.path.splitext(static_output_path)[0]
                    for ext in ['.mp3', '.m4a', '.webm', '.opus', '.flac', '.mp4', '.mkv']:
                        candidate_paths.append(base_path + ext)

                # Check candidate paths and common audio extensions
                for path in candidate_paths:
                    if path and os.path.exists(path):
                        # If mp4 selected, return the mp4 path directly
                        if output_ext == 'mp4':
                            self.logger.info(f"Successfully downloaded video: {path}")
                            return path
                        # If this is not the desired audio extension, see if postprocessor created the audio file
                        base_no_ext = os.path.splitext(path)[0]
                        audio_candidate = base_no_ext + f'.{output_ext}'
                        if os.path.exists(audio_candidate):
                            self.logger.info(f"Successfully extracted audio: {audio_candidate}")
                            return audio_candidate
                        if path.endswith(('.mp3', '.m4a', '.opus', '.flac')):
                            self.logger.info(f"Successfully extracted audio: {path}")
                            return path

                # As a final attempt, scan output directory for a freshly created matching title file
                try:
                    files = sorted(
                        [os.path.join(self.options.output_dir, f) for f in os.listdir(self.options.output_dir)],
                        key=lambda p: os.path.getmtime(p), reverse=True
                    )
                    for p in files[:10]:
                        if os.path.isfile(p) and (p.endswith(('.mp3', '.m4a', '.opus', '.flac')) or (output_ext=='mp4' and p.endswith('.mp4'))):
                            self.logger.info(f"Successfully extracted audio: {p}")
                            return p
                except Exception:
                    pass
                    
                    # File not found - this is a file system issue
                    fs_error = FileSystemError(
                        "Audio file not found after extraction",
                        ["Check available disk space", "Verify write permissions", "Try a different output directory"]
                    )
                    self.logger.error(str(fs_error))
                    if self.progress_tracker:
                        self.progress_tracker.show_error_with_suggestions(str(fs_error), fs_error.suggestions)
                    return None
                    
            except yt_dlp.DownloadError as e:
                if attempt < max_retries:
                    wait_time = self.error_handler.get_retry_delay(attempt)
                    self.logger.warning(f"Download failed (attempt {attempt + 1}/{max_retries + 1}): {e}")
                    if self.progress_tracker:
                        self.progress_tracker.show_stage_message(f"Retrying in {wait_time:.1f} seconds", f"Attempt {attempt + 1}/{max_retries + 1}")
                    time.sleep(wait_time)
                else:
                    network_error = self.error_handler.handle_network_error(e, "video download", max_retries)
                    self.logger.error(str(network_error))
                    if self.progress_tracker:
                        self.progress_tracker.show_error_with_suggestions(str(network_error), network_error.suggestions)
                    return None
                    
            except (OSError, PermissionError) as e:
                # File system related errors
                fs_error = self.error_handler.handle_file_system_error(e, "downloading audio", output_path)
                self.logger.error(str(fs_error))
                if self.progress_tracker:
                    self.progress_tracker.show_error_with_suggestions(str(fs_error), fs_error.suggestions)
                return None
                    
            except Exception as e:
                if attempt < max_retries:
                    wait_time = self.error_handler.get_retry_delay(attempt)
                    self.logger.warning(f"Download failed (attempt {attempt + 1}/{max_retries + 1}): {e}")
                    if self.progress_tracker:
                        self.progress_tracker.show_stage_message(f"Retrying in {wait_time:.1f} seconds", f"Attempt {attempt + 1}/{max_retries + 1}")
                    time.sleep(wait_time)
                else:
                    # For unexpected errors, treat as network error with generic suggestions
                    network_error = self.error_handler.handle_network_error(e, "video download", max_retries)
                    self.logger.error(str(network_error))
                    if self.progress_tracker:
                        self.progress_tracker.show_error_with_suggestions(str(network_error), network_error.suggestions)
                    return None
        
        return None
    
    def is_playlist_url(self, url: str) -> bool:
        """
        Check if the provided URL is a YouTube playlist URL.
        
        Determines whether a given URL points to a YouTube playlist by attempting
        to extract information and checking for multiple entries. This helps the
        application decide whether to use single video or playlist processing logic.
        
        Args:
            url (str): URL to check for playlist characteristics
            
        Returns:
            bool: True if URL is a playlist containing multiple videos,
                  False if it's a single video or invalid URL
                  
        Example:
            >>> extractor = YouTubeExtractor(options)
            >>> is_playlist = extractor.is_playlist_url(
            ...     "https://youtube.com/playlist?list=PLrAXtmRdnEQy6nuLMt9xaJGA6H_VjlXEL"
            ... )
            >>> if is_playlist:
            ...     print("Processing as playlist")
            ... else:
            ...     print("Processing as single video")
        """
        try:
            # Check if this is a search URL (ytsearch format)
            if url.startswith('ytsearch'):
                return True
            
            base_info_opts = {'quiet': True, 'no_warnings': True}
            if getattr(self.options, 'cookie_path', None):
                base_info_opts['cookiefile'] = self.options.cookie_path
            with yt_dlp.YoutubeDL(base_info_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                # Check if this is a playlist by looking for entries
                return info and 'entries' in info and len(info.get('entries', [])) > 1
        except Exception:
            return False
    
    def get_playlist_info(self, url: str) -> Optional[PlaylistInfo]:
        """
        Retrieve playlist information without downloading.
        
        Extracts comprehensive metadata from a YouTube playlist URL without downloading
        any content. This includes playlist details and information about all contained
        videos, which is essential for planning the download process and providing
        user feedback.
        
        Args:
            url (str): YouTube playlist URL to extract information from
            
        Returns:
            PlaylistInfo: Object containing playlist metadata (title, uploader,
                         video_count) and a list of VideoInfo objects for each
                         video in the playlist
            None: If extraction fails due to network issues, invalid URL, private
                  playlist, or other errors
                  
        Example:
            >>> extractor = YouTubeExtractor(options)
            >>> playlist = extractor.get_playlist_info(
            ...     "https://youtube.com/playlist?list=PLrAXtmRdnEQy6nuLMt9xaJGA6H_VjlXEL"
            ... )
            >>> if playlist:
            ...     print(f"Playlist: {playlist.title}")
            ...     print(f"Videos: {playlist.video_count}")
            ...     for video in playlist.videos[:3]:  # Show first 3
            ...         print(f"  - {video.title}")
        """
        try:
            with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                
                if not info or 'entries' not in info:
                    self.logger.error(f"No playlist entries found for {url}")
                    return None
                
                # Show progress for large playlists
                entries = info.get('entries', [])
                total_entries = len(entries)
                
                if self.progress_tracker and total_entries > 10:
                    self.progress_tracker.show_stage_message(f"Processing {total_entries} videos in playlist")
                
                # Extract video information from playlist entries with progress
                videos = []
                for i, entry in enumerate(entries):
                    if entry:  # Skip None entries (unavailable videos)
                        video_info = VideoInfo(
                            title=entry.get('title', 'Unknown Title'),
                            uploader=entry.get('uploader', info.get('uploader', 'Unknown Uploader')),
                            duration=entry.get('duration', 0),
                            upload_date=entry.get('upload_date', ''),
                            url=entry.get('webpage_url', entry.get('url', '')),
                            id=entry.get('id', '')
                        )
                        videos.append(video_info)
                        
                        # Show progress for large playlists
                        if self.progress_tracker and total_entries > 20 and (i + 1) % 10 == 0:
                            self.progress_tracker.show_stage_message(f"Processed {i + 1}/{total_entries} videos")
                
                return PlaylistInfo(
                    title=info.get('title', 'Unknown Playlist'),
                    uploader=info.get('uploader', 'Unknown Uploader'),
                    video_count=len(videos),
                    videos=videos
                )
                
        except yt_dlp.DownloadError as e:
            self.logger.error(f"Failed to extract playlist info for {url}: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error extracting playlist info for {url}: {e}")
            return None
    
    def extract_playlist_audio(self, url: str, max_retries: int = 3, filtered_videos: Optional[list] = None) -> Dict[str, Any]:
        """
        Extract audio from all videos in a YouTube playlist with error recovery.
        
        Processes an entire YouTube playlist by downloading audio from each video
        sequentially. Creates organized folder structure, handles individual video
        failures gracefully, and provides comprehensive progress tracking and
        error reporting.
        
        Args:
            url (str): YouTube playlist URL to process
            max_retries (int, optional): Maximum number of retry attempts per video.
                                       Defaults to 3.
            
        Returns:
            Dict[str, Any]: Comprehensive results dictionary containing:
                - success (bool): Whether any videos were successfully downloaded
                - playlist_title (str): Name of the playlist
                - playlist_folder (str): Path to created playlist folder
                - total_videos (int): Total number of videos in playlist
                - successful_downloads (List[Dict]): List of successful downloads
                - failed_downloads (List[Dict]): List of failed downloads
                - success_count (int): Number of successful downloads
                - failure_count (int): Number of failed downloads
                - error (str): Error message if playlist processing failed entirely
                
        Example:
            >>> extractor = YouTubeExtractor(options, progress_tracker)
            >>> results = extractor.extract_playlist_audio(
            ...     "https://youtube.com/playlist?list=PLrAXtmRdnEQy6nuLMt9xaJGA6H_VjlXEL"
            ... )
            >>> if results['success']:
            ...     print(f"Downloaded {results['success_count']} of {results['total_videos']} videos")
            ...     print(f"Saved to: {results['playlist_folder']}")
        """
        # Show stage message
        if self.progress_tracker:
            self.progress_tracker.show_stage_message("Retrieving playlist information")
        
        # Get playlist information first
        playlist_info = self.get_playlist_info(url)
        if not playlist_info:
            error_msg = 'Failed to retrieve playlist information'
            if self.progress_tracker:
                self.progress_tracker.show_error_with_suggestions(
                    error_msg,
                    ["Check if the playlist URL is valid", "Verify the playlist is public", "Check internet connection"]
                )
            return {
                'success': False,
                'error': error_msg,
                'successful_downloads': [],
                'failed_downloads': [],
                'playlist_folder': None
            }
        
        # Show playlist information
        if self.progress_tracker:
            self.progress_tracker.show_playlist_info(playlist_info.title, playlist_info.uploader, playlist_info.video_count)
            
            # Ask for confirmation for large playlists
            if not self.progress_tracker.confirm_large_playlist(playlist_info.video_count):
                return {
                    'success': False,
                    'error': 'Operation cancelled by user',
                    'successful_downloads': [],
                    'failed_downloads': [],
                    'playlist_folder': None
                }
        
        # Create playlist folder
        playlist_folder_name = create_safe_directory_name(playlist_info.title)
        playlist_folder_path = os.path.join(self.options.output_dir, playlist_folder_name)
        
        try:
            os.makedirs(playlist_folder_path, exist_ok=True)
        except (OSError, PermissionError) as e:
            fs_error = self.error_handler.handle_file_system_error(e, "creating playlist folder", playlist_folder_path)
            self.logger.error(str(fs_error))
            return {
                'success': False,
                'error': str(fs_error),
                'successful_downloads': [],
                'failed_downloads': [],
                'playlist_folder': None
            }
        
        if self.progress_tracker:
            self.progress_tracker.show_stage_message("Creating playlist folder", playlist_folder_path)
        
        self.logger.info(f"Processing playlist: {playlist_info.title}")
        self.logger.info(f"Found {playlist_info.video_count} videos")
        self.logger.info(f"Saving to folder: {playlist_folder_path}")
        
        # Track results
        successful_downloads = []
        failed_downloads = []
        
        # Create playlist progress tracker
        playlist_progress = PlaylistProgressTracker(
            playlist_info.video_count, 
            verbose=self.progress_tracker.verbose if self.progress_tracker else False
        )
        
        # Create a temporary extractor with playlist folder as output directory
        playlist_options = ExtractionOptions(
            quality=self.options.quality,
            output_dir=playlist_folder_path,
            format_template=self.options.format_template,
            embed_metadata=self.options.embed_metadata,
            output_format=getattr(self.options, 'output_format', 'mp3')
        )
        # Don't pass progress tracker to avoid duplicate progress displays
        playlist_extractor = YouTubeExtractor(playlist_options)
        
        # Choose videos (filtered if provided)
        videos_to_process = filtered_videos if filtered_videos is not None else playlist_info.videos

        # Process each video sequentially
        for i, video in enumerate(videos_to_process, 1):
            playlist_progress.start_video(i, video.title)
            self.logger.info(f"Processing video {i}/{playlist_info.video_count}: {video.title}")
            
            try:
                # Extract audio for this video
                output_path = playlist_extractor.extract_video_audio(video.url, max_retries)
                
                if output_path:
                    successful_downloads.append({
                        'title': video.title,
                        'url': video.url,
                        'output_path': output_path
                    })
                    playlist_progress.video_success(video.title, output_path)
                    self.logger.info(f"Successfully downloaded: {video.title}")
                else:
                    error_msg = 'Download failed after retries'
                    failed_downloads.append({
                        'title': video.title,
                        'url': video.url,
                        'error': error_msg
                    })
                    playlist_progress.video_failed(video.title, error_msg)
                    self.logger.error(f"Failed to download: {video.title}")
                    
            except Exception as e:
                error_msg = str(e)
                failed_downloads.append({
                    'title': video.title,
                    'url': video.url,
                    'error': error_msg
                })
                playlist_progress.video_failed(video.title, error_msg)
                self.logger.error(f"Error processing {video.title}: {e}")
                # Continue with next video instead of stopping
                continue
        
        # Return comprehensive results
        return {
            'success': len(successful_downloads) > 0,
            'playlist_title': playlist_info.title,
            'playlist_folder': playlist_folder_path,
            'total_videos': playlist_info.video_count,
            'successful_downloads': successful_downloads,
            'failed_downloads': failed_downloads,
            'success_count': len(successful_downloads),
            'failure_count': len(failed_downloads)
        }

    async def extract_playlist_audio_concurrent(self, url: str, concurrency: int = 3, max_retries: int = 3) -> Dict[str, Any]:
        """Concurrent playlist processing using asyncio with bounded concurrency."""
        import asyncio

        if self.progress_tracker:
            self.progress_tracker.show_stage_message("Retrieving playlist information")
        playlist_info = self.get_playlist_info(url)
        if not playlist_info:
            error_msg = 'Failed to retrieve playlist information'
            if self.progress_tracker:
                self.progress_tracker.show_error_with_suggestions(
                    error_msg,
                    ["Check if the playlist URL is valid", "Verify the playlist is public", "Check internet connection"]
                )
            return {
                'success': False,
                'error': error_msg,
                'successful_downloads': [],
                'failed_downloads': [],
                'playlist_folder': None
            }

        # Prepare folder
        playlist_folder_name = create_safe_directory_name(playlist_info.title)
        playlist_folder_path = os.path.join(self.options.output_dir, playlist_folder_name)
        try:
            os.makedirs(playlist_folder_path, exist_ok=True)
        except (OSError, PermissionError) as e:
            fs_error = self.error_handler.handle_file_system_error(e, "creating playlist folder", playlist_folder_path)
            self.logger.error(str(fs_error))
            return {
                'success': False,
                'error': str(fs_error),
                'successful_downloads': [],
                'failed_downloads': [],
                'playlist_folder': None
            }

        # Child extractor without tracker (to reduce duplicated hooks output)
        playlist_options = ExtractionOptions(
            quality=self.options.quality,
            output_dir=playlist_folder_path,
            format_template=self.options.format_template,
            embed_metadata=self.options.embed_metadata,
            output_format=getattr(self.options, 'output_format', 'mp3')
        )
        child = YouTubeExtractor(playlist_options)

        sem = asyncio.Semaphore(max(1, min(concurrency, 10)))
        successful_downloads = []
        failed_downloads = []

        async def worker(video):
            async with sem:
                out = await asyncio.to_thread(child.extract_video_audio, video.url, max_retries)
                if out:
                    successful_downloads.append({'title': video.title, 'url': video.url, 'output_path': out})
                else:
                    failed_downloads.append({'title': video.title, 'url': video.url, 'error': 'Download failed'})

        await asyncio.gather(*(worker(v) for v in playlist_info.videos))

        return {
            'success': len(successful_downloads) > 0,
            'playlist_title': playlist_info.title,
            'playlist_folder': playlist_folder_path,
            'total_videos': playlist_info.video_count,
            'successful_downloads': successful_downloads,
            'failed_downloads': failed_downloads,
            'success_count': len(successful_downloads),
            'failure_count': len(failed_downloads)
        }
    
    def validate_url(self, url: str) -> bool:
        """
        Validate if the provided URL is a valid YouTube URL.
        
        Checks whether a given URL is a valid YouTube video or playlist URL that
        can be processed by the extractor. Uses the error handler's validation
        logic to ensure consistency across the application.
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if URL is a valid YouTube URL that can be processed,
                  False if URL is invalid, malformed, or not accessible
                  
        Example:
            >>> extractor = YouTubeExtractor(options)
            >>> valid = extractor.validate_url("https://youtube.com/watch?v=dQw4w9WgXcQ")
            >>> if valid:
            ...     print("URL is valid and can be processed")
            ... else:
            ...     print("Invalid YouTube URL")
        """
        try:
            self.error_handler.validate_url(url)
            return True
        except (URLValidationError, NetworkError):
            return False
    
    def validate_url_lazy(self, url: str) -> bool:
        """
        Fast URL validation without full content checking.
        
        Performs basic URL format validation without fetching all playlist content.
        Much faster for large playlists but less thorough than full validation.
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if URL format is valid, False otherwise
        """
        if not url or not isinstance(url, str):
            return False
        
        # Allow yt-dlp search shortcuts like ytsearch: or ytsearchN:
        if url.startswith(('ytsearch:', 'ytsearch')):
            return True
        if not url.startswith(('http://', 'https://')):
            return False
        
        if 'youtube.com' not in url and 'youtu.be' not in url:
            return False
            
        return True