import telebot
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv('api_key')
bot = telebot.TeleBot(api_key)

dict = pd.read_csv('urbandict-word-defs.csv',on_bad_lines='skip')
words=dict['word'].tolist()
meaning=dict['definition'].tolist()
size=len(words)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Bob🐶.
I am here to answer you the urban dictionary meaning of a word. Just say anyword and I'll send the urban meaning to you🦴!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    input_word=message.text.lower()
    print(input_word)
    f = open("searched_words.txt", "a")
    f.write(f"{input_word} \n")
    f.close()
    counter=0

    for i in range(0,size):
        counter+=1
        dictionary=words[i]
        if input_word==dictionary:
            mean=meaning[i]
            mean = mean.replace(";;", "\n")

            bot.reply_to(message,mean)
            df1 = pd.read_excel('Telegram_Dictionary_Bot_users_dataset.xlsx', index_col=0)
            df2 = pd.DataFrame([[message.date,message.from_user.id,message.from_user.first_name,\
                message.from_user.username,input_word,message.from_user.is_premium,message.from_user.is_bot]] \
                ,columns=['date','user_id','first_name','username','words','is_premium','is_bot']).set_index('date')
            df3 = pd.concat([df1, df2])
            df3.to_excel("Telegram_Dictionary_Bot_users_dataset.xlsx",startrow=0,startcol=0) 
            break
        else:
            if counter==size:
             bot.reply_to(message,"Word not found! try again")

bot.infinity_polling()
