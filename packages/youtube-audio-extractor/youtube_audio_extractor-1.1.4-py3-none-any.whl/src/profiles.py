"""Configuration profiles management for YouTube Audio Extractor."""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
import click

from .config import AppConfig


@dataclass
class Profile:
    """Configuration profile data structure."""
    name: str
    description: str
    quality: str = "320"
    output_format: str = "mp3"
    output_dir: str = "downloads"
    playlist_folder: bool = True
    metadata: bool = True
    lyrics: bool = False
    resume: bool = False
    verbose: bool = False
    min_duration: Optional[int] = None
    max_duration: Optional[int] = None
    include_keywords: Optional[str] = None
    exclude_keywords: Optional[str] = None
    search_limit: int = 10
    cookie_path: Optional[str] = None
    custom_args: List[str] = None
    
    def __post_init__(self):
        if self.custom_args is None:
            self.custom_args = []


class ProfileManager:
    """Manages configuration profiles."""
    
    def __init__(self, config: AppConfig):
        self.config = config
        self.profiles_dir = Path(config.config_dir) / "profiles"
        self.profiles_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_file = self.profiles_dir / "profiles.json"
        self._profiles: Dict[str, Profile] = {}
        self._load_profiles()
    
    def _load_profiles(self) -> None:
        """Load profiles from disk."""
        if self.profiles_file.exists():
            try:
                with open(self.profiles_file, 'r') as f:
                    data = json.load(f)
                    for name, profile_data in data.items():
                        self._profiles[name] = Profile(**profile_data)
            except (json.JSONDecodeError, TypeError) as e:
                click.echo(f"Warning: Could not load profiles: {e}")
                self._profiles = {}
        else:
            self._create_default_profiles()
    
    def _save_profiles(self) -> None:
        """Save profiles to disk."""
        try:
            data = {name: asdict(profile) for name, profile in self._profiles.items()}
            with open(self.profiles_file, 'w') as f:
                json.dump(data, f, indent=2)
        except OSError as e:
            click.echo(f"Error saving profiles: {e}")
    
    def _create_default_profiles(self) -> None:
        """Create default profiles."""
        default_profiles = [
            Profile(
                name="high_quality",
                description="High quality downloads (320kbps MP3)",
                quality="320",
                output_format="mp3",
                output_dir="downloads/high_quality"
            ),
            Profile(
                name="mobile",
                description="Mobile-optimized downloads (128kbps MP3)",
                quality="128",
                output_format="mp3",
                output_dir="downloads/mobile"
            ),
            Profile(
                name="lossless",
                description="Lossless downloads (FLAC format)",
                quality="320",
                output_format="flac",
                output_dir="downloads/lossless"
            ),
            Profile(
                name="with_lyrics",
                description="Downloads with lyrics included",
                quality="192",
                output_format="mp3",
                output_dir="downloads/with_lyrics",
                lyrics=True
            ),
            Profile(
                name="playlist_music",
                description="Music playlists with filters",
                quality="192",
                output_format="mp3",
                output_dir="downloads/music",
                min_duration=120,
                max_duration=600,
                exclude_keywords="live,cover,remix"
            ),
            Profile(
                name="podcasts",
                description="Podcast downloads (longer duration)",
                quality="128",
                output_format="mp3",
                output_dir="downloads/podcasts",
                min_duration=300,
                include_keywords="podcast,episode"
            )
        ]
        
        for profile in default_profiles:
            self._profiles[profile.name] = profile
        
        self._save_profiles()
    
    def list_profiles(self) -> List[Profile]:
        """List all available profiles."""
        return list(self._profiles.values())
    
    def get_profile(self, name: str) -> Optional[Profile]:
        """Get a profile by name."""
        return self._profiles.get(name)
    
    def create_profile(self, profile: Profile) -> bool:
        """Create a new profile."""
        if profile.name in self._profiles:
            return False  # Profile already exists
        
        self._profiles[profile.name] = profile
        self._save_profiles()
        return True
    
    def update_profile(self, profile: Profile) -> bool:
        """Update an existing profile."""
        if profile.name not in self._profiles:
            return False  # Profile doesn't exist
        
        self._profiles[profile.name] = profile
        self._save_profiles()
        return True
    
    def delete_profile(self, name: str) -> bool:
        """Delete a profile."""
        if name not in self._profiles:
            return False  # Profile doesn't exist
        
        del self._profiles[name]
        self._save_profiles()
        return True
    
    def duplicate_profile(self, source_name: str, new_name: str, new_description: str = None) -> bool:
        """Duplicate an existing profile."""
        source_profile = self.get_profile(source_name)
        if not source_profile:
            return False  # Source profile doesn't exist
        
        if new_name in self._profiles:
            return False  # Target profile already exists
        
        # Create new profile with same settings
        new_profile = Profile(
            name=new_name,
            description=new_description or f"Copy of {source_name}",
            quality=source_profile.quality,
            output_format=source_profile.output_format,
            output_dir=source_profile.output_dir,
            playlist_folder=source_profile.playlist_folder,
            metadata=source_profile.metadata,
            lyrics=source_profile.lyrics,
            resume=source_profile.resume,
            verbose=source_profile.verbose,
            min_duration=source_profile.min_duration,
            max_duration=source_profile.max_duration,
            include_keywords=source_profile.include_keywords,
            exclude_keywords=source_profile.exclude_keywords,
            search_limit=source_profile.search_limit,
            cookie_path=source_profile.cookie_path,
            custom_args=source_profile.custom_args.copy()
        )
        
        self._profiles[new_name] = new_profile
        self._save_profiles()
        return True
    
    def export_profile(self, name: str, file_path: str) -> bool:
        """Export a profile to a file."""
        profile = self.get_profile(name)
        if not profile:
            return False
        
        try:
            with open(file_path, 'w') as f:
                json.dump(asdict(profile), f, indent=2)
            return True
        except OSError:
            return False
    
    def import_profile(self, file_path: str) -> bool:
        """Import a profile from a file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            profile = Profile(**data)
            return self.create_profile(profile)
        except (OSError, json.JSONDecodeError, TypeError):
            return False
    
    def apply_profile(self, profile: Profile, url: str, additional_args: List[str] = None) -> List[str]:
        """Apply a profile to generate command line arguments."""
        args = [url]
        
        # Basic options
        args.extend(["--quality", profile.quality])
        args.extend(["--format", profile.output_format])
        args.extend(["--output", profile.output_dir])
        
        # Boolean options
        if not profile.playlist_folder:
            args.append("--no-playlist-folder")
        
        if not profile.metadata:
            args.append("--no-metadata")
        
        if profile.lyrics:
            args.append("--lyrics")
        
        if profile.resume:
            args.append("--resume")
        
        if profile.verbose:
            args.append("--verbose")
        
        # Duration filters
        if profile.min_duration is not None:
            args.extend(["--min-duration", str(profile.min_duration)])
        
        if profile.max_duration is not None:
            args.extend(["--max-duration", str(profile.max_duration)])
        
        # Keyword filters
        if profile.include_keywords:
            args.extend(["--include", profile.include_keywords])
        
        if profile.exclude_keywords:
            args.extend(["--exclude", profile.exclude_keywords])
        
        # Search limit
        if profile.search_limit != 10:
            args.extend(["--search-limit", str(profile.search_limit)])
        
        # Cookie path
        if profile.cookie_path:
            args.extend(["--cookie-path", profile.cookie_path])
        
        # Custom arguments
        if profile.custom_args:
            args.extend(profile.custom_args)
        
        # Additional arguments
        if additional_args:
            args.extend(additional_args)
        
        return args
    
    def get_profile_summary(self, profile: Profile) -> str:
        """Get a summary of profile settings."""
        summary = f"Profile: {profile.name}\n"
        summary += f"Description: {profile.description}\n"
        summary += f"Quality: {profile.quality}kbps\n"
        summary += f"Format: {profile.output_format}\n"
        summary += f"Output: {profile.output_dir}\n"
        
        if profile.lyrics:
            summary += "Lyrics: Yes\n"
        
        if profile.min_duration or profile.max_duration:
            summary += f"Duration: {profile.min_duration or 0}-{profile.max_duration or '∞'}s\n"
        
        if profile.include_keywords:
            summary += f"Include: {profile.include_keywords}\n"
        
        if profile.exclude_keywords:
            summary += f"Exclude: {profile.exclude_keywords}\n"
        
        return summary


def create_profile_interactive(manager: ProfileManager) -> Optional[Profile]:
    """Create a profile interactively."""
    click.echo("Creating a new profile...")
    
    name = click.prompt("Profile name", type=str)
    if manager.get_profile(name):
        click.echo(f"Profile '{name}' already exists!")
        return None
    
    description = click.prompt("Description", type=str)
    quality = click.prompt("Quality (128/192/320)", type=click.Choice(["128", "192", "320"]), default="320")
    output_format = click.prompt("Format (mp3/m4a/opus/flac)", type=click.Choice(["mp3", "m4a", "opus", "flac"]), default="mp3")
    output_dir = click.prompt("Output directory", type=str, default="downloads")
    
    # Advanced options
    playlist_folder = click.confirm("Create playlist folders?", default=True)
    metadata = click.confirm("Embed metadata?", default=True)
    lyrics = click.confirm("Download lyrics?", default=False)
    resume = click.confirm("Resume mode?", default=False)
    verbose = click.confirm("Verbose output?", default=False)
    
    # Filters
    use_filters = click.confirm("Use duration filters?", default=False)
    min_duration = None
    max_duration = None
    
    if use_filters:
        min_duration = click.prompt("Minimum duration (seconds)", type=int, default=0)
        max_duration = click.prompt("Maximum duration (seconds)", type=int, default=3600)
    
    use_keywords = click.confirm("Use keyword filters?", default=False)
    include_keywords = None
    exclude_keywords = None
    
    if use_keywords:
        include_keywords = click.prompt("Include keywords (comma-separated)", type=str, default="")
        exclude_keywords = click.prompt("Exclude keywords (comma-separated)", type=str, default="")
    
    profile = Profile(
        name=name,
        description=description,
        quality=quality,
        output_format=output_format,
        output_dir=output_dir,
        playlist_folder=playlist_folder,
        metadata=metadata,
        lyrics=lyrics,
        resume=resume,
        verbose=verbose,
        min_duration=min_duration,
        max_duration=max_duration,
        include_keywords=include_keywords,
        exclude_keywords=exclude_keywords
    )
    
    return profile


def list_profiles_command(manager: ProfileManager) -> None:
    """List all profiles."""
    profiles = manager.list_profiles()
    
    if not profiles:
        click.echo("No profiles found.")
        return
    
    click.echo(f"\nAvailable profiles ({len(profiles)}):")
    click.echo("=" * 50)
    
    for profile in profiles:
        click.echo(f"\n{profile.name}")
        click.echo(f"  Description: {profile.description}")
        click.echo(f"  Quality: {profile.quality}kbps, Format: {profile.output_format}")
        click.echo(f"  Output: {profile.output_dir}")
        
        if profile.lyrics:
            click.echo("  Features: Lyrics")
        
        if profile.min_duration or profile.max_duration:
            click.echo(f"  Duration: {profile.min_duration or 0}-{profile.max_duration or '∞'}s")
        
        if profile.include_keywords or profile.exclude_keywords:
            click.echo(f"  Filters: {profile.include_keywords or 'none'} / {profile.exclude_keywords or 'none'}")


def show_profile_command(manager: ProfileManager, name: str) -> None:
    """Show detailed profile information."""
    profile = manager.get_profile(name)
    
    if not profile:
        click.echo(f"Profile '{name}' not found.")
        return
    
    click.echo(manager.get_profile_summary(profile))
