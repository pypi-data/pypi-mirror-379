# Panel Print

A Python library that provides beautiful console output using Rich panels for enhanced debugging and data visualization.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.1-brightgreen.svg)](https://github.com/yourusername/panel-print)

## Features

- 🎨 **Beautiful Output**: Pretty print objects in elegant Rich panels
- � **DataFrame Display**: Interactive pandas DataFrame and Series visualization with `show`
- 🀽� **Easy to Use**: Simple API with intuitive functions
- 🔧 **Customizable**: Configurable max length for container abbreviation
- 🚀 **Fast**: Built on top of the powerful Rich library and itables
- 🐍 **Modern Python**: Supports Python 3.10+

## Installation

Install using pip:

```bash
pip install panel-print
```

Or using uv:

```bash
uv add panel-print
```

## Quick Start

```python
from panel_print import pp, show
import pandas as pd

# Pretty print any Python object
data = {
    "name": "John Doe", 
    "age": 30,
    "skills": ["Python", "JavaScript", "Go"],
    "address": {
        "street": "123 Main St",
        "city": "San Francisco",
        "state": "CA"
    }
}

pp(data)

# Display pandas DataFrame/Series interactively
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

show(df)  # Interactive table display
```

## Usage Examples

### Basic Usage

```python
from panel_print import pp

# Print simple values
pp("Hello, World!")
pp(42)
pp([1, 2, 3, 4, 5])
```

### Multiple Objects

```python
from panel_print import pp

# Print multiple objects at once
pp("User Info:", {"name": "Alice", "age": 25}, ["admin", "user"])
```

### Custom Max Length

```python
from panel_print import pp

# Control container abbreviation
long_list = list(range(100))
pp(long_list, max_length=10)  # Will abbreviate after 10 items
```

### Complex Data Structures

```python
from panel_print import pp

# Works great with nested data
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "features": ["auth", "logging", "caching"],
    "debug": True
}

pp(config)
```

### Pandas DataFrame and Series Display

```python
from panel_print import show
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [999.99, 25.50, 79.99, 299.00],
    'Stock': [15, 100, 50, 8],
    'Rating': [4.5, 4.2, 4.7, 4.1]
})

# Interactive table display with search, sort, and export features
show(df)

# Works with Series too
series = pd.Series([1, 2, 3, 4, 5], name='Numbers')
show(series)

# Large datasets with automatic pagination
large_df = pd.DataFrame(np.random.randn(1000, 5), 
                       columns=['A', 'B', 'C', 'D', 'E'])
show(large_df)  # Automatically handles large data
```

### Integration with Rich

```python
from panel_print import print, pprint

# Access Rich's print and pprint directly
print("This uses Rich's enhanced print")
pprint({"key": "value"})  # Rich's pretty print without panels
```

## API Reference

### `pp(*objects, max_length=20)`

Pretty print objects in a panel format.

**Parameters:**

- `*objects` (Any): One or more objects to pretty print
- `max_length` (int, optional): Maximum length of containers before abbreviating. Defaults to 20.

**Returns:**

- None

**Example:**

```python
pp(data, max_length=50)
```

### `show(df, **kwargs)`

Display pandas DataFrame or Series in an interactive table format with search, sorting, and export capabilities.

**Parameters:**

- `df` (pd.DataFrame | pd.Series): The pandas DataFrame or Series to display
- `**kwargs`: Additional keyword arguments passed to itables.show()

**Features:**

- Interactive search and column filtering
- Sortable columns
- Export to CSV, Excel, and HTML
- Automatic pagination for large datasets
- Responsive design
- Index display control

**Returns:**

- None (displays interactive table in notebook/browser)

**Example:**

```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
show(df)
```

## Advanced Usage

### Debugging Complex Objects

```python
from panel_print import pp
import datetime

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.datetime.now()
  
    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"

user = User("Alice", "alice@example.com")
pp("Debug User Object:", user, user.__dict__)
```

### Working with APIs

```python
import requests
from panel_print import pp

response = requests.get("https://api.github.com/users/octocat")
pp("GitHub API Response:", response.json())
```

### Data Analysis Workflow

```python
import pandas as pd
from panel_print import pp, show

# Load and explore data
df = pd.read_csv("sales_data.csv")

# Quick overview with pp
pp("Dataset Info:", {
    "Shape": df.shape,
    "Columns": list(df.columns),
    "Memory Usage": f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
})

# Interactive data exploration with show
show(df.head(20))  # First 20 rows with interactive features
show(df.describe())  # Statistical summary
show(df.groupby('category').sum())  # Grouped analysis
```

## Requirements

- Python 3.10 or higher
- Rich >= 14.1.0
- itables (for pandas DataFrame/Series display)
- pandas (optional, required for DataFrame/Series functionality)

## Development

### Setting up Development Environment

1. Clone the repository:

```bash
git clone https://github.com/yourusername/panel-print.git
cd panel-print
```

2. Install dependencies using uv:

```bash
uv sync
```

3. Run tests:

```bash
uv run pytest
```

### Building the Package

```bash
uv build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) - Python library for rich text and beautiful formatting
- Inspired by the need for better debugging output in Python applications

## Changelog

### v0.1.2

- Added `show` function for interactive pandas DataFrame and Series display
- Integrated itables for enhanced data visualization
- Added search, sort, and export capabilities for tabular data
- Improved data analysis workflow support

### v0.1.0

- Initial release
- Basic panel printing functionality
- Support for multiple objects
- Configurable max length parameter

---

Made with ❤️ for the Python community
