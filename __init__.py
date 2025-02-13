import uvicorn
from api import app
from setting import WebSetting

if __name__ == "__main__":

    uvicorn.run(
        app,
        host=WebSetting.api_host.value,
        port=WebSetting.api_port.value,
    )
