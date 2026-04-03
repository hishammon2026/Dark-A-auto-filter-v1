import os
import asyncio
from pyrogram import Client
from config import Config # നിന്റെ config.py ഫയലിൽ നിന്ന് വാല്യൂസ് എടുക്കുന്നു
from aiohttp import web

# Render-ന് വേണ്ടിയുള്ള വെബ് സർവർ
async def hello(request):
    return web.Response(text="Chithrashala Bot is Alive and Running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", hello)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render നൽകുന്ന PORT മാത്രം എൻവയോൺമെന്റിൽ നിന്ന് എടുക്കുന്നു
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"✅ Web Server started on port {port}")

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FilterBot",
            api_id=Config.API_ID,     # നേരിട്ട് Config-ൽ നിന്ന് എടുക്കുന്നു
            api_hash=Config.API_HASH, # നേരിട്ട് Config-ൽ നിന്ന് എടുക്കുന്നു
            bot_token=Config.BOT_TOKEN, # നേരിട്ട് Config-ൽ നിന്ന് എടുക്കുന്നു
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        await start_web_server()
        print("🚀 Chithrashala Bot is Online!")

    async def stop(self, *args):
        await super().stop()
        print("🛑 Bot Stopped!")

if __name__ == "__main__":
    app = Bot()
    app.run()
