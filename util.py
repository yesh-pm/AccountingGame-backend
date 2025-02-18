import random
import pandas as pd
from pathlib import Path


def read_excel(path: Path, sheet_name: str = None):
    return pd.read_excel(path, sheet_name=sheet_name)


def generate_random_numbers(target_sum, count):
    numbers = sorted(
        [random.randint(1, target_sum - count + 1) for _ in range(count - 1)]
    )
    numbers = [0] + numbers + [target_sum]
    return [numbers[i + 1] - numbers[i] for i in range(count)]
