from flask import Flask
from pyrogram import Client, filters, idle
from main import Bot
app = Flask(__name__)
 
@app.route('/')
def hello_world():
  return 'GreyMatter_Botskk'

def Pyroggram():
  print("akhil")
  Bot.start()
  idle()
  Bot.stop()



if __name__ == "__main__":
    print("akhil2")
    Pyroggram()
    app.run(debug="True")