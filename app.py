from flask import Flask
from pyrogram import Client, filters, idle
#from main import Bot
import threading


app = Flask(__name__)
app.debug = True
#pyro = Client("account")

pyro = Client(
    "LibraryBot",
    bot_token="5976715403:AAGgEOL7PmixhQWfa7p3avxsGF9biQgtl90",
    api_id=1774230,
    api_hash="b0829cf5b62052d6c8adee27b02f1f00"
    )

@pyro.on_message(filters.private & filters.command(["start"]))
async def settings(bot,message):
  #print(f"{message.chat.id}")
  #if int(message.chat.id) in Config.OWNER_ID:
  #await message.reply_text("<b>👤 Admin Pannel</b>",reply_markup=helper.AdminKeyboard)
  #else:
  #Chat_Id = message.chat.id
  await message.reply_text("<b>💔 Only Admin Command!!</b>")
 

@app.route("/")
def hello_worldyy():
    return str(pyro.get_me())

@app.route('/home')
def hello_world():
  return 'GreyMatter_Botskk'

pyro.start()
threading.Thread(target=app.run, daemon=True).start()
idle()
pyro.stop()

#@app.route('/')
#def hello_worldy():
#  print("akhil")
#  Bot.start()
#  idle()
#  Bot.stop()

#def Pyroggram():
  
#print("kyuki kyaa hotaa h")


#if __name__ == "__main__":
    #print("akhil2")
    #Pyroggram()
#    app.run(debug="True")








