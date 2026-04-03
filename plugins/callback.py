from pyrogram import Client, filters
from database.database import db

@Client.on_callback_query()
async def cb_handler(bot, query):
    data = query.data

    # സിനിമയുടെ ഫയൽ അയക്കാനുള്ള ലോജിക്
    if data.startswith("send_"):
        file_id = data.split("_")[1]
        
        try:
            # ബട്ടൺ ഞെക്കുമ്പോൾ മുകളിൽ ചെറിയൊരു മെസ്സേജ് കാണിക്കാൻ
            await query.answer("Preparing your file... Please wait!", show_alert=False)
            
            # ഫയൽ അയക്കുന്നു
            await bot.send_cached_media(
                chat_id=query.message.chat.id,
                file_id=file_id,
                caption=f"**Here is your requested movie.**\n\n_Powered by Chithrashala_"
            )
        except Exception as e:
            await query.answer(f"Error: {str(e)}", show_alert=True)

    # ഹെൽപ്പ് ബട്ടൺ ലോജിക്
    elif data == "help":
        await query.message.edit_text(
            text="**How to use me?**\n\n1. Add me to your group.\n2. Make me admin.\n3. Just type movie name in group or PM.\n4. Click the button to get the file!",
            reply_markup=query.message.reply_markup
        )

    # എബൗട്ട് ബട്ടൺ ലോജിക്
    elif data == "about":
        await query.message.edit_text(
            text="**About Me**\n\nI am an Advanced Auto Filter Bot built by hisham for movie lovers. I can index millions of files and provide them instantly!",
            reply_markup=query.message.reply_markup
      )
