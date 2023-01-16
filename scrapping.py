import requests
from bs4 import BeautifulSoup
import telebot
#from telebot import types
import schedule
import time

API_KEY = 'Your_API_KEY'

url = "Your_Site_URL"


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"} #user simulation


response = requests.get(url, headers=headers)
print(response)
bs = BeautifulSoup(response.text, 'lxml')

news_txt = bs.find('h2', 'd-md-none mb-0 pt-1 h5') #filter for the news you want
news = news_txt.text
print(news) #not necessary, used for comparison



bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def send_news(message=None):
    if message is not None:
        chat_id = message.chat.id
    else:
        chat_id = 'your_chat_id'
    bot.send_message(chat_id=chat_id, text="Main news -" + news)

to_do = schedule.every().day.at("09:00").do(send_news) #еime when me need getting a news


while True:
    schedule.run_pending()
    time.sleep(1)




bot.polling()
