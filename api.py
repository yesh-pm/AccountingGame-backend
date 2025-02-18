import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from setting import WebSetting
from data_interface import account_elements
from model import NormalBalanceElements, GetRandomNBElementsRequest

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3141",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(WebSetting.api_base.value, app)


@app.post("/get_random_nb_elements")
async def get_random_nb_elements(request: GetRandomNBElementsRequest):
    num = request.num
    credit_num = random.randint(0, num)
    debit_num = num - credit_num
    credit_elements = random.sample(
        account_elements.get_credits_elements,
        min(credit_num, len(account_elements.get_credits_elements)),
    )
    debit_elements = random.sample(
        account_elements.get_debits_elements,
        min(debit_num, len(account_elements.get_debits_elements)),
    )

    elements = [
        NormalBalanceElements(name=el, type="credit") for el in credit_elements
    ] + [NormalBalanceElements(name=el, type="debit") for el in debit_elements]

    random.shuffle(elements)
    return elements
