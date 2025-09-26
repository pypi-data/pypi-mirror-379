#!/usr/bin/env python3
"""DinoScan CLI - Command line interface for DinoScan code analysis"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

from .analyzers import AVAILABLE_ANALYZERS
from .core import DinoScan


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="DinoScan - Advanced Python code analysis tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "analyzer",
        choices=list(AVAILABLE_ANALYZERS.keys()) + ["all"],
        help="Analyzer to run (or 'all' for all analyzers)",
    )

    parser.add_argument("file", type=Path, help="Python file to analyze")

    parser.add_argument(
        "--format",
        choices=["json", "text"],
        default="json",
        help="Output format (default: json)",
    )

    parser.add_argument(
        "--profile",
        choices=["minimal", "standard", "comprehensive"],
        default="standard",
        help="Analysis profile (default: standard)",
    )

    parser.add_argument(
        "--exclude",
        action="append",
        help="Exclude patterns (can be used multiple times)",
    )

    parser.add_argument("--version", action="version", version="DinoScan 1.0.0")

    args = parser.parse_args()

    # Validate file exists
    if not args.file.exists():
        print(f"Error: File {args.file} does not exist", file=sys.stderr)
        sys.exit(1)

    if args.file.suffix != ".py":
        print(f"Error: File {args.file} is not a Python file", file=sys.stderr)
        sys.exit(1)

    try:
        # Initialize DinoScan
        scanner = DinoScan(profile=args.profile, exclude_patterns=args.exclude or [])

        # Run analysis
        if args.analyzer == "all":
            results = scanner.analyze_all(args.file)
        else:
            results = scanner.analyze(args.file, args.analyzer)

        # Output results
        if args.format == "json":
            print(json.dumps(results, indent=2))
        else:
            print_text_results(results)

    except Exception as e:
        print(f"Error during analysis: {e}", file=sys.stderr)
        sys.exit(1)


def print_text_results(results: List[Dict[str, Any]]):
    """Print results in human-readable text format"""
    if not results:
        print("No issues found.")
        return

    for result in results:
        severity = result.get("severity", "info").upper()
        file_path = result.get("file", "unknown")
        line = result.get("line", 0)
        column = result.get("column", 0)
        message = result.get("message", "No message")
        rule_id = result.get("rule_id", "")
        analyzer = result.get("analyzer", "unknown")

        location = f"{file_path}:{line}:{column}"
        rule_info = f" [{rule_id}]" if rule_id else ""

        print(f"{severity}: {message}{rule_info}")
        print(f"  --> {location} ({analyzer})")
        print()


if __name__ == "__main__":
    main()
