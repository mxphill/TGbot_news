import requests
from bs4 import BeautifulSoup
from translate import Translator
import telebot
from telebot import types
import schedule
import time

API_KEY = '5829570171:AAFNkFeVPIhgwFm6-gbijkNMKIGLK2B9HE8'

url = "https://www.dutchnews.nl/news/category/society/"


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}


response = requests.get(url, headers=headers)
print(response)
bs = BeautifulSoup(response.text, 'lxml')

news_txt = bs.find('h2', 'd-md-none mb-0 pt-1 h5')
news = news_txt.text
print(news)



bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def send_news(message=None):
    if message is not None:
        chat_id = message.chat.id
    else:
        chat_id = 335249930
    bot.send_message(chat_id=chat_id, text="Main news -" + news)

to_do = schedule.every().day.at("09:00").do(send_news)


while True:
    schedule.run_pending()
    time.sleep(1)



'''
translator = Translator(from_lang="english",to_lang="russian")
translation = translator.translate(news)
print (translation)
'''


bot.polling()