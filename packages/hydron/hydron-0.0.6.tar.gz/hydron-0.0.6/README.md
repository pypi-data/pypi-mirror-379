# **hydron**
Python interface for launching and post-processing SWMF magnetohydrodynamic simulations

## Installation
All examples assume the use of `uv`.
### Express
For when you're using the package just for analysis.
```bash
uv pip install hydron
```

### Developer
For when you are developing a project of your own and are trying to add `hydron` as a dependency.
```bash
uv add hydron
```

## Contributor Guide
Contributors are expected to be using `uv`.
Please fork `hydron` and submit your changes in a pull request.
The following are some common workflows.

### Testing
```bash
    uv run --extra test pytest
```

### Previewing Documentation
```bash
    uv run --extra docs myst start
```
