# uv-job

Simple task runner for uv.

> [!IMPORTANT]  
> After creating this project I discovered [taskipy](https://pypi.org/project/taskipy/) which does exactly the same thing. So you should use that instead.
> 
> ```bash
> uv add --dev taskipy 
> ```
> 
> ```toml
> [tool.taskipy.tasks]
> tests = "pytest -v"
> ```
> 
> ```bash
> uv run task test
> ```

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
