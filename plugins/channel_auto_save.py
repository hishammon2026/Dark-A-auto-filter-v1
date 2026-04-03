from pyrogram import Client, filters
from database.database import db

@Client.on_message(filters.chat_active & (filters.document | filters.video))
async def auto_save(bot, message):
    chat_id = message.chat.id
    try:
        # ബോട്ട് ഈ ചാനലിൽ അഡ്മിൻ ആണോ എന്ന് പരിശോധിക്കുന്നു
        member = await bot.get_chat_member(chat_id, "me")
        if member.status in ["administrator", "creator"]:
            file = message.document or message.video
            # ഫയൽ വിവരങ്ങൾ ഡാറ്റാബേസിലേക്ക് അയക്കുന്നു
            await db.save_file(
                file_name=file.file_name,
                file_id=file.file_id,
                file_size=file.file_size,
                caption=message.caption or file.file_name
            )
            print(f"✅ New file saved from: {message.chat.title}")
    except Exception as e:
        print(f"Error in auto_save: {e}")
