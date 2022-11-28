import logging
import os
#from config import Config
import pyrogram
from pyrogram import Client
 
 
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

app = Client(
    "LibraryBot",
    bot_token="5913561812:AAHfAcCA_PKkBO0DgWuLhn7XUIaLlmsiOow",
    api_id=1774230,
    api_hash="b0829cf5b62052d6c8adee27b02f1f00"
    )
    #Config.BOT_TOKEN,
    #Config.API_ID,
    #Config.API_HASH,
    #plugins=plugins, 



@Client.on_message(filters.private & filters.command(["admin"]))
async def settings(bot,message):
  #print(f"{message.chat.id}")
  #if int(message.chat.id) in Config.OWNER_ID:
  #await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  #else:
  #Chat_Id = message.chat.id
  await message.reply_text("<b>💔 Only Admin Command!!</b>")
   




if __name__ == "__main__" :
  #download_path = "Downloads/"
  #if not os.path.isdir(download_path):
    #os.mkdir(download_path)
  #plugins = dict(root="plugins")
  app.run()
  
  
 
 




#import os
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Koyeb'

#if __name__ == "__main__":
    #app.run(debug=True,host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
