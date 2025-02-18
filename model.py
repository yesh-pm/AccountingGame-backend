from pydantic import BaseModel


class GetRandomNBElementsRequest(BaseModel):
    num: int


class NormalBalanceElements(BaseModel):
    name: str
    type: str
