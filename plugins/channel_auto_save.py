from pyrogram import Client, filters
from database.database import db

# 'filters.chat_active' എന്നതിന് പകരം 'filters.chat' ഉപയോഗിക്കുന്നു
# ഇത് ഗ്രൂപ്പുകളിലും ചാനലുകളിലും ഒരുപോലെ വർക്ക് ചെയ്യും
@Client.on_message(filters.chat & (filters.document | filters.video))
async def auto_save(bot, message):
    chat_id = message.chat.id
    try:
        # ബോട്ട് ഈ ചാനലിൽ/ഗ്രൂപ്പിൽ അഡ്മിൻ ആണോ എന്ന് പരിശോധിക്കുന്നു
        member = await bot.get_chat_member(chat_id, "me")
        
        # അഡ്മിൻ അല്ലെങ്കിൽ ക്രിയേറ്റർ ആണെങ്കിൽ മാത്രം ഫയൽ സേവ് ചെയ്യും
        if member.status in ["administrator", "creator"]:
            file = message.document or message.video
            
            # ഫയൽ വിവരങ്ങൾ നിന്റെ ഡാറ്റാബേസിലേക്ക് (MongoDB) അയക്കുന്നു
            await db.save_file(
                file_name=file.file_name,
                file_id=file.file_id,
                file_size=file.file_size,
                caption=message.caption or file.file_name
            )
            print(f"✅ New file saved from: {message.chat.title}")
            
    except Exception as e:
        # എന്തെങ്കിലും എറർ ഉണ്ടെങ്കിൽ അത് ലോഗ്സിൽ കാണിക്കും
        print(f"Error in auto_save: {e}")
