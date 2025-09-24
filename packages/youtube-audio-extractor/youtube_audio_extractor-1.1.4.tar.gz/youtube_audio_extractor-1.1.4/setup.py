"""Setup configuration for YouTube Audio Extractor."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements.txt if it exists
try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    # Fallback requirements if requirements.txt is not found
    requirements = [
        "yt-dlp>=2023.7.6",
        "ffmpeg-python>=0.2.0", 
        "mutagen>=1.47.0",
        "click>=8.1.0"
    ]

setup(
    name="youtube-audio-extractor",
    version="1.1.4",
    author="KetchaLegend",
    author_email="kbepa02@gmail.com",
    description="Extract audio from YouTube videos and playlists, convert to MP3 format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ketchalegend/youtube-extractor",
    project_urls={
        "Bug Reports": "https://github.com/ketchalegend/youtube-extractor/issues",
        "Source": "https://github.com/ketchalegend/youtube-extractor",
        "Documentation": "https://github.com/ketchalegend/youtube-extractor#readme",
        "Changelog": "https://github.com/ketchalegend/youtube-extractor/blob/main/CHANGELOG.md",
    },
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "youtube-audio-extractor=src.main:main",
            "youtube-audio-extractor-web=src.web:run",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Internet :: WWW/HTTP",
    ],
)