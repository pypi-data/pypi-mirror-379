# uv-job

Simple task runner for uv.

## Installation

```bash
uv add --dev uv-job
```

## Configuration

```toml
# pyproject.toml
# ...

[tool.jobs]
test = "pytest -v"
```

## Usage

```bash
uv run job test
```
