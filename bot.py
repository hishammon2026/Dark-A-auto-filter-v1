import os
import asyncio
from pyrogram import Client
from config import Config
from aiohttp import web

# --- വെബ് സർവർ ലോജിക് (Render-ന് വേണ്ടി മാത്രം) ---
async def hello(request):
    return web.Response(text="Chithrashala Bot is Alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", hello)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render നൽകുന്ന PORT എടുക്കുന്നു, ഇല്ലെങ്കിൽ 8080 എടുക്കുന്നു
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"✅ Web Server started on port {port}")

# --- ബോട്ട് ക്ലാസ് ---
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
        # ബോട്ട് സ്റ്റാർട്ട് ആയ ഉടനെ വെബ് സർവർ തുടങ്ങുന്നു
        await start_web_server()
        print("🚀 Bot is Online!")

    async def stop(self, *args):
        await super().stop()
        print("🛑 Bot Stopped!")

if __name__ == "__main__":
    app = Bot()
    app.run()
