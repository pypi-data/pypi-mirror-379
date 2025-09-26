"""Tests for DinoScan analyzers"""

import ast
from pathlib import Path
from unittest import TestCase

from dinoscan.analyzers import (
    AVAILABLE_ANALYZERS,
    CircularImportAnalyzer,
    DeadCodeAnalyzer,
    DocsAnalyzer,
    DuplicateAnalyzer,
    SecurityAnalyzer,
)


class TestSecurityAnalyzer(TestCase):
    """Test SecurityAnalyzer functionality"""

    def setUp(self):
        """Initialize SecurityAnalyzer instance for each test."""
        self.analyzer = SecurityAnalyzer()

    def test_detect_dangerous_function_calls(self):
        """Test detection of dangerous function calls like eval() and exec()"""
        code = """
def dangerous_code():
    eval("print('danger')")
    exec("x = 1")
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Should detect both eval and exec
        eval_findings = [
            f for f in findings if f["rule_id"] == "SEC002" and "eval" in f["message"]
        ]
        exec_findings = [
            f for f in findings if f["rule_id"] == "SEC002" and "exec" in f["message"]
        ]

        self.assertEqual(len(eval_findings), 1)
        self.assertEqual(len(exec_findings), 1)
        self.assertEqual(eval_findings[0]["severity"], "error")
        self.assertIn("fix_suggestion", eval_findings[0])

    def test_detect_potential_secrets(self):
        """Test detection of potential hardcoded secrets"""
        code = """
password = "my_secret_password"
api_key = "sk-1234567890abcdef"
token = "auth_token_12345"
regular_string = "hello world"
short = "abc"
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        secret_findings = [f for f in findings if f["rule_id"] == "SEC001"]
        # Should detect password and api_key at minimum
        self.assertGreaterEqual(len(secret_findings), 2)

        for finding in secret_findings:
            self.assertEqual(finding["severity"], "warning")
            self.assertEqual(finding["category"], "security")
            self.assertIn("fix_suggestion", finding)

    def test_no_findings_clean_code(self):
        """Test that clean code produces no security findings"""
        code = """
def safe_function():
    print("Hello, world!")
    return 42
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        self.assertEqual(len(findings), 0)


class TestDeadCodeAnalyzer(TestCase):
    """Test DeadCodeAnalyzer functionality"""

    def setUp(self):
        """Initialize a DeadCodeAnalyzer instance before each test."""
        self.analyzer = DeadCodeAnalyzer()

    def test_detect_unused_functions(self):
        """Test detection of unused functions"""
        code = """
def used_function():
    return "used"

def unused_function():
    return "unused"

result = used_function()
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        unused_findings = [f for f in findings if "unused_function" in f["message"]]
        self.assertGreater(len(unused_findings), 0)

        for finding in unused_findings:
            self.assertEqual(finding["rule_id"], "DEAD001")
            self.assertEqual(finding["category"], "maintainability")
            self.assertIn("fix_suggestion", finding)

    def test_ignore_private_names(self):
        """Test that private names (starting with _) are ignored"""
        code = """
def _private_function():
    return "private"

_private_var = "private"
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Should not report private names as unused
        private_findings = [f for f in findings if "_private" in f["message"]]
        self.assertEqual(len(private_findings), 0)

    def test_used_definitions(self):
        """Test that used definitions are not reported"""
        code = """
def function_a():
    return function_b()

def function_b():
    return "result"

class MyClass:
    pass

instance = MyClass()
result = function_a()
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Should not report any of these as unused
        used_names = ["function_a", "function_b", "MyClass"]
        for name in used_names:
            unused_findings = [f for f in findings if name in f["message"]]
            self.assertEqual(
                len(unused_findings), 0, f"{name} should not be reported as unused"
            )


class TestCircularImportAnalyzer(TestCase):
    """Test CircularImportAnalyzer functionality"""

    def setUp(self):
        """Initialize a CircularImportAnalyzer instance before each test."""
        self.analyzer = CircularImportAnalyzer()

    def test_detect_potential_circular_imports(self):
        """Test detection of potential circular imports"""
        code = """
import module.submodule
from package.module import something
from .relative import item
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Should detect imports that might be circular (simplified heuristic)
        circular_findings = [f for f in findings if f["rule_id"] == "CIRC001"]

        for finding in circular_findings:
            self.assertEqual(finding["severity"], "warning")
            self.assertEqual(finding["category"], "design")
            self.assertIn("fix_suggestion", finding)

    def test_ignore_standard_library_imports(self):
        """Test that standard library imports are not flagged"""
        code = """
import os
import sys
import json
from pathlib import Path
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Standard library imports should not be flagged
        std_lib_findings = [
            f
            for f in findings
            if any(name in f["message"] for name in ["os", "sys", "json", "pathlib"])
        ]
        self.assertEqual(len(std_lib_findings), 0)


