from enum import Enum


class WebSetting(Enum):
    """
    basesetting for web
    """

    api_host = "0.0.0.0"
    api_port = 12138
    api_base = "/dependency"
    web_host = "0.0.0.0"
    web_port = 3141
    web_base = ""
