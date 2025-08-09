---
title: Python Development Best Practices
date: 2025-08-06
tags: [python, best-practices, development, code-quality]
excerpt: Essential best practices for Python development that will help you write cleaner, more maintainable, and more professional code.
---

# Python Development Best Practices

After years of Python development, I've compiled a list of best practices that consistently lead to better, more maintainable code. These practices have served me well across different projects and team sizes.

## Code Organization and Structure

### Use Clear Project Structure

Organize your project with a clear, predictable structure:

```
my_project/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       ├── utils/
│       └── tests/
├── docs/
├── pyproject.toml
└── README.md
```

### Follow PEP 8

Use `ruff` or `black` to automatically format your code:

```bash
# Using ruff (recommended)
ruff format .
ruff check .

# Using black
black .
```

## Dependency Management

### Use Modern Tools

Embrace modern Python tooling like `uv` for dependency management:

```bash
# Initialize project
uv init my-project

# Add dependencies
uv add requests
uv add --dev pytest

# Install dependencies
uv sync
```

### Pin Your Dependencies

Always specify version ranges in your `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests>=2.28.0,<3.0.0",
    "pydantic>=2.0.0,<3.0.0",
]
```

## Code Quality

### Write Comprehensive Docstrings

Use consistent docstring formats (I prefer the "requests" style):

```python
def process_data(data: list[dict], threshold: float = 0.5) -> list[dict]:
    """Process a list of data dictionaries based on a threshold.
    
    Args:
        data: List of dictionaries containing data to process
        threshold: Minimum value for inclusion in results
        
    Returns:
        Filtered and processed list of dictionaries
        
    Raises:
        ValueError: If threshold is not between 0 and 1
    """
    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1")
    
    return [item for item in data if item.get("score", 0) >= threshold]
```

### Use Type Hints Everywhere

Modern Python should include type hints:

```python
from typing import Any, Dict, List, Optional
from datetime import datetime

def load_config(path: str) -> Dict[str, Any]:
    """Load configuration from file."""
    # Implementation here
    pass

def process_items(
    items: List[Dict[str, Any]], 
    created_after: Optional[datetime] = None
) -> List[Dict[str, Any]]:
    """Process items with optional date filtering."""
    # Implementation here
    pass
```

### Embrace Error Handling

Be explicit about error handling:

```python
from pathlib import Path
import json

def load_json_file(file_path: str) -> dict[str, Any]:
    """Load JSON data from file with proper error handling."""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {file_path}: {e}")
    except Exception as e:
        raise RuntimeError(f"Failed to load {file_path}: {e}")
```

## Testing

### Write Tests from the Start

Don't wait to add tests. Start with basic tests and expand:

```python
import pytest
from my_package.utils import process_data

def test_process_data_filters_by_threshold():
    """Test that process_data correctly filters by threshold."""
    data = [
        {"name": "item1", "score": 0.8},
        {"name": "item2", "score": 0.3},
        {"name": "item3", "score": 0.7},
    ]
    
    result = process_data(data, threshold=0.5)
    
    assert len(result) == 2
    assert result[0]["name"] == "item1"
    assert result[1]["name"] == "item3"

def test_process_data_invalid_threshold():
    """Test that invalid thresholds raise ValueError."""
    with pytest.raises(ValueError, match="Threshold must be between 0 and 1"):
        process_data([], threshold=1.5)
```

### Use pytest Configuration

Create a `pytest.ini` or add to `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
```

## Performance and Optimization

### Profile Before Optimizing

Use `cProfile` to understand where time is spent:

```python
import cProfile
import pstats

def profile_function():
    # Your code here
    pass

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    profile_function()
    pr.disable()
    
    stats = pstats.Stats(pr)
    stats.sort_stats('cumulative').print_stats(10)
```

### Use Appropriate Data Structures

Choose the right tool for the job:

```python
# For membership testing, use sets
valid_ids = {1, 2, 3, 4, 5}
if user_id in valid_ids:  # O(1) lookup
    process_user()

# For ordered data with frequent lookups, use dict
user_lookup = {user.id: user for user in users}

# For FIFO operations, use collections.deque
from collections import deque
queue = deque()
queue.appendleft(item)  # O(1)
item = queue.pop()      # O(1)
```

## Security

### Validate Input

Never trust user input:

```python
from pathlib import Path

def safe_file_access(filename: str, base_dir: str) -> Path:
    """Safely access files within a base directory."""
    base_path = Path(base_dir).resolve()
    file_path = (base_path / filename).resolve()
    
    # Prevent directory traversal
    if not str(file_path).startswith(str(base_path)):
        raise ValueError("Access denied: path outside base directory")
    
    return file_path
```

### Use Environment Variables for Secrets

Never hardcode secrets:

```python
import os
from typing import Optional

def get_database_url() -> str:
    """Get database URL from environment variables."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL environment variable not set")
    return url

# In production, use more sophisticated secret management
def get_secret(key: str, default: Optional[str] = None) -> str:
    """Get secret from environment with fallback."""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Required secret '{key}' not found")
    return value
```

## Final Thoughts

These practices have evolved over time and continue to serve me well. The key is consistency - establish patterns early and stick to them across your codebase.

Remember:
- Code is read more often than it's written
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

What are your favorite Python development practices? I'd love to hear about them!