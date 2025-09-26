"""DinoScan Analyzers - Individual code analysis modules"""

import ast
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Type


class BaseAnalyzer(ABC):
    """Base class for all analyzers"""

    def __init__(self, profile: str = "standard"):
        self.profile = profile

    @abstractmethod
    def analyze(
        self, tree: ast.AST, file_path: Path, content: str
    ) -> List[Dict[str, Any]]:
        """Analyze the AST and return findings"""


class SecurityAnalyzer(BaseAnalyzer):
    """Security vulnerability analyzer"""

    def analyze(
        self, tree: ast.AST, file_path: Path, content: str
    ) -> List[Dict[str, Any]]:
        """Analyze the AST tree and detect security vulnerabilities such as
        hardcoded secrets and dangerous calls.
        """
        findings = []

        class SecurityVisitor(ast.NodeVisitor):
            """AST visitor that detects hardcoded secrets in string literals and dangerous
            function calls."""

            def visit_Constant(self, node: ast.Constant):
                """Visit Constant nodes and detect potential secrets in string
                literals.
                """
                if isinstance(node.value, str):
                    self._maybe_record_string(node.value, node)
                self.generic_visit(node)

            def visit_Call(self, node):
                """Visit function call nodes and record dangerous
                calls like eval or exec.
                """
                # Check for dangerous function calls
                if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec"]:
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": node.lineno,
                            "column": node.col_offset,
                            "severity": "error",
                            "message": f"Dangerous function call: {node.func.id}",
                            "rule_id": "SEC002",
                            "analyzer": "security",
                            "category": "security",
                            "fix_suggestion": (
                                f"Replace {node.func.id}()"
                                " with safer alternatives or validate input "
                                "thoroughly"
                            ),
                        }
                    )
                self.generic_visit(node)

            def _maybe_record_string(self, value: str, node: ast.AST) -> None:
                """Check if a string value is a potential secret and record a
                finding if so.
                """
                if self._is_potential_secret(value):
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": getattr(node, "lineno", 1),
                            "column": getattr(node, "col_offset", 0),
                            "severity": "warning",
                            "message": "Potential hardcoded secret detected",
                            "rule_id": "SEC001",
                            "analyzer": "security",
                            "category": "security",
                            "fix_suggestion": (
                                "Move secrets to environment variables or "
                                "secure configuration files"
                            ),
                        }
                    )

            @staticmethod
            def _is_potential_secret(value: str) -> bool:
                """Check if value looks like a secret"""
                if not isinstance(value, str):
                    return False
                if len(value) < 8:
                    return False
                # Simple heuristics for secrets (expandable)
                secret_patterns: List[str] = [
                    r"password",
                    r"secret",
                    r"api[_-]?key",
                    r"auth[_-]?token",
                    r"access[_-]?key",
                ]
                return any(
                    re.search(pattern, value, re.IGNORECASE)
                    for pattern in secret_patterns
                )

        visitor = SecurityVisitor()
        visitor.visit(tree)
        return findings


