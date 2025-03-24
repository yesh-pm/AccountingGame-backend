import uvicorn
from api import app
from setting import WebSetting
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for simplicity (you can restrict to your domain later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your domain(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the app!"}

if __name__ == "__main__":

    uvicorn.run(
        app,
        host=WebSetting.api_host.value,
        port=WebSetting.api_port.value,
    )