class TestDuplicateAnalyzer(TestCase):
    """Test DuplicateAnalyzer functionality"""

    def setUp(self):
        """Initialize a DuplicateAnalyzer instance before each test."""
        self.analyzer = DuplicateAnalyzer()

    def test_detect_duplicate_functions(self):
        """Test detection of duplicate function bodies"""
        code = """
def function_a():
    x = 1
    y = 2
    z = 3
    return x + y + z

def function_b():
    x = 1
    y = 2
    z = 3
    return x + y + z

def different_function():
    return "different"
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        duplicate_findings = [f for f in findings if f["rule_id"] == "DUP001"]
        self.assertGreater(len(duplicate_findings), 0)

        for finding in duplicate_findings:
            self.assertEqual(finding["severity"], "info")
            self.assertEqual(finding["category"], "maintainability")
            self.assertIn("fix_suggestion", finding)
            self.assertIn("function_a", finding["message"])
            self.assertIn("function_b", finding["message"])

    def test_ignore_small_functions(self):
        """Test that small functions are ignored"""
        code = """
def small_a():
    return 1

def small_b():
    return 1
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # Small functions should not be reported as duplicates
        self.assertEqual(len(findings), 0)

    def test_no_duplicates_different_functions(self):
        """Test that different functions are not flagged"""
        code = """
def function_a():
    x = 1
    y = 2
    z = 3
    return x + y + z

def function_b():
    a = 1
    b = 2
    c = 3
    return a * b * c
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        self.assertEqual(len(findings), 0)


class TestDocsAnalyzer(TestCase):
    """Test DocsAnalyzer functionality"""

    def setUp(self):
        """Initialize a DocsAnalyzer instance before each test."""
        self.analyzer = DocsAnalyzer()

    def test_detect_missing_function_docstrings(self):
        """Test detection of missing function docstrings"""
        code = """
def function_with_docstring():
    '''This function has a docstring'''
    return True

def function_without_docstring():
    return False
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        missing_docstring_findings = [f for f in findings if f["rule_id"] == "DOC001"]
        self.assertEqual(len(missing_docstring_findings), 1)

        finding = missing_docstring_findings[0]
        self.assertIn("function_without_docstring", finding["message"])
        self.assertEqual(finding["severity"], "info")
        self.assertEqual(finding["category"], "documentation")
        self.assertIn("fix_suggestion", finding)

    def test_detect_missing_class_docstrings(self):
        """Test detection of missing class docstrings"""
        code = """
class ClassWithDocstring:
    '''This class has a docstring'''
    pass

class ClassWithoutDocstring:
    pass
"""
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        missing_docstring_findings = [f for f in findings if f["rule_id"] == "DOC002"]
        self.assertEqual(len(missing_docstring_findings), 1)

        finding = missing_docstring_findings[0]
        self.assertIn("ClassWithoutDocstring", finding["message"])
        self.assertEqual(finding["severity"], "info")
        self.assertEqual(finding["category"], "documentation")

    def test_recognize_various_docstring_formats(self):
        """Test that various docstring formats are recognized"""
        code = '''
def function_with_single_quotes():
    'Single quote docstring'
    return True

def function_with_double_quotes():
    "Double quote docstring"
    return True

def function_with_triple_quotes():
    """Triple quote docstring"""
    return True

class ClassWithDocstring:
    """Class docstring"""
    pass
'''
        tree = ast.parse(code)
        findings = self.analyzer.analyze(tree, Path("test.py"), code)

        # None of these should be flagged as missing docstrings
        self.assertEqual(len(findings), 0)


class TestAnalyzerRegistry(TestCase):
    """Test the analyzer registry"""

    def test_all_analyzers_available(self):
        """Test that all expected analyzers are in the registry"""
        expected_analyzers = {
            "security": SecurityAnalyzer,
            "dead-code": DeadCodeAnalyzer,
            "circular": CircularImportAnalyzer,
            "duplicates": DuplicateAnalyzer,
            "docs": DocsAnalyzer,
        }

        self.assertEqual(len(AVAILABLE_ANALYZERS), len(expected_analyzers))

        for name, analyzer_class in expected_analyzers.items():
            self.assertIn(name, AVAILABLE_ANALYZERS)
            self.assertEqual(AVAILABLE_ANALYZERS[name], analyzer_class)

    def test_analyzer_instantiation(self):
        """Test that all analyzers can be instantiated"""
        for _, analyzer_class in AVAILABLE_ANALYZERS.items():
            analyzer = analyzer_class()
            self.assertIsInstance(analyzer, analyzer_class)

            # Test with custom profile
            analyzer_custom = analyzer_class(profile="comprehensive")
            self.assertEqual(analyzer_custom.profile, "comprehensive")

    def test_analyzer_interface(self):
        """Test that all analyzers implement the required interface"""
        for _, analyzer_class in AVAILABLE_ANALYZERS.items():
            analyzer = analyzer_class()

            # Should have analyze method
            self.assertTrue(hasattr(analyzer, "analyze"))
            self.assertTrue(callable(analyzer.analyze))

            # Should have profile attribute
            self.assertTrue(hasattr(analyzer, "profile"))
