"""Core data models for the GitHub IOC Scanner."""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional, Set


@dataclass
class ScanConfig:
    """Configuration for a scan operation."""
    org: Optional[str] = None
    team: Optional[str] = None
    repo: Optional[str] = None
    team_first_org: bool = False  # New team-first organization scan mode
    fast_mode: bool = False
    include_archived: bool = False
    issues_dir: Optional[str] = "issues"
    ioc_files: Optional[List[str]] = None
    # SBOM scanning options
    enable_sbom: bool = True
    disable_sbom: bool = False
    sbom_only: bool = False
    # Authentication options
    github_app_config: Optional[str] = None
    # Resume and checkpointing options
    resume: Optional[str] = None
    list_scans: bool = False
    save_state: bool = True
    no_save_state: bool = False
    # Cache management options
    clear_cache: bool = False
    clear_cache_type: Optional[str] = None
    refresh_repo: Optional[str] = None
    cache_info: bool = False
    cleanup_cache: Optional[int] = None
    # Output and logging options
    verbose: bool = False
    log_file: Optional[str] = None
    quiet: bool = False
    debug_rate_limits: bool = False
    show_stack_traces: bool = False
    suppress_rate_limit_messages: bool = False
    # Batch processing options
    enable_batch_processing: bool = True
    batch_size: Optional[int] = None
    max_concurrent: Optional[int] = None
    batch_strategy: Optional[str] = None
    enable_cross_repo_batching: Optional[bool] = None
    batch_config_file: Optional[str] = None
    # Rate limiting options
    rate_limit_strategy: str = "normal"
    enable_intelligent_rate_limiting: bool = True
    rate_limit_safety_margin: int = 50


@dataclass
class Repository:
    """Represents a GitHub repository."""
    name: str
    full_name: str
    archived: bool
    default_branch: str
    updated_at: datetime


@dataclass
class FileInfo:
    """Information about a file in a repository."""
    path: str
    sha: str
    size: int


@dataclass
class PackageDependency:
    """Represents a package dependency found in a lockfile or manifest."""
    name: str
    version: str
    dependency_type: str  # dependencies, devDependencies, etc.


@dataclass
class IOCMatch:
    """Represents a match between a package dependency and an IOC definition."""
    repo: str
    file_path: str
    package_name: str
    version: str
    ioc_source: str


@dataclass
class IOCDefinition:
    """Represents IOC definitions loaded from a Python file."""
    packages: Dict[str, Optional[Set[str]]]  # package_name -> versions or None
    source_file: str


@dataclass
class CacheStats:
    """Statistics about cache performance."""
    hits: int = 0
    misses: int = 0
    time_saved: float = 0.0
    cache_size: int = 0


@dataclass
class ScanResults:
    """Results of a scan operation."""
    matches: List[IOCMatch]
    cache_stats: CacheStats
    repositories_scanned: int
    files_scanned: int


@dataclass
class FileContent:
    """Represents the content of a file fetched from GitHub."""
    content: str
    sha: str
    size: int


@dataclass
class APIResponse:
    """Generic wrapper for GitHub API responses with ETag support."""
    data: Optional[object] = None
    etag: Optional[str] = None
    not_modified: bool = False  # True if 304 Not Modified
    rate_limit_remaining: int = 0
    rate_limit_reset: int = 0