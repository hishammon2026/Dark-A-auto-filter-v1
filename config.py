import os

class Config:
    API_ID = int(os.environ.get("API_ID", "your api id"))
    API_HASH = os.environ.get("API_HASH", "your api hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your bot token")
    DATABASE_URI = os.environ.get("DATABASE_URI", "your MONGODB_LINK")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    START_PIC = os.environ.get("START_PIC", "your telegraph pic")
    ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "your id").split()]
