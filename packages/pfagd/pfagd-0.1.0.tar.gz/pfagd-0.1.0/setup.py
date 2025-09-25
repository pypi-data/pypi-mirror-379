"""
PFAGD Setup Configuration
Pip-installable package setup for Python for Android Game Development
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read version
version_file = Path(__file__).parent / "pfagd" / "version.py"
version_vars = {}
exec(version_file.read_text(encoding='utf-8'), version_vars)
VERSION = version_vars['__version__']

# Read README
readme_file = Path(__file__).parent / "README.md"
LONG_DESCRIPTION = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ""

# Requirements
INSTALL_REQUIRES = [
    "kivy>=2.1.0",
    "Pillow>=8.0.0",
    "requests>=2.25.0",
    "buildozer>=1.4.0",  # For Android builds
    "PyInstaller>=4.0",  # For desktop builds
]

# Optional requirements for different platforms
EXTRAS_REQUIRE = {
    'android': [
        'pyjnius>=1.4.0',  # For Android API access
        'plyer>=2.0.0',    # For platform features
    ],
    'desktop': [
        'pygame>=2.0.0',   # Alternative renderer for desktop
        'PyQt5>=5.15.0',   # Alternative UI toolkit
    ],
    'dev': [
        'pytest>=6.0.0',
        'pytest-cov>=2.0.0',
        'black>=21.0.0',
        'flake8>=3.8.0',
        'mypy>=0.800',
    ],
}

# All extras combined
EXTRAS_REQUIRE['all'] = sum(EXTRAS_REQUIRE.values(), [])

setup(
    name="pfagd",
    version=VERSION,
    author="PFAGD Development Team",
    author_email="dev@pfagd.org",
    description="Python for Android Game Development - Cross-platform game framework",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/pfagd/pfagd",
    project_urls={
        "Bug Tracker": "https://github.com/pfagd/pfagd/issues",
        "Documentation": "https://pfagd.readthedocs.io/",
        "Source": "https://github.com/pfagd/pfagd",
    },
    
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pfagd': [
            'templates/**/*',
            'examples/**/*',
            'docs/**/*',
        ],
    },
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    
    entry_points={
        "console_scripts": [
            "pfagd=pfagd.cli.main:main",
        ],
    },
    
    keywords=[
        "game", "development", "android", "cross-platform", 
        "kivy", "mobile", "desktop", "2d", "3d", "gamedev"
    ],
    
    zip_safe=False,  # Kivy requires files to be extractable
)