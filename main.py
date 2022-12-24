import logging
import os
#from config import Config
import pyrogram
from pyrogram import Client
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

 
 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

Bot = Client(
    "LibraryBot",
    bot_token="5976715403:AAGgEOL7PmixhQWfa7p3avxsGF9biQgtl90",
    api_id=1774230,
    api_hash="b0829cf5b62052d6c8adee27b02f1f00"
    )
    #Config.BOT_TOKEN,
    #Config.API_ID,
    #Config.API_HASH,
    #plugins=plugins, 



@Bot.on_message(filters.private & filters.command(["start"]))
async def settings(bot,message):
  #print(f"{message.chat.id}")
  #if int(message.chat.id) in Config.OWNER_ID:
  #await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  #else:
  #Chat_Id = message.chat.id
  await message.reply_text("<b>💔 Only Admin Command!!</b>")
   
#@Bot.on_message(filters.private & filters.command("start2"))
#async def start_handler(_, event: Message):
#	await event.reply_photo("https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
#                                caption=Config.START_MSG.format(event.from_user.mention),
#                                reply_markup=InlineKeyboardMarkup([
#					[InlineKeyboardButton('❤ Donation Link', url='https://www.telegram.dog/greymatters_about')],
#					[InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/GreyMatter_Bots")],
#					[InlineKeyboardButton("Donation", callback_data="Help_msg"),
#                                        InlineKeyboardButton("About", callback_data="About_msg")]
#				]))



#if __name__ == "__main__" :
  #download_path = "Downloads/"
  #if not os.path.isdir(download_path):
    #os.mkdir(download_path)
  #plugins = dict(root="plugins")
#  app.run()
  
  
 
 




#import os
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Koyeb'

#if __name__ == "__main__":
    #app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
# Start Clients
Bot.start()
#User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
#User.stop()
 