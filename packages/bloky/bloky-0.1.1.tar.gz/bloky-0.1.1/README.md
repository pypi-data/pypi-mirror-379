# Bloky

A Python tool that analyzes Python code to detect blocking operations that could impact performance in async contexts.

## Features

- **Boto3 Detection**: Identifies synchronous boto3 client calls
- **Database Session Detection**: Finds usage of synchronous Session instead of AsyncSession
- **File Operations**: Detects blocking file I/O operations
- **Network Calls**: Identifies synchronous HTTP requests
- **Recursive Scanning**: Analyzes all Python files in directories and subdirectories
- **Detailed Reporting**: Provides comprehensive reports with code snippets

## Installation

### Install from source (development)

```bash
pip install -e .
```

### Install from PyPI (when published)

```bash
pip install bloky
```

## Usage

After installation, you can use the `bloky` command from anywhere:

### Analyze a directory

```bash
bloky /path/to/your/project
```

### Analyze a single file

```bash
bloky /path/to/file.py
```

### Save report to file

```bash
bloky /path/to/project --output blocking_report.txt
```

### Alternative: Run directly without installation

```bash
python main.py /path/to/your/project
```

## Detected Issues

The analyzer detects several types of blocking operations:

1. **boto3_sync_call**: Synchronous boto3 client calls
2. **potential_boto3_sync**: Potential boto3 operations
3. **sync_session_usage**: Using Session instead of AsyncSession
4. **sync_db_operation**: Synchronous database operations
5. **sync_file_operation**: Blocking file I/O
6. **sync_network_call**: Synchronous HTTP requests

## Example Output

```console
🚨 BLOCKING OPERATIONS DETECTED
==================================================

SUMMARY:
  boto3_sync_call: 2 occurrences
  sync_session_usage: 1 occurrences

BOTO3 SYNC CALL:
------------------------------
  📍 /path/to/file.py:15
     Synchronous boto3 client call detected
     Code: scheduler = get_boto_client("scheduler")
            target = {"Arn": arn, "Input": state_input, "RoleArn": role_arn}
            schedule = scheduler.create_schedule(

SYNC SESSION USAGE:
------------------------------
  📍 /path/to/file.py:45
     Using synchronous Session instead of AsyncSession
     Code: def playbook_list_get(
            self,
            request: Request,
            satori_db: Session,
```

## Examples of Detected Patterns

### Boto3 Synchronous Calls

```python
# This will be detected
scheduler = get_boto_client("scheduler")
schedule = scheduler.create_schedule(...)
```

### Database Session Issues

```python
# This will be detected - using Session instead of AsyncSession
def some_function(self, satori_db: Session):
    result = satori_db.query(Model).all()
```

### File Operations

```python
# This will be detected
with open('file.txt') as f:
    content = f.read()  # Blocking read operation
```

### Network Calls

```python
# This will be detected
import requests
response = requests.get('https://api.example.com')  # Blocking HTTP call
```
