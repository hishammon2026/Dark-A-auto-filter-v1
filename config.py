import os

class Config:
    API_ID = int(os.environ.get("API_ID", "28390522"))
    API_HASH = os.environ.get("API_HASH", "bb6e4438855b6c9ac8d9f0d999a664c4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8717566228:AAEClZPtvCtagIViPRJlhE5Bw2sT6FR-9R8")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://hishammon:hishammon@cluster0.2g7bqyf.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/32a61cb5e9dbe98d79f9a-51aea34fedf9627dc6.jpg")
    ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "7042953166").split()]
