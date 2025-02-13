from pydantic import BaseModel


class NormalBalanceElements(BaseModel):
    name: str
    type: str
