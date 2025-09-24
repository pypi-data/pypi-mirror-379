"""Interactive CLI wizard for complex operations."""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import click
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint

from .config import AppConfig
import subprocess


class InteractiveWizard:
    """Interactive CLI wizard for complex operations."""
    
    def __init__(self, config: AppConfig):
        self.config = config
        self.console = Console()
    
    def start(self) -> None:
        """Start the interactive wizard."""
        self.console.print(Panel.fit(
            "[bold blue]YouTube Audio Extractor - Interactive Wizard[/bold blue]\n"
            "Welcome to the interactive mode! This wizard will guide you through complex operations.",
            title="🎵 Interactive Mode"
        ))
        
        while True:
            choice = self._show_main_menu()
            
            if choice == "1":
                self._download_wizard()
            elif choice == "2":
                self._batch_wizard()
            elif choice == "3":
                self._playlist_wizard()
            elif choice == "4":
                self._search_wizard()
            elif choice == "5":
                self._config_wizard()
            elif choice == "6":
                self._analytics_wizard()
            elif choice == "7":
                self._help_wizard()
            elif choice == "0":
                self.console.print("\n👋 Goodbye!")
                break
            else:
                self.console.print("[red]Invalid choice. Please try again.[/red]")
    
    def _show_main_menu(self) -> str:
        """Show the main menu and get user choice."""
        self.console.print("\n" + "="*50)
        self.console.print("[bold]Main Menu[/bold]")
        self.console.print("="*50)
        
        menu_items = [
            "1. 📥 Download Wizard - Single video or playlist",
            "2. 📦 Batch Wizard - Multiple URLs from file",
            "3. 🎵 Playlist Wizard - Advanced playlist operations",
            "4. 🔍 Search Wizard - YouTube search and download",
            "5. ⚙️  Configuration Wizard - Manage settings",
            "6. 📊 Analytics Wizard - View statistics and reports",
            "7. ❓ Help Wizard - Learn about features",
            "0. 🚪 Exit"
        ]
        
        for item in menu_items:
            self.console.print(item)
        
        return Prompt.ask("\nSelect an option", choices=["0", "1", "2", "3", "4", "5", "6", "7"])
    
    def _download_wizard(self) -> None:
        """Interactive download wizard."""
        self.console.print(Panel.fit(
            "[bold]Download Wizard[/bold]\n"
            "This wizard will help you download audio from YouTube videos or playlists.",
            title="📥 Download"
        ))
        
        # Get URL
        url = Prompt.ask("Enter YouTube URL or search query")
        
        # Determine if it's a search
        is_search = not url.startswith(("http://", "https://"))
        
        # Get basic options
        quality = self._get_quality_choice()
        output_format = self._get_format_choice()
        output_dir = Prompt.ask("Output directory", default="downloads")
        
        # Advanced options
        self.console.print("\n[bold]Advanced Options[/bold]")
        include_lyrics = Confirm.ask("Download lyrics?", default=False)
        embed_metadata = Confirm.ask("Embed metadata?", default=True)
        create_playlist_folder = Confirm.ask("Create playlist folders?", default=True)
        
        # Duration filters
        use_filters = Confirm.ask("Use duration filters?", default=False)
        min_duration = None
        max_duration = None
        
        if use_filters:
            min_duration = IntPrompt.ask("Minimum duration (seconds)", default=0)
            max_duration = IntPrompt.ask("Maximum duration (seconds)", default=3600)
        
        # Keyword filters
        use_keywords = Confirm.ask("Use keyword filters?", default=False)
        include_keywords = None
        exclude_keywords = None
        
        if use_keywords:
            include_keywords = Prompt.ask("Include keywords (comma-separated)", default="")
            exclude_keywords = Prompt.ask("Exclude keywords (comma-separated)", default="")
        
        # Build command
        args = self._build_download_args(
            url, quality, output_format, output_dir, is_search,
            include_lyrics, embed_metadata, create_playlist_folder,
            min_duration, max_duration, include_keywords, exclude_keywords
        )
        
        # Confirm and execute
        self._confirm_and_execute(args, "Download")
    
    def _batch_wizard(self) -> None:
        """Interactive batch processing wizard."""
        self.console.print(Panel.fit(
            "[bold]Batch Processing Wizard[/bold]\n"
            "This wizard will help you process multiple URLs from a file.",
            title="📦 Batch Processing"
        ))
        
        # Get URLs file
        urls_file = Prompt.ask("Enter path to URLs file (.txt)")
        
        if not Path(urls_file).exists():
            self.console.print(f"[red]File not found: {urls_file}[/red]")
            return
        
        # Get common options
        quality = self._get_quality_choice()
        output_format = self._get_format_choice()
        output_dir = Prompt.ask("Output directory", default="downloads")
        
        # Batch-specific options
        self.console.print("\n[bold]Batch Options[/bold]")
        include_lyrics = Confirm.ask("Download lyrics for all?", default=False)
        resume_mode = Confirm.ask("Resume mode (skip already downloaded)?", default=True)
        parallel_downloads = IntPrompt.ask("Number of parallel downloads", default=3)
        
        # Build command
        args = [
            "--urls-file", urls_file,
            "--quality", quality,
            "--format", output_format,
            "--output", output_dir
        ]
        
        if include_lyrics:
            args.append("--lyrics")
        if resume_mode:
            args.append("--resume")
        
        # Confirm and execute
        self._confirm_and_execute(args, "Batch Processing")
    
    def _playlist_wizard(self) -> None:
        """Interactive playlist wizard."""
        self.console.print(Panel.fit(
            "[bold]Playlist Wizard[/bold]\n"
            "This wizard will help you download and manage YouTube playlists.",
            title="🎵 Playlist Operations"
        ))
        
        # Get playlist URL
        playlist_url = Prompt.ask("Enter playlist URL")
        
        if not playlist_url.startswith(("http://", "https://")):
            self.console.print("[red]Please enter a valid URL[/red]")
            return
        
        # Get basic options
        quality = self._get_quality_choice()
        output_format = self._get_format_choice()
        output_dir = Prompt.ask("Output directory", default="downloads")
        
        # Playlist-specific options
        self.console.print("\n[bold]Playlist Options[/bold]")
        include_lyrics = Confirm.ask("Download lyrics?", default=False)
        create_playlist_folder = Confirm.ask("Create playlist folder?", default=True)
        resume_mode = Confirm.ask("Resume mode?", default=True)
        
        # Advanced filters
        use_filters = Confirm.ask("Use advanced filters?", default=False)
        min_duration = None
        max_duration = None
        include_keywords = None
        exclude_keywords = None
        
        if use_filters:
            min_duration = IntPrompt.ask("Minimum duration (seconds)", default=0)
            max_duration = IntPrompt.ask("Maximum duration (seconds)", default=3600)
            include_keywords = Prompt.ask("Include keywords (comma-separated)", default="")
            exclude_keywords = Prompt.ask("Exclude keywords (comma-separated)", default="")
        
        # Build command
        args = [
            playlist_url,
            "--quality", quality,
            "--format", output_format,
            "--output", output_dir
        ]
        
        if include_lyrics:
            args.append("--lyrics")
        if create_playlist_folder:
            args.append("--playlist-folder")
        if resume_mode:
            args.append("--resume")
        
        if min_duration is not None:
            args.extend(["--min-duration", str(min_duration)])
        if max_duration is not None:
            args.extend(["--max-duration", str(max_duration)])
        if include_keywords:
            args.extend(["--include", include_keywords])
        if exclude_keywords:
            args.extend(["--exclude", exclude_keywords])
        
        # Confirm and execute
        self._confirm_and_execute(args, "Playlist Download")
    
    def _search_wizard(self) -> None:
        """Interactive search wizard."""
        self.console.print(Panel.fit(
            "[bold]Search Wizard[/bold]\n"
            "This wizard will help you search YouTube and download results.",
            title="🔍 YouTube Search"
        ))
        
        # Get search query
        query = Prompt.ask("Enter search query")
        search_limit = IntPrompt.ask("Number of results to download", default=10, min=1, max=50)
        
        # Get basic options
        quality = self._get_quality_choice()
        output_format = self._get_format_choice()
        output_dir = Prompt.ask("Output directory", default="downloads")
        
        # Search-specific options
        self.console.print("\n[bold]Search Options[/bold]")
        include_lyrics = Confirm.ask("Download lyrics?", default=False)
        create_playlist_folder = Confirm.ask("Create search results folder?", default=True)
        
        # Build command
        args = [
            "--search",
            "--search-limit", str(search_limit),
            query,
            "--quality", quality,
            "--format", output_format,
            "--output", output_dir
        ]
        
        if include_lyrics:
            args.append("--lyrics")
        if create_playlist_folder:
            args.append("--playlist-folder")
        
        # Confirm and execute
        self._confirm_and_execute(args, "Search and Download")
    
    def _config_wizard(self) -> None:
        """Interactive configuration wizard."""
        self.console.print(Panel.fit(
            "[bold]Configuration Wizard[/bold]\n"
            "This wizard will help you manage your settings and preferences.",
            title="⚙️ Configuration"
        ))
        
        # Show current config
        self._show_current_config()
        
        # Configuration options
        self.console.print("\n[bold]Configuration Options[/bold]")
        config_choices = [
            "1. Set default quality",
            "2. Set default output directory",
            "3. Set default format",
            "4. Configure auto-update settings",
            "5. Reset to defaults",
            "0. Back to main menu"
        ]
        
        for choice in config_choices:
            self.console.print(choice)
        
        choice = Prompt.ask("Select configuration option", choices=["0", "1", "2", "3", "4", "5"])
        
        if choice == "1":
            new_quality = self._get_quality_choice()
            self.config.set_default_quality(new_quality)
            self.console.print(f"[green]Default quality set to {new_quality}kbps[/green]")
        elif choice == "2":
            new_output = Prompt.ask("Enter default output directory")
            self.config.set_default_output_dir(new_output)
            self.console.print(f"[green]Default output directory set to {new_output}[/green]")
        elif choice == "3":
            new_format = self._get_format_choice()
            self.config.set_default_format(new_format)
            self.console.print(f"[green]Default format set to {new_format}[/green]")
        elif choice == "4":
            self._configure_auto_update()
        elif choice == "5":
            if Confirm.ask("Are you sure you want to reset to defaults?"):
                self.config.reset_to_defaults()
                self.console.print("[green]Configuration reset to defaults[/green]")
    
    def _analytics_wizard(self) -> None:
        """Interactive analytics wizard."""
        self.console.print(Panel.fit(
            "[bold]Analytics Wizard[/bold]\n"
            "This wizard will show you download statistics and reports.",
            title="📊 Analytics"
        ))
        
        # Show analytics
        self._show_analytics()
    
    def _help_wizard(self) -> None:
        """Interactive help wizard."""
        self.console.print(Panel.fit(
            "[bold]Help Wizard[/bold]\n"
            "This wizard will help you learn about the features and usage.",
            title="❓ Help"
        ))
        
        help_topics = [
            "1. Basic usage",
            "2. Advanced features",
            "3. Troubleshooting",
            "4. Examples",
            "0. Back to main menu"
        ]
        
        for topic in help_topics:
            self.console.print(topic)
        
        choice = Prompt.ask("Select help topic", choices=["0", "1", "2", "3", "4"])
        
        if choice == "1":
            self._show_basic_help()
        elif choice == "2":
            self._show_advanced_help()
        elif choice == "3":
            self._show_troubleshooting_help()
        elif choice == "4":
            self._show_examples_help()
    
    def _get_quality_choice(self) -> str:
        """Get quality choice from user."""
        quality_choices = ["128", "192", "320"]
        quality_table = Table(title="Quality Options")
        quality_table.add_column("Option", style="cyan")
        quality_table.add_column("Quality", style="magenta")
        quality_table.add_column("Description", style="green")
        
        quality_table.add_row("1", "128 kbps", "Lower quality, smaller files")
        quality_table.add_row("2", "192 kbps", "Good balance")
        quality_table.add_row("3", "320 kbps", "High quality, larger files")
        
        self.console.print(quality_table)
        
        choice = Prompt.ask("Select quality", choices=["1", "2", "3"])
        return quality_choices[int(choice) - 1]
    
    def _get_format_choice(self) -> str:
        """Get format choice from user."""
        format_choices = ["mp3", "m4a", "opus", "flac"]
        format_table = Table(title="Format Options")
        format_table.add_column("Option", style="cyan")
        format_table.add_column("Format", style="magenta")
        format_table.add_column("Description", style="green")
        
        format_table.add_row("1", "MP3", "Most compatible")
        format_table.add_row("2", "M4A", "Apple devices")
        format_table.add_row("3", "Opus", "Modern, efficient")
        format_table.add_row("4", "FLAC", "Lossless")
        
        self.console.print(format_table)
        
        choice = Prompt.ask("Select format", choices=["1", "2", "3", "4"])
        return format_choices[int(choice) - 1]
    
    def _build_download_args(self, url: str, quality: str, output_format: str, 
                           output_dir: str, is_search: bool, include_lyrics: bool,
                           embed_metadata: bool, create_playlist_folder: bool,
                           min_duration: Optional[int], max_duration: Optional[int],
                           include_keywords: Optional[str], exclude_keywords: Optional[str]) -> List[str]:
        """Build command line arguments for download."""
        args = [url, "--quality", quality, "--format", output_format, "--output", output_dir]
        
        if is_search:
            args = ["--search"] + args
        
        if include_lyrics:
            args.append("--lyrics")
        
        if not embed_metadata:
            args.append("--no-metadata")
        
        if not create_playlist_folder:
            args.append("--no-playlist-folder")
        
        if min_duration is not None:
            args.extend(["--min-duration", str(min_duration)])
        if max_duration is not None:
            args.extend(["--max-duration", str(max_duration)])
        if include_keywords:
            args.extend(["--include", include_keywords])
        if exclude_keywords:
            args.extend(["--exclude", exclude_keywords])
        
        return args
    
    def _confirm_and_execute(self, args: List[str], operation: str) -> None:
        """Confirm and execute the command."""
        self.console.print(f"\n[bold]Command to execute:[/bold]")
        self.console.print(f"youtube-audio-extractor {' '.join(args)}")
        
        if Confirm.ask(f"\nExecute {operation}?"):
            try:
                # Execute via module to avoid circular imports
                cmd = [sys.executable, "-m", "src.main", *args]
                result = subprocess.run(cmd)
                if result.returncode != 0:
                    self.console.print(f"[red]Command exited with code {result.returncode}[/red]")
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
        else:
            self.console.print("Operation cancelled.")
    
    def _show_current_config(self) -> None:
        """Show current configuration."""
        config_table = Table(title="Current Configuration")
        config_table.add_column("Setting", style="cyan")
        config_table.add_column("Value", style="green")
        
        config_table.add_row("Default Quality", f"{self.config.default_quality}kbps")
        config_table.add_row("Default Output", self.config.default_output_dir)
        config_table.add_row("Default Format", self.config.default_format)
        config_table.add_row("Config Directory", str(self.config.config_dir))
        
        self.console.print(config_table)
    
    def _configure_auto_update(self) -> None:
        """Configure auto-update settings."""
        self.console.print("\n[bold]Auto-Update Configuration[/bold]")
        
        enable_auto_update = Confirm.ask("Enable automatic update checking?", default=True)
        if enable_auto_update:
            check_interval = IntPrompt.ask("Check interval (hours)", default=24, min=1, max=168)
            self.config.set_auto_update_settings(True, check_interval)
            self.console.print(f"[green]Auto-update enabled (check every {check_interval} hours)[/green]")
        else:
            self.config.set_auto_update_settings(False, 24)
            self.console.print("[green]Auto-update disabled[/green]")
    
    def _show_analytics(self) -> None:
        """Show analytics and statistics."""
        # This would integrate with the analytics module
        self.console.print("\n[bold]Download Analytics[/bold]")
        self.console.print("Analytics features coming soon!")
    
    def _show_basic_help(self) -> None:
        """Show basic help information."""
        help_text = """
[bold]Basic Usage[/bold]

1. Download a single video:
   youtube-audio-extractor "https://www.youtube.com/watch?v=VIDEO_ID"

2. Download a playlist:
   youtube-audio-extractor "https://www.youtube.com/playlist?list=PLAYLIST_ID"

3. Search and download:
   youtube-audio-extractor --search "artist name"

4. Use the web interface:
   youtube-audio-extractor-web
        """
        self.console.print(Panel(help_text, title="Basic Help"))
    
    def _show_advanced_help(self) -> None:
        """Show advanced help information."""
        help_text = """
[bold]Advanced Features[/bold]

1. Quality and format options:
   -q 320 --format mp3

2. Filters:
   --min-duration 120 --max-duration 600
   --include "remix,live" --exclude "cover"

3. Batch processing:
   --urls-file urls.txt

4. Resume downloads:
   --resume

5. Download lyrics:
   --lyrics
        """
        self.console.print(Panel(help_text, title="Advanced Help"))
    
    def _show_troubleshooting_help(self) -> None:
        """Show troubleshooting help."""
        help_text = """
[bold]Troubleshooting[/bold]

1. "ffmpeg not found":
   - Install ffmpeg: brew install ffmpeg (macOS)
   - Or: sudo apt install ffmpeg (Ubuntu)

2. "Permission denied":
   - Check output directory permissions
   - Try different output directory

3. "Video unavailable":
   - Verify URL is correct
   - Check if video is private/region-restricted

4. "Network timeout":
   - Check internet connection
   - Try again later
        """
        self.console.print(Panel(help_text, title="Troubleshooting"))
    
    def _show_examples_help(self) -> None:
        """Show examples help."""
        help_text = """
[bold]Examples[/bold]

1. High quality single video:
   youtube-audio-extractor -q 320 "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

2. Playlist with filters:
   youtube-audio-extractor --min-duration 120 --max-duration 600 "PLAYLIST_URL"

3. Search with lyrics:
   youtube-audio-extractor --search --lyrics "beyonce"

4. Batch processing:
   youtube-audio-extractor --urls-file urls.txt -q 192
        """
        self.console.print(Panel(help_text, title="Examples"))


def start_interactive_mode(config: AppConfig) -> None:
    """Start the interactive mode."""
    wizard = InteractiveWizard(config)
    wizard.start()
