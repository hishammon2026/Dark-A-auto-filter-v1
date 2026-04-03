from pyrogram import Client
from config import Config

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FilterBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        print("Bot is Online!")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped!")

if __name__ == "__main__":
    app = Bot()
    app.run()
