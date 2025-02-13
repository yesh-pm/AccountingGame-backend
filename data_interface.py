from typing import List
import pandas as pd
from pathlib import Path


class ExcelDataInterface:
    def __init__(self, filename: Path, sheet_names: List[str] = None):
        self.filename = filename
        self.data = pd.read_excel(self.filename, sheet_name=sheet_names)

    def get_data(self, sheet_name: str):
        return self.data[sheet_name]

    @property
    def get_credits_elements(self):
        sheet = self.get_data("Normal Balance")
        return sheet.iloc[:, 1].dropna().tolist()

    @property
    def get_debits_elements(self):
        sheet = self.get_data("Normal Balance")
        return sheet.iloc[:, 0].dropna().tolist()


account_elements = ExcelDataInterface(
    Path(__file__).parent / "data" / "Accounting Elements for Game.xlsx",
    ["Normal Balance"],
)


if __name__ == "__main__":
    print(account_elements.get_credits_elements())
    print(account_elements.get_debits_elements())