class DeadCodeAnalyzer(BaseAnalyzer):
    """Dead code analyzer"""

    def analyze(
        self, tree: ast.AST, file_path: Path, content: str
    ) -> List[Dict[str, Any]]:
        """Analyze AST for unused definitions in the given file content.

        Performs two AST visits to collect defined and used names and
        returns findings for unused definitions.
        """
        findings = []
        defined_names = set()
        used_names = set()

        class DefinitionVisitor(ast.NodeVisitor):
            """
            AST visitor that collects all defined names (functions, classes,
            and assignments) from the syntax tree.
            """

            def visit_FunctionDef(self, node):
                """Record function definition names to defined_names set."""
                defined_names.add(node.name)
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                """Record class definition names to defined_names set."""
                defined_names.add(node.name)
                self.generic_visit(node)

            def visit_Assign(self, node):
                """Record assigned names to defined_names set."""
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        defined_names.add(target.id)
                self.generic_visit(node)

        class UsageVisitor(ast.NodeVisitor):
            """AST node visitor that records usage of variable names in load
            contexts.
            """

            def visit_Name(self, node):
                """Record usage of names in load context to used_names set."""
                if isinstance(node.ctx, ast.Load):
                    used_names.add(node.id)
                self.generic_visit(node)

        # Find definitions and usages
        def_visitor = DefinitionVisitor()
        def_visitor.visit(tree)

        usage_visitor = UsageVisitor()
        usage_visitor.visit(tree)

        # Find unused definitions
        unused = defined_names - used_names

        # Add findings for unused definitions (simplified)
        for name in unused:
            if not name.startswith("_"):  # Ignore private names
                findings.append(
                    {
                        "file": str(file_path),
                        "line": 1,  # Simplified - would need more complex tracking
                        "column": 1,
                        "severity": "info",
                        "message": f"Potentially unused definition: {name}",
                        "rule_id": "DEAD001",
                        "analyzer": "dead-code",
                        "category": "maintainability",
                        "fix_suggestion": (
                            f"Remove unused definition '{name}' or add usage "
                            "if it's intended for external use"
                        ),
                    }
                )

        return findings


class CircularImportAnalyzer(BaseAnalyzer):
    """Circular import analyzer"""

    def analyze(
        self, tree: ast.AST, file_path: Path, content: str
    ) -> List[Dict[str, Any]]:
        """Analyze the AST of a file to detect circular import
        patterns and return findings.
        """
        findings = []

        class ImportVisitor(ast.NodeVisitor):
            """AST visitor that traverses import statements to detect potential
            circular imports and records findings.
            """

            def visit_Import(self, node):
                """Visit import statements and record potential circular imports."""
                for alias in node.names:
                    # Simplified circular import detection
                    module_name = alias.name
                    if ImportVisitor._might_be_circular(module_name, file_path):
                        findings.append(
                            {
                                "file": str(file_path),
                                "line": node.lineno,
                                "column": node.col_offset,
                                "severity": "warning",
                                "message": (
                                    f"Potential circular import: {module_name}"
                                ),
                                "rule_id": "CIRC001",
                                "analyzer": "circular",
                                "category": "design",
                                "fix_suggestion": (
                                    "Refactor to break circular dependency "
                                    f"with {module_name}"
                                ),
                            }
                        )
                self.generic_visit(node)

            def visit_ImportFrom(self, node):
                """
                Visit from-import statements and record potential circular
                imports.
                """
                if node.module and ImportVisitor._might_be_circular(
                    node.module, file_path
                ):
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": node.lineno,
                            "column": node.col_offset,
                            "severity": "warning",
                            "message": (f"Potential circular import: {node.module}"),
                            "rule_id": "CIRC001",
                            "analyzer": "circular",
                            "category": "design",
                            "fix_suggestion": (
                                "Refactor to break circular dependency with "
                                f"{node.module}"
                            ),
                        }
                    )
                self.generic_visit(node)

            @staticmethod
            def _might_be_circular(module_name: str, current_file: Path) -> bool:
                """Simplified circular import detection"""
                # Very basic heuristic - check if importing from same directory
                return "." in module_name and not module_name.startswith(".")

        visitor = ImportVisitor()
        visitor.visit(tree)
        return findings


