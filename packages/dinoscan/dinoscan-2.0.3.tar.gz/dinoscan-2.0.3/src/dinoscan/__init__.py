"""DinoScan - Advanced Python code analysis tool"""

__version__ = "2.0.3"
__author__ = "DinoScan Team"
__email__ = "contact@dinoscan.com"

from .analyzers import (
    CircularImportAnalyzer,
    DeadCodeAnalyzer,
    DocsAnalyzer,
    DuplicateAnalyzer,
    SecurityAnalyzer,
)
from .core import DinoScan

__all__ = [
    "DinoScan",
    "SecurityAnalyzer",
    "DeadCodeAnalyzer",
    "CircularImportAnalyzer",
    "DuplicateAnalyzer",
    "DocsAnalyzer",
]
