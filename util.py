import pandas as pd
from pathlib import Path


def read_excel(path: Path, sheet_name: str = None):
    return pd.read_excel(path, sheet_name=sheet_name)
