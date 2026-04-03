import os
from pyrogram import Client
from config import Config
from aiohttp import web

# Render-ന് വേണ്ടിയുള്ള ചെറിയ വെബ് സർവർ
async def hello(request):
    return web.Response(text="Chithrashala Bot is Alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", hello)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

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
        await start_web_server()
        await super().start()
        print("Bot Started Successfully!")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped!")

if __name__ == "__main__":
    app = Bot()
    app.run()
