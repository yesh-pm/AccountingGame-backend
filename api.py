from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from setting import WebSetting
from data_interface import account_elements

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


@app.get("/get_all_nb_element")
async def get_all_nb_element():
    return {
        "credit": account_elements.get_credits_elements,
        "debit": account_elements.get_debits_elements,
    }
