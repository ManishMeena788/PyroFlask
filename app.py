from flask import Flask
from pyrogram import Client, filters, idle
from main import Bot
app = Flask(__name__)
 
@app.route('/')
def hello_world():
  return 'GreyMatter_Botskk'
  print("akhil")
  Bot.start()
  idle()
  Bot.stop()

#def Pyroggram():
  
print("kyuki kyaa hotaa h")


if __name__ == "__main__":
    #print("akhil2")
    #Pyroggram()
    app.run(debug="True")