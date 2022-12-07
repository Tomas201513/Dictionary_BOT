import os
import telebot
from dotenv import load_dotenv
load_dotenv()
import pandas
api_key=os.getenv('api_key')
bot = telebot.TeleBot(api_key)
#https://drive.google.com/file/d/1OqNUMS5zlJDIHLWNDhjuxugYtZS9_kph/view?usp=sharing

dict = pandas.read_csv('urbandict-word-defs.csv',on_bad_lines='skip')
words=dict['word'].tolist()
meaning=dict['definition'].tolist()
size=len(words)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    input_word=message.text.lower()
    counter=0
    for i in range(0,size):
        counter+=1
        dictionary=words[i]
        if input_word==dictionary:
            mean=meaning[i]
            print(meaning[i])
            bot.reply_to(message,mean)
            break
        else:
            if counter==size:
             bot.reply_to(message,"Word not found! try again")

        

bot.infinity_polling()
# bot.sendDocument