"""Blocking Analyzer - Detects blocking operations in Python code.

This tool analyzes Python files to identify potential blocking operations
that could impact performance in async contexts.
"""

import argparse
import ast
import sys
from pathlib import Path


class BlockingIssue:
    """Represents a detected blocking issue."""

    def __init__(
        self,
        file_path: str,
        line_number: int,
        issue_type: str,
        description: str,
        code_snippet: str = "",
    ):
        self.file_path = file_path
        self.line_number = line_number
        self.issue_type = issue_type
        self.description = description
        self.code_snippet = code_snippet

    def __str__(self):
        return f"{self.file_path}:{self.line_number} - {self.issue_type}: {self.description}"


class BlockingAnalyzer(ast.NodeVisitor):
    """AST visitor that detects blocking operations in Python code."""

    def __init__(self, file_path: str, source_code: str):
        self.file_path = file_path
        self.source_code = source_code
        self.source_lines = source_code.splitlines()
        self.issues: list[BlockingIssue] = []
        self.current_function = None
        self.current_class = None
        self.imports = {}

    def visit_Import(self, node: ast.Import):
        """Track import statements."""
        for alias in node.names:
            self.imports[alias.name] = alias.asname or alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Track from imports."""
        if node.module:
            for alias in node.names:
                self.imports[alias.name] = f"{node.module}.{alias.name}"
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Visit function definitions."""
        old_function = self.current_function
        self.current_function = node.name
        self.generic_visit(node)
        self.current_function = old_function

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Visit async function definitions."""
        old_function = self.current_function
        self.current_function = node.name
        self.generic_visit(node)
        self.current_function = old_function

    def visit_ClassDef(self, node: ast.ClassDef):
        """Visit class definitions."""
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_Call(self, node: ast.Call):
        """Detect blocking function calls."""
        self._check_boto3_calls(node)
        self._check_database_calls(node)
        self._check_file_operations(node)
        self._check_network_calls(node)
        self.generic_visit(node)

    def _check_boto3_calls(self, node: ast.Call):
        """Check for synchronous boto3 calls."""
        if isinstance(node.func, ast.Attribute):
            # Check for boto3 client calls like get_boto_client("scheduler")
            if isinstance(node.func.value, ast.Call):
                if isinstance(node.func.value.func, ast.Attribute):
                    if isinstance(
                        node.func.value.func.value, ast.Name
                    ) and node.func.value.func.value.id in ["boto3", "get_boto_client"]:
                        self._add_issue(
                            node.lineno,
                            "boto3_sync_call",
                            "Synchronous boto3 client call detected",
                            self._get_code_snippet(node.lineno),
                        )
                elif isinstance(node.func.value.func, ast.Name):
                    if node.func.value.func.id in ["boto3", "get_boto_client"]:
                        self._add_issue(
                            node.lineno,
                            "boto3_sync_call",
                            "Synchronous boto3 client call detected",
                            self._get_code_snippet(node.lineno),
                        )

            # Check for direct boto3 method calls on client objects
            if isinstance(node.func.value, ast.Name):
                if node.func.value.id in [
                    "scheduler",
                    "s3",
                    "dynamodb",
                    "lambda",
                    "s3_client",
                ]:
                    # This could be a boto3 client
                    self._add_issue(
                        node.lineno,
                        "potential_boto3_sync",
                        f"Potential synchronous boto3 call: {node.func.value.id}.{node.func.attr}",
                        self._get_code_snippet(node.lineno),
                    )

            # Check for boto3 resource calls like boto3.resource('dynamodb')
            if isinstance(node.func.value, ast.Call):
                if isinstance(node.func.value.func, ast.Attribute):
                    if (
                        isinstance(node.func.value.func.value, ast.Name)
                        and node.func.value.func.value.id == "boto3"
                        and node.func.value.func.attr == "resource"
                    ):
                        self._add_issue(
                            node.lineno,
                            "boto3_sync_call",
                            "Synchronous boto3 resource call detected",
                            self._get_code_snippet(node.lineno),
                        )

            # Check for method calls on boto3 resource objects
            if isinstance(node.func.value, ast.Attribute):
                if isinstance(node.func.value.value, ast.Name):
                    if node.func.value.value.id in ["dynamodb", "table"]:
                        self._add_issue(
                            node.lineno,
                            "potential_boto3_sync",
                            f"Potential synchronous boto3 resource call: {node.func.value.value.id}.{node.func.value.attr}.{node.func.attr}",
                            self._get_code_snippet(node.lineno),
                        )

    def _check_database_calls(self, node: ast.Call):
        """Check for synchronous database operations."""
        if isinstance(node.func, ast.Attribute):
            # Check for Session instead of AsyncSession
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "satori_db"
                and isinstance(node.func.value, ast.Name)
            ):
                # Check if this is a Session parameter
                if self._is_session_parameter(node.func.value.id):
                    self._add_issue(
                        node.lineno,
                        "sync_session_usage",
                        "Using synchronous Session instead of AsyncSession",
                        self._get_code_snippet(node.lineno),
                    )

            # Check for common blocking database operations
            blocking_db_methods = [
                "query",
                "filter",
                "all",
                "first",
                "one",
                "one_or_none",
                "scalar",
                "execute",
                "commit",
                "rollback",
                "close",
            ]

            if node.func.attr in blocking_db_methods:
                if isinstance(node.func.value, ast.Name):
                    if (
                        "session" in node.func.value.id.lower()
                        or "db" in node.func.value.id.lower()
                    ):
                        self._add_issue(
                            node.lineno,
                            "sync_db_operation",
                            f"Synchronous database operation: {node.func.attr}",
                            self._get_code_snippet(node.lineno),
                        )

    def _check_file_operations(self, node: ast.Call):
        """Check for blocking file operations."""
        if isinstance(node.func, ast.Attribute):
            blocking_file_methods = [
                "read",
                "write",
                "readlines",
                "writelines",
                "flush",
            ]

            if node.func.attr in blocking_file_methods:
                # Check for file operations on file objects
                if isinstance(node.func.value, ast.Name):
                    # This could be a file object
                    self._add_issue(
                        node.lineno,
                        "sync_file_operation",
                        f"Synchronous file operation: {node.func.attr}",
                        self._get_code_snippet(node.lineno),
                    )
                # Also check for file operations in with statements context
                elif isinstance(node.func.value, ast.Name):
                    self._add_issue(
                        node.lineno,
                        "sync_file_operation",
                        f"Synchronous file operation: {node.func.attr}",
                        self._get_code_snippet(node.lineno),
                    )

    def _check_network_calls(self, node: ast.Call):
        """Check for blocking network operations."""
        if isinstance(node.func, ast.Attribute):
            blocking_network_methods = [
                "get",
                "post",
                "put",
                "delete",
                "patch",
                "request",
            ]

            if node.func.attr in blocking_network_methods:
                if isinstance(node.func.value, ast.Name):
                    if node.func.value.id in ["requests", "urllib"]:
                        self._add_issue(
                            node.lineno,
                            "sync_network_call",
                            f"Synchronous network call: {node.func.attr}",
                            self._get_code_snippet(node.lineno),
                        )

    def _is_session_parameter(self, param_name: str) -> bool:
        """Check if a parameter is likely a database session."""
        session_keywords = ["session", "db", "database"]
        return any(keyword in param_name.lower() for keyword in session_keywords)

    def _add_issue(
        self,
        line_number: int,
        issue_type: str,
        description: str,
        code_snippet: str = "",
    ):
        """Add a blocking issue to the list."""
        issue = BlockingIssue(
            self.file_path, line_number, issue_type, description, code_snippet
        )
        self.issues.append(issue)

    def _get_code_snippet(self, line_number: int, context_lines: int = 2) -> str:
        """Get code snippet around the given line number."""
        start = max(0, line_number - context_lines - 1)
        end = min(len(self.source_lines), line_number + context_lines)
        return "\n".join(self.source_lines[start:end])


class FileScanner:
    """Scans directories for Python files."""

    def __init__(self, root_path: str):
        self.root_path = Path(root_path)

    def scan_python_files(self) -> list[Path]:
        """Recursively find all Python files."""
        python_files = []
        for file_path in self.root_path.rglob("*.py"):
            # Skip __pycache__ directories
            if "__pycache__" not in str(file_path):
                python_files.append(file_path)
        return python_files


class ReportGenerator:
    """Generates analysis reports."""

    def __init__(self):
        self.all_issues: list[BlockingIssue] = []

    def add_issues(self, issues: list[BlockingIssue]):
        """Add issues to the report."""
        self.all_issues.extend(issues)

    def generate_report(self) -> str:
        """Generate a comprehensive report."""
        if not self.all_issues:
            return "✅ No blocking operations detected!"

        report = []
        report.append("🚨 BLOCKING OPERATIONS DETECTED")
        report.append("=" * 50)
        report.append("")

        # Group issues by type
        issues_by_type = {}
        for issue in self.all_issues:
            if issue.issue_type not in issues_by_type:
                issues_by_type[issue.issue_type] = []
            issues_by_type[issue.issue_type].append(issue)

        # Summary
        report.append("SUMMARY:")
        for issue_type, issues in issues_by_type.items():
            report.append(f"  {issue_type}: {len(issues)} occurrences")
        report.append("")

        # Detailed issues
        for issue_type, issues in issues_by_type.items():
            report.append(f"{issue_type.upper().replace('_', ' ')}:")
            report.append("-" * 30)

            for issue in issues:
                report.append(f"  📍 {issue.file_path}:{issue.line_number}")
                report.append(f"     {issue.description}")
                if issue.code_snippet:
                    report.append(f"     Code: {issue.code_snippet.strip()}")
                report.append("")

        return "\n".join(report)


def analyze_file(file_path: Path) -> list[BlockingIssue]:
    """Analyze a single Python file for blocking operations."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        tree = ast.parse(source_code, filename=str(file_path))
        analyzer = BlockingAnalyzer(str(file_path), source_code)
        analyzer.visit(tree)

        return analyzer.issues
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return []


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze Python code for blocking operations"
    )
    parser.add_argument("path", help="Path to analyze (file or directory)")
    parser.add_argument("--output", "-o", help="Output file for the report")

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Error: Path '{path}' does not exist")
        sys.exit(1)

    # Determine if it's a file or directory
    if path.is_file():
        if path.suffix != ".py":
            print(f"Error: File '{path}' is not a Python file")
            sys.exit(1)
        python_files = [path]
    else:
        scanner = FileScanner(path)
        python_files = scanner.scan_python_files()

    if not python_files:
        print("No Python files found to analyze")
        sys.exit(0)

    print(f"Analyzing {len(python_files)} Python files...")

    report_generator = ReportGenerator()

    for file_path in python_files:
        print(f"Analyzing: {file_path}")
        issues = analyze_file(file_path)
        report_generator.add_issues(issues)

    report = report_generator.generate_report()

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
