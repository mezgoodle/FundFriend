import os


class DefaultConfig:
    """Bot Configuration"""

    PORT = os.environ.get("PORT", 3978)
    HOST = os.environ.get("HOST", "localhost")
    APP_ID = os.environ.get("MicrosoftAppId")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword")
