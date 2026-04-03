from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    buttons = [
        [
            InlineKeyboardButton("➕ Add Me To Your Group ➕", url=f"http://t.me/{bot.username}?startgroup=true")
        ],
        [
            InlineKeyboardButton("Help 💡", callback_data="help"),
            InlineKeyboardButton("About ℹ️", callback_data="about")
        ]
    ]
    
    await message.reply_photo(
        photo=Config.START_PIC,
        caption=f"**Hello {message.from_user.mention},**\n\nI am an Advanced Auto Filter Bot. You can search movies here or in your groups!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
