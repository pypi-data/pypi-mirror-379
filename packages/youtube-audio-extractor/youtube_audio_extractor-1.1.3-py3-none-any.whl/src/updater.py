"""Auto-update functionality for YouTube Audio Extractor."""

import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional, Dict, Any
import requests
from packaging import version

from .config import AppConfig


class UpdateChecker:
    """Handles checking for and installing updates automatically."""
    
    def __init__(self, config: AppConfig):
        self.config = config
        self.current_version = self._get_current_version()
        self.github_api_url = "https://api.github.com/repos/ketchalegend/youtube-extractor/releases/latest"
        self.pypi_api_url = "https://pypi.org/pypi/youtube-audio-extractor/json"
    
    def _get_current_version(self) -> str:
        """Get the current installed version."""
        try:
            # Try to get version from package metadata
            result = subprocess.run(
                [sys.executable, "-c", "import youtube_audio_extractor; print(youtube_audio_extractor.__version__)"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except Exception:
            pass
        
        # Fallback to setup.py version
        try:
            setup_path = Path(__file__).parent.parent / "setup.py"
            if setup_path.exists():
                with open(setup_path, 'r') as f:
                    content = f.read()
                    for line in content.split('\n'):
                        if 'version=' in line:
                            # Extract version from setup.py
                            version_line = line.strip()
                            if '"' in version_line:
                                start = version_line.find('"') + 1
                                end = version_line.find('"', start)
                                return version_line[start:end]
        except Exception:
            pass
        
        return "1.2.0"  # Fallback version
    
    def check_for_updates(self, check_pypi: bool = True) -> Optional[Dict[str, Any]]:
        """
        Check for available updates.
        
        Args:
            check_pypi: Whether to check PyPI for updates (default: True)
            
        Returns:
            Dict with update info if available, None if up to date
        """
        try:
            if check_pypi:
                return self._check_pypi_updates()
            else:
                return self._check_github_updates()
        except Exception as e:
            print(f"Error checking for updates: {e}")
            return None
    
    def _check_pypi_updates(self) -> Optional[Dict[str, Any]]:
        """Check PyPI for updates."""
        try:
            response = requests.get(self.pypi_api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            latest_version = data['info']['version']
            
            if version.parse(latest_version) > version.parse(self.current_version):
                return {
                    'version': latest_version,
                    'current_version': self.current_version,
                    'source': 'pypi',
                    'url': f"https://pypi.org/project/youtube-audio-extractor/{latest_version}/",
                    'changelog': data['info'].get('description', ''),
                    'release_date': data['releases'][latest_version][0]['upload_time'] if latest_version in data['releases'] else None
                }
        except Exception as e:
            print(f"Error checking PyPI: {e}")
        
        return None
    
    def _check_github_updates(self) -> Optional[Dict[str, Any]]:
        """Check GitHub releases for updates."""
        try:
            response = requests.get(self.github_api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            latest_version = data['tag_name'].lstrip('v')  # Remove 'v' prefix if present
            
            if version.parse(latest_version) > version.parse(self.current_version):
                return {
                    'version': latest_version,
                    'current_version': self.current_version,
                    'source': 'github',
                    'url': data['html_url'],
                    'changelog': data.get('body', ''),
                    'release_date': data['published_at']
                }
        except Exception as e:
            print(f"Error checking GitHub: {e}")
        
        return None
    
    def install_update(self, update_info: Dict[str, Any], force: bool = False) -> bool:
        """
        Install the available update.
        
        Args:
            update_info: Update information from check_for_updates()
            force: Force installation even if user doesn't confirm
            
        Returns:
            True if update was installed successfully
        """
        if not force:
            print(f"\n🔄 Update available!")
            print(f"Current version: {update_info['current_version']}")
            print(f"Latest version: {update_info['version']}")
            print(f"Source: {update_info['source']}")
            print(f"URL: {update_info['url']}")
            
            if update_info.get('changelog'):
                print(f"\nChangelog:")
                print(update_info['changelog'][:500] + "..." if len(update_info['changelog']) > 500 else update_info['changelog'])
            
            response = input(f"\nDo you want to install the update? (y/N): ").strip().lower()
            if response not in ['y', 'yes']:
                print("Update cancelled.")
                return False
        
        try:
            print(f"\n📦 Installing update to version {update_info['version']}...")
            
            # Install from PyPI
            cmd = [sys.executable, "-m", "pip", "install", "--upgrade", "youtube-audio-extractor"]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"✅ Successfully updated to version {update_info['version']}!")
                print("Please restart the application to use the new version.")
                return True
            else:
                print(f"❌ Update failed: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Update timed out. Please try again.")
            return False
        except Exception as e:
            print(f"❌ Update failed: {e}")
            return False
    
    def auto_check_and_update(self, check_interval_hours: int = 24) -> bool:
        """
        Automatically check for updates and install if available.
        
        Args:
            check_interval_hours: Hours between update checks
            
        Returns:
            True if update was installed
        """
        # Check if we should check for updates
        last_check_file = Path(self.config.config_dir) / "last_update_check"
        
        if last_check_file.exists():
            try:
                last_check = float(last_check_file.read_text().strip())
                time_since_check = time.time() - last_check
                hours_since_check = time_since_check / 3600
                
                if hours_since_check < check_interval_hours:
                    return False  # Too soon to check
            except (ValueError, OSError):
                pass  # File corrupted, proceed with check
        
        # Check for updates
        update_info = self.check_for_updates()
        
        # Update last check time
        try:
            last_check_file.parent.mkdir(parents=True, exist_ok=True)
            last_check_file.write_text(str(time.time()))
        except OSError:
            pass  # Can't save, but continue
        
        if update_info:
            return self.install_update(update_info, force=False)
        
        return False
    
    def show_update_info(self) -> None:
        """Show current version and update status."""
        print(f"Current version: {self.current_version}")
        
        update_info = self.check_for_updates()
        if update_info:
            print(f"🔄 Update available: {update_info['version']}")
            print(f"Source: {update_info['source']}")
            print(f"URL: {update_info['url']}")
        else:
            print("✅ You're running the latest version!")


def check_and_update(config: AppConfig, force_check: bool = False) -> bool:
    """
    Convenience function to check for updates.
    
    Args:
        config: App configuration
        force_check: Force check even if recently checked
        
    Returns:
        True if update was installed
    """
    updater = UpdateChecker(config)
    
    if force_check:
        update_info = updater.check_for_updates()
        if update_info:
            return updater.install_update(update_info, force=False)
    else:
        return updater.auto_check_and_update()
    
    return False
