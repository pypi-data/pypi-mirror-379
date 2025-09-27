"""Tests for DinoScan CLI functionality"""

import json
import tempfile
from io import StringIO
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from dinoscan.cli import main


class TestDinoscanCLI(TestCase):
    """Test DinoScan CLI functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_file_content = """

def test_function():
    password = "secret123"
    eval("dangerous_code")
    return True


def unused_function():
    return False
"""

    def create_temp_python_file(self, content=None):
        """Create a temporary Python file for testing"""
        if content is None:
            content = self.test_file_content

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            return Path(temp_file.name)

    def test_help_command(self):
        """Test that --help works"""
        with patch("sys.argv", ["dinoscan", "--help"]):
            with self.assertRaises(SystemExit) as cm:
                main()
            # Help should exit with code 0
            self.assertEqual(cm.exception.code, 0)

    def test_version_command(self):
        """Test that --version works"""
        with patch("sys.argv", ["dinoscan", "--version"]):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)

    def test_analyze_with_security_analyzer(self):
        """Test analyzing a file with security analyzer"""
        temp_file = self.create_temp_python_file()

        with (
            patch("sys.argv", ["dinoscan", "security", str(temp_file)]),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should be valid JSON
            result = json.loads(output)
            self.assertIsInstance(result, list)

            # Should contain security findings
            security_findings = [f for f in result if f.get("analyzer") == "security"]
            self.assertGreater(len(security_findings), 0)

    def test_analyze_with_all_analyzers(self):
        """Test analyzing a file with all analyzers"""
        temp_file = self.create_temp_python_file()

        with (
            patch("sys.argv", ["dinoscan", "all", str(temp_file)]),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should be valid JSON
            result = json.loads(output)
            self.assertIsInstance(result, list)

            # Should contain findings from multiple analyzers
            analyzers_found = {f.get("analyzer") for f in result if f.get("analyzer")}
            self.assertGreater(len(analyzers_found), 1)

    def test_text_output_format(self):
        """Test text output format"""
        temp_file = self.create_temp_python_file()

        with (
            patch(
                "sys.argv", ["dinoscan", "security", str(temp_file), "--format", "text"]
            ),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should contain human-readable text, not JSON
            self.assertNotEqual(output.strip(), "")
            # Should not be JSON (will raise exception if it is)
            with self.assertRaises(json.JSONDecodeError):
                json.loads(output)

    def test_json_output_format(self):
        """Test JSON output format (default)"""
        temp_file = self.create_temp_python_file()

        with (
            patch(
                "sys.argv", ["dinoscan", "security", str(temp_file), "--format", "json"]
            ),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should be valid JSON
            result = json.loads(output)
            self.assertIsInstance(result, list)

    def test_analysis_profile_options(self):
        """Test different analysis profile options"""
        temp_file = self.create_temp_python_file()

        profiles = ["minimal", "standard", "comprehensive"]

        for profile in profiles:
            with (
                patch(
                    "sys.argv",
                    ["dinoscan", "security", str(temp_file), "--profile", profile],
                ),
                patch("sys.stdout", new=StringIO()) as fake_out,
            ):
                main()
                output = fake_out.getvalue()

                # Should be valid JSON
                result = json.loads(output)
                self.assertIsInstance(result, list)

    def test_exclude_patterns(self):
        """Test exclude patterns functionality"""
        temp_file = self.create_temp_python_file()

        with (
            patch(
                "sys.argv",
                [
                    "dinoscan",
                    "security",
                    str(temp_file),
                    "--exclude",
                    "test*",
                    "--exclude",
                    "*.tmp",
                ],
            ),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should be valid JSON
            result = json.loads(output)
            self.assertIsInstance(result, list)

    def test_nonexistent_file_error(self):
        """Test error handling for nonexistent files"""
        with (
            patch("sys.argv", ["dinoscan", "security", "nonexistent_file.py"]),
            patch("sys.stderr", new=StringIO()) as fake_err,
        ):
            with self.assertRaises(SystemExit) as cm:
                main()

            self.assertEqual(cm.exception.code, 1)
            error_output = fake_err.getvalue()
            self.assertIn("does not exist", error_output)

    def test_non_python_file_error(self):
        """Test error handling for non-Python files"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".txt", delete=False
            ) as f:
                temp_file = f.name
                f.write("Not Python code")
                f.flush()

            with (
                patch("sys.argv", ["dinoscan", "security", temp_file]),
                patch("sys.stderr", new=StringIO()) as fake_err,
            ):
                with self.assertRaises(SystemExit) as cm:
                    main()

                self.assertEqual(cm.exception.code, 1)
                error_output = fake_err.getvalue()
                self.assertIn("not a Python file", error_output)
        finally:
            if temp_file and Path(temp_file).exists():
                Path(temp_file).unlink()

    def test_invalid_analyzer_error(self):
        """Test error handling for invalid analyzer names"""
        temp_file = self.create_temp_python_file()

        with patch("sys.argv", ["dinoscan", "invalid_analyzer", str(temp_file)]):
            with self.assertRaises(SystemExit) as cm:
                main()
            # Should exit with error code due to invalid choice
            self.assertEqual(cm.exception.code, 2)

    def test_empty_file_analysis(self):
        """Test analyzing an empty Python file"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
                temp_file = f.name
                f.write("")
                f.flush()

            with (
                patch("sys.argv", ["dinoscan", "security", temp_file]),
                patch("sys.stdout", new=StringIO()) as fake_out,
            ):
                main()
                output = fake_out.getvalue()

                # Should be valid JSON with empty results
                result = json.loads(output)
                self.assertIsInstance(result, list)
        finally:
            if temp_file and Path(temp_file).exists():
                Path(temp_file).unlink()

    def test_syntax_error_file_analysis(self):
        """Test analyzing a file with syntax errors"""
        temp_file = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
                temp_file = f.name
                f.write("def invalid_syntax(\n")  # Missing closing parenthesis
                f.flush()

            with (
                patch("sys.argv", ["dinoscan", "security", temp_file]),
                patch("sys.stdout", new=StringIO()) as fake_out,
            ):
                main()
                output = fake_out.getvalue()

                # Should be valid JSON with syntax error
                result = json.loads(output)
                self.assertIsInstance(result, list)

                # Should contain syntax error
                syntax_errors = [f for f in result if f.get("rule_id") == "SYNTAX001"]
                self.assertGreater(len(syntax_errors), 0)
        finally:
            if temp_file and Path(temp_file).exists():
                Path(temp_file).unlink()

    def test_analysis_error_handling(self):
        """Test error handling during analysis"""
        temp_file = self.create_temp_python_file()

        # Test with a valid file but mock an analysis error
        with patch("dinoscan.core.DinoScan.analyze") as mock_analyze:
            mock_analyze.side_effect = Exception("Analysis failed")

            with (
                patch("sys.argv", ["dinoscan", "security", str(temp_file)]),
                patch("sys.stderr", new=StringIO()) as fake_err,
            ):
                with self.assertRaises(SystemExit) as cm:
                    main()

                self.assertEqual(cm.exception.code, 1)
                error_output = fake_err.getvalue()
                self.assertIn("Error during analysis", error_output)

    def test_clean_file_no_issues(self):
        """Test analyzing a clean file with no issues"""
        clean_code = """
def clean_function():
    '''A well-documented function'''
    return 'clean code'

result = clean_function()
"""
        temp_file = self.create_temp_python_file(clean_code)

        with (
            patch("sys.argv", ["dinoscan", "security", str(temp_file)]),
            patch("sys.stdout", new=StringIO()) as fake_out,
        ):
            main()
            output = fake_out.getvalue()

            # Should be valid JSON
            result = json.loads(output)
            self.assertIsInstance(result, list)
            # May be empty for security analyzer on clean code
