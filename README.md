# AccountingGame-backend

## Dependency Installation Guide

### Using PDM (Recommended)

If you have **PDM** installed, you can install dependencies directly using:

```

pdm install
```

This will install all dependencies as specified in `pyproject.toml`.

If you don't have PDM installed, you can install it via:

```
pip install pdm
```

------

## Using pip (Without PDM)

If you prefer to use `pip`, you can install dependencies from `requirements.txt`:

pip install -r requirements.txt

## Notes

- If you are using **PDM**, `pdm install` will automatically create and manage a virtual environment.
- requirements.txt may be out of date, so pdm is always better.
