import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.database import db

@Client.on_message(filters.text & (filters.group | filters.private))
async def search_movie(bot, message):
    # മൂന്ന് അക്ഷരമെങ്കിലും ഉണ്ടെങ്കിൽ മാത്രമേ സെർച്ച് ചെയ്യൂ
    query = message.text
    if len(query) < 3:
        return

    # ഡാറ്റാബേസിൽ നിന്ന് സിനിമകൾ തിരയുന്നു
    files = await db.get_search_results(query)
    
    if not files:
        # സിനിമ ഇല്ലെങ്കിൽ ഗ്രൂപ്പിൽ ബഹളം വെക്കാതിരിക്കാൻ റിപ്ലൈ ഒഴിവാക്കാം
        return

    buttons = []
    for file in files:
        # ഫയൽ സൈസ് കണക്കാക്കുന്നു (MB അല്ലെങ്കിൽ GB-യിൽ)
        f_size = file['file_size']
        abs_size = f_size / (1024 * 1024)
        if abs_size > 1024:
            formated_size = f"{round(abs_size / 1024, 2)} GB"
        else:
            formated_size = f"{round(abs_size, 2)} MB"

        # സിനിമയുടെ പേരും സൈസും ബട്ടണിൽ വരുന്നു
        buttons.append([
            InlineKeyboardButton(
                text=f"🎬 {file['file_name']} - {formated_size}", 
                callback_data=f"send_{file['file_id']}"
            )
        ])

    if buttons:
        await message.reply_text(
            text=f"**Found {len(files)} results for:** `{query}`\n\n_Select your preferred quality below:_",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

# ബട്ടണിൽ ക്ലിക്ക് ചെയ്താൽ ഫയൽ അയക്കാനുള്ള ലോജിക്
@Client.on_callback_query(filters.regex(r"^send_"))
async def send_file(bot, query):
    file_id = query.data.split("_")[1]
    
    try:
        # യൂസറിന് ഒരു അലേർട്ട് നൽകുന്നു
        await query.answer("Fetching your file... Please wait!", show_alert=False)
        
        # ഫയൽ അയക്കുന്നു (ഇത് ടെലിഗ്രാം സെർവറിൽ ഉള്ള ഫയൽ ആയതുകൊണ്ട് സ്പീഡിൽ ലഭിക്കും)
        await bot.send_cached_media(
            chat_id=query.message.chat.id,
            file_id=file_id,
            caption=f"**Here is your requested file.**\n\n_Powered by Chithrashala_"
        )
    except Exception as e:
        await query.answer(f"Error: {str(e)}", show_alert=True)
