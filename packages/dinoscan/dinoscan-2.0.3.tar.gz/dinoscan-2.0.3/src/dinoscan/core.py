"""Core DinoScan functionality"""

import ast
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from .analyzers import AVAILABLE_ANALYZERS


class DinoScan:
    """Main DinoScan analyzer class"""

    def __init__(
        self, profile: str = "standard", exclude_patterns: Optional[List[str]] = None
    ):
        self.profile = profile
        self.exclude_patterns = exclude_patterns or []

    def analyze(
        self, file_path: Union[str, Path], analyzer_name: str
    ) -> List[Dict[str, Any]]:
        """Analyze a file with a specific analyzer"""
        if analyzer_name not in AVAILABLE_ANALYZERS:
            raise ValueError(f"Unknown analyzer: {analyzer_name}")

        # Convert to Path object if string is passed
        if isinstance(file_path, str):
            file_path = Path(file_path)

        # Validate file exists and is a Python file
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if file_path.suffix != ".py":
            raise ValueError(f"Not a Python file: {file_path}")

        # Read file content
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            raise RuntimeError(f"Failed to read file {file_path}: {e}")

        # Parse AST
        try:
            tree = ast.parse(content, filename=str(file_path))
        except SyntaxError as e:
            return [
                {
                    "file": str(file_path),
                    "line": e.lineno or 1,
                    "column": e.offset or 1,
                    "severity": "error",
                    "message": f"Syntax error: {e.msg}",
                    "rule_id": "SYNTAX001",
                    "analyzer": "parser",
                    "category": "syntax",
                    "fix_suggestion": "Fix the syntax error in your Python code",
                }
            ]

        # Run analyzer
        analyzer_class = AVAILABLE_ANALYZERS[analyzer_name]
        analyzer = analyzer_class(profile=self.profile)

        return analyzer.analyze(tree, file_path, content)

    def analyze_all(self, file_path: Union[str, Path]) -> List[Dict[str, Any]]:
        """Analyze a file with all available analyzers"""
        all_results = []

        for analyzer_name in AVAILABLE_ANALYZERS:
            try:
                results = self.analyze(file_path, analyzer_name)
                all_results.extend(results)
            except Exception as e:
                # Add error result for failed analyzer
                all_results.append(
                    {
                        "file": str(file_path),
                        "line": 1,
                        "column": 1,
                        "severity": "error",
                        "message": f"Analyzer '{analyzer_name}' failed: {e}",
                        "rule_id": "ANALYZER_ERROR",
                        "analyzer": analyzer_name,
                        "category": "internal",
                        "fix_suggestion": (
                            f"Check the file format and content for {analyzer_name} "
                            "compatibility"
                        ),
                    }
                )

        return all_results
