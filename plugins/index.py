from pyrogram import Client, filters
from database.database import db
from config import Config

@Client.on_message(filters.forwarded & filters.private & filters.user(Config.ADMINS))
async def forward_index(bot, message):
    if message.forward_from_chat:
        chat_id = message.forward_from_chat.id
        last_msg_id = message.forward_from_message_id
        
        status = await message.reply_text("🔍 **Indexing started... Please wait.**")
        
        count = 0
        # ചാനലിലെ പഴയ മെസ്സേജുകൾ ഓരോന്നായി സ്കാൻ ചെയ്യുന്നു
        async for msg in bot.iter_messages(chat_id, limit=last_msg_id):
            if msg.document or msg.video:
                file = msg.document or msg.video
                await db.save_file(
                    file_name=file.file_name,
                    file_id=file.file_id,
                    file_size=file.file_size,
                    caption=msg.caption or file.file_name
                )
                count += 1
                if count % 100 == 0:
                    await status.edit(f"⚡ **Indexed {count} files...**")

        await status.edit(f"✅ **Success! {count} files indexed from '{message.forward_from_chat.title}'.**")
    else:
        await message.reply_text("❌ Please forward a file from a channel.")
