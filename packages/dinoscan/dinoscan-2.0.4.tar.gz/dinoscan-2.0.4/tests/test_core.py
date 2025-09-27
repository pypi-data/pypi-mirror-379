"""Tests for DinoScan core functionality"""

import os
import sys
import tempfile
from pathlib import Path
from unittest import TestCase

import pytest

from dinoscan.core import DinoScan

# Cross-platform test decorators
skip_on_windows = pytest.mark.skipif(
    sys.platform.startswith("win"), reason="POSIX-only behavior"
)
skip_on_posix = pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="Windows-only behavior"
)


class TestDinoScanCore(TestCase):
    """Test DinoScan core functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.scanner = DinoScan()

    def test_init_default_profile(self):
        """Test DinoScan initialization with default profile"""
        scanner = DinoScan()
        self.assertEqual(scanner.profile, "standard")
        self.assertEqual(scanner.exclude_patterns, [])

    def test_init_custom_profile(self):
        """Test DinoScan initialization with custom profile"""
        scanner = DinoScan(profile="comprehensive", exclude_patterns=["test/"])
        self.assertEqual(scanner.profile, "comprehensive")
        self.assertEqual(scanner.exclude_patterns, ["test/"])

    def test_analyze_nonexistent_file(self):
        """Test analyzing a file that doesn't exist"""
        with self.assertRaises(FileNotFoundError):
            self.scanner.analyze(Path("nonexistent.py"), "security")

    def test_analyze_non_python_file(self):
        """Test analyzing a non-Python file"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
                temp_file = f.name
                f.write(b"Not Python code")
                f.flush()

            with self.assertRaises(ValueError):
                self.scanner.analyze(Path(temp_file), "security")
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_analyze_invalid_analyzer(self):
        """Test using an invalid analyzer name"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
                temp_file = f.name
                f.write(b"print('hello')")
                f.flush()

            with self.assertRaises(ValueError):
                self.scanner.analyze(Path(temp_file), "invalid_analyzer")
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_analyze_syntax_error(self):
        """Test analyzing a file with syntax errors"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("def invalid_syntax(\n")  # Missing closing parenthesis
                f.flush()

            results = self.scanner.analyze(Path(temp_file), "security")
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]["rule_id"], "SYNTAX001")
            self.assertEqual(results[0]["severity"], "error")
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_analyze_valid_file(self):
        """Test analyzing a valid Python file"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("def hello_world():\n    print('Hello, World!')\n")
                f.flush()

            results = self.scanner.analyze(Path(temp_file), "security")
            # Should not raise any exceptions and return a list
            self.assertIsInstance(results, list)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_analyze_all_valid_file(self):
        """Test analyzing a file with all analyzers"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("def hello_world():\n    print('Hello, World!')\n")
                f.flush()

            results = self.scanner.analyze_all(Path(temp_file))
            self.assertIsInstance(results, list)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_analyze_all_syntax_error(self):
        """Test analyze_all with a syntax error file"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("def invalid_syntax(\n")
                f.flush()

            results = self.scanner.analyze_all(Path(temp_file))
            # Should contain error results from each analyzer that failed
            self.assertGreater(len(results), 0)
            # First result should be syntax error
            syntax_errors = [r for r in results if r.get("rule_id") == "SYNTAX001"]
            self.assertGreater(len(syntax_errors), 0)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_string_path_conversion(self):
        """Test that string paths are converted to Path objects"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("def hello_world():\n    print('Hello, World!')\n")
                f.flush()

            # Should work with string path
            results = self.scanner.analyze(temp_file, "security")
            self.assertIsInstance(results, list)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_file_encoding(self):
        """Test handling files with different encodings"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(
                suffix=".py", delete=False, mode="w", encoding="utf-8"
            ) as f:
                temp_file = f.name
                f.write(
                    "# -*- coding: utf-8 -*-\ndef hello():\n    print('Hello 世界')\n"
                )
                f.flush()

            results = self.scanner.analyze(Path(temp_file), "security")
            self.assertIsInstance(results, list)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_empty_file(self):
        """Test analyzing an empty Python file"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode="w") as f:
                temp_file = f.name
                f.write("")
                f.flush()

            results = self.scanner.analyze(Path(temp_file), "security")
            self.assertIsInstance(results, list)
        finally:
            if temp_file and os.path.exists(temp_file):
                os.unlink(temp_file)