class DuplicateAnalyzer(BaseAnalyzer):
    """Code duplication analyzer"""

    def analyze(
        self,
        tree: ast.AST,
        file_path: Path,
        content: str,
    ) -> List[Dict[str, Any]]:
        """Analyze the AST tree for duplicate function bodies and
        return a list of findings.
        """
        findings = []

        # Simplified duplicate detection - look for identical function bodies
        functions = []

        class FunctionVisitor(ast.NodeVisitor):
            """Visits function definitions to identify and collect
            substantial functions for duplication analysis.
            """

            def visit_FunctionDef(self, node):
                """Visit each function definition node to collect substantial
                function bodies for duplication analysis.
                """
                # Get function body as string (simplified)
                body_nodes = [ast.dump(stmt) for stmt in node.body]
                if len(body_nodes) > 3:  # Only check substantial functions
                    functions.append((node.name, body_nodes, node.lineno))
                self.generic_visit(node)

        visitor = FunctionVisitor()
        visitor.visit(tree)

        # Check for duplicates
        for i, (name1, body1, line1) in enumerate(functions):
            for _, (name2, body2, _) in enumerate(functions[i + 1 :], i + 1):
                if body1 == body2:
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": line1,
                            "column": 1,
                            "severity": "info",
                            "message": (
                                f"Duplicate function body detected: {name1} and {name2}"
                            ),
                            "rule_id": "DUP001",
                            "analyzer": "duplicates",
                            "category": "maintainability",
                            "fix_suggestion": (
                                "Extract common functionality into a shared function "
                                f"to reduce duplication between {name1} and {name2}"
                            ),
                        }
                    )

        return findings


class DocsAnalyzer(BaseAnalyzer):
    """Documentation analyzer"""

    def analyze(
        self, tree: ast.AST, file_path: Path, content: str
    ) -> List[Dict[str, Any]]:
        """Analyze the AST of a Python file to collect findings for missing
        docstrings.
        """
        findings = []

        class DocstringVisitor(ast.NodeVisitor):
            """Visitor that checks AST nodes for missing docstrings
            on functions and classes.
            """

            def visit_FunctionDef(self, node):
                """Visit a function definition and record a finding
                if it lacks a docstring.
                """
                if not self._has_docstring(node):
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": node.lineno,
                            "column": node.col_offset,
                            "severity": "info",
                            "message": (f"Function '{node.name}' missing docstring"),
                            "rule_id": "DOC001",
                            "analyzer": "docs",
                            "category": "documentation",
                            "fix_suggestion": (
                                f"Add docstring to function '{node.name}' describing "
                                "its purpose, parameters, and return value"
                            ),
                        }
                    )
                self.generic_visit(node)

            def visit_ClassDef(self, node):
                """Visit a class definition and record a finding if it lacks a
                docstring.
                """
                if not self._has_docstring(node):
                    findings.append(
                        {
                            "file": str(file_path),
                            "line": node.lineno,
                            "column": node.col_offset,
                            "severity": "info",
                            "message": f"Class '{node.name}' missing docstring",
                            "rule_id": "DOC002",
                            "analyzer": "docs",
                            "category": "documentation",
                            "fix_suggestion": (
                                f"Add docstring to class '{node.name}' "
                                "describing its purpose and usage"
                            ),
                        }
                    )
                self.generic_visit(node)

            @staticmethod
            def _has_docstring(node) -> bool:
                """Check if node has a docstring"""
                if not node.body:
                    return False
                first_stmt = node.body[0]
                if not isinstance(first_stmt, ast.Expr):
                    return False

                value = first_stmt.value

                # For Python 3.8+, ast.Constant is used for all literals
                if isinstance(value, ast.Constant):
                    return isinstance(value.value, str)

                # For older Python versions, check for ast.Str
                # Note: ast.Str was removed in Python 3.12 but exists in 3.8-3.11
                try:
                    # Use dynamic attribute access to avoid issues when ast.Str doesn't exist
                    str_type = getattr(ast, "Str", None)
                    if str_type and isinstance(value, str_type):
                        return True
                except (AttributeError, TypeError):
                    # Expected when ast.Str doesn't exist in Python 3.12+
                    pass

                return False

        # Continue implementation...
        visitor = DocstringVisitor()
        visitor.visit(tree)
        return findings


# Registry of available analyzers
AVAILABLE_ANALYZERS: Dict[str, Type[BaseAnalyzer]] = {
    "security": SecurityAnalyzer,
    "dead-code": DeadCodeAnalyzer,
    "circular": CircularImportAnalyzer,
    "duplicates": DuplicateAnalyzer,
    "docs": DocsAnalyzer,
}
