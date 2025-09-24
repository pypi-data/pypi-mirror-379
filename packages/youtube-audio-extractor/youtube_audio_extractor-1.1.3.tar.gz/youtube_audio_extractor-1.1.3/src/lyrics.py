"""Lyrics fetching and management functionality."""

import re
import requests
import logging
from typing import Optional, Dict, Any
from pathlib import Path


class LyricsFetcher:
    """
    Handles fetching lyrics from external APIs and saving them to files.
    
    Provides functionality to fetch lyrics from various sources and save them
    as text files alongside audio files. Supports multiple lyrics APIs with
    fallback options.
    """
    
    def __init__(self):
        """Initialize the lyrics fetcher with default settings."""
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'YouTube-Audio-Extractor/1.0'
        })
    
    def extract_artist_title(self, filename: str) -> Dict[str, str]:
        """
        Extract artist and title from filename.
        
        Attempts to parse common filename patterns to extract artist and title
        information for lyrics lookup.
        
        Args:
            filename (str): The filename to parse (with or without extension)
            
        Returns:
            Dict[str, str]: Dictionary with 'artist' and 'title' keys
            
        Example:
            >>> fetcher = LyricsFetcher()
            >>> result = fetcher.extract_artist_title("Artist - Song Title.mp3")
            >>> print(result)  # {'artist': 'Artist', 'title': 'Song Title'}
        """
        # Remove file extension
        clean_name = Path(filename).stem
        
        # Common patterns: "Artist - Title", "Artist - Title (Official Video)", etc.
        patterns = [
            r'^(.+?)\s*-\s*(.+?)(?:\s*\([^)]*\))?$',  # Artist - Title (stuff)
            r'^(.+?)\s*–\s*(.+?)(?:\s*\([^)]*\))?$',  # Artist – Title (en dash)
            r'^(.+?)\s*—\s*(.+?)(?:\s*\([^)]*\))?$',  # Artist — Title (em dash)
        ]
        
        for pattern in patterns:
            match = re.match(pattern, clean_name, re.IGNORECASE)
            if match:
                artist = match.group(1).strip()
                title = match.group(2).strip()
                
                # Clean up common suffixes
                title = re.sub(r'\s*\([^)]*\)\s*$', '', title).strip()
                title = re.sub(r'\s*\[[^\]]*\]\s*$', '', title).strip()
                
                return {
                    'artist': self._clean_text(artist),
                    'title': self._clean_text(title)
                }
        
        # Fallback: use filename as title
        return {
            'artist': 'Unknown Artist',
            'title': self._clean_text(clean_name)
        }
    
    def _clean_text(self, text: str) -> str:
        """
        Clean text for API requests.
        
        Removes problematic characters and normalizes text for better
        API matching.
        
        Args:
            text (str): Text to clean
            
        Returns:
            str: Cleaned text
        """
        if not text:
            return ""
        
        # Remove or replace problematic characters
        cleaned = re.sub(r'[^\w\s\-\.]', '', text)
        # Normalize whitespace
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        
        return cleaned
    
    def fetch_lyrics_ovh(self, artist: str, title: str) -> Optional[str]:
        """
        Fetch lyrics from Lyrics.ovh API.
        
        Attempts to fetch lyrics from the free Lyrics.ovh API service.
        
        Args:
            artist (str): Artist name
            title (str): Song title
            
        Returns:
            Optional[str]: Lyrics text if found, None otherwise
            
        Example:
            >>> fetcher = LyricsFetcher()
            >>> lyrics = fetcher.fetch_lyrics_ovh("Rick Astley", "Never Gonna Give You Up")
            >>> if lyrics:
            ...     print("Found lyrics!")
        """
        try:
            # Clean and encode for URL
            clean_artist = self._clean_text(artist)
            clean_title = self._clean_text(title)
            
            if not clean_artist or not clean_title:
                return None
            
            url = f"https://api.lyrics.ovh/v1/{clean_artist}/{clean_title}"
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            lyrics = data.get('lyrics')
            
            if lyrics and lyrics.strip():
                return lyrics.strip()
            
        except requests.exceptions.RequestException as e:
            self.logger.debug(f"Lyrics.ovh API error: {e}")
        except (KeyError, ValueError) as e:
            self.logger.debug(f"Lyrics.ovh response parsing error: {e}")
        
        return None
    
    def fetch_lyrics(self, artist: str, title: str) -> Optional[str]:
        """
        Fetch lyrics using available APIs with fallback.
        
        Tries multiple lyrics sources in order of preference.
        
        Args:
            artist (str): Artist name
            title (str): Song title
            
        Returns:
            Optional[str]: Lyrics text if found, None otherwise
        """
        # Try Lyrics.ovh first (free, no auth required)
        lyrics = self.fetch_lyrics_ovh(artist, title)
        if lyrics:
            return lyrics
        
        # Could add more APIs here in the future
        # lyrics = self.fetch_lyrics_genius(artist, title)
        # if lyrics:
        #     return lyrics
        
        return None
    
    def save_lyrics_file(self, lyrics: str, audio_file_path: str, 
                        format: str = 'txt') -> Optional[str]:
        """
        Save lyrics to a file alongside the audio file.
        
        Creates a lyrics file with the same name as the audio file but with
        a .txt extension (or specified format).
        
        Args:
            lyrics (str): The lyrics text to save
            audio_file_path (str): Path to the audio file
            format (str): File format extension (default: 'txt')
            
        Returns:
            Optional[str]: Path to the saved lyrics file, None if failed
            
        Example:
            >>> fetcher = LyricsFetcher()
            >>> lyrics_path = fetcher.save_lyrics_file(
            ...     "Never gonna give you up...", 
            ...     "/path/to/song.mp3"
            ... )
            >>> print(lyrics_path)  # "/path/to/song.txt"
        """
        try:
            audio_path = Path(audio_file_path)
            lyrics_path = audio_path.with_suffix(f'.{format}')
            
            with open(lyrics_path, 'w', encoding='utf-8') as f:
                f.write(lyrics)
            
            self.logger.info(f"Lyrics saved to: {lyrics_path}")
            return str(lyrics_path)
            
        except (OSError, IOError) as e:
            self.logger.error(f"Failed to save lyrics file: {e}")
            return None
    
    def get_lyrics_for_file(self, audio_file_path: str, 
                           save_file: bool = True) -> Optional[str]:
        """
        Get lyrics for an audio file and optionally save them.
        
        Extracts artist/title from filename, fetches lyrics, and optionally
        saves them to a file.
        
        Args:
            audio_file_path (str): Path to the audio file
            save_file (bool): Whether to save lyrics to a file
            
        Returns:
            Optional[str]: Lyrics text if found, None otherwise
            
        Example:
            >>> fetcher = LyricsFetcher()
            >>> lyrics = fetcher.get_lyrics_for_file("/path/to/Artist - Song.mp3")
            >>> if lyrics:
            ...     print("Found and saved lyrics!")
        """
        filename = Path(audio_file_path).name
        track_info = self.extract_artist_title(filename)
        
        if track_info['artist'] == 'Unknown Artist':
            self.logger.warning(f"Could not extract artist from filename: {filename}")
            return None
        
        self.logger.info(f"Looking for lyrics: {track_info['artist']} - {track_info['title']}")
        
        lyrics = self.fetch_lyrics(track_info['artist'], track_info['title'])
        
        if lyrics:
            if save_file:
                self.save_lyrics_file(lyrics, audio_file_path)
            return lyrics
        else:
            self.logger.info(f"No lyrics found for: {track_info['artist']} - {track_info['title']}")
            return None
