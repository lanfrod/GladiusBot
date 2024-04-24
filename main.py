import telebot
from telebot import types
import pymorphy2
import sqlite3
from translate import Translator
import json
import requests
from youtube_search import YoutubeSearch
from googlesearch import search

bot = telebot.TeleBot('6851175195:AAF8vfmlpJWCWioSo-sOpPpZKDAAx6jAbN8')
API = 'f2d22ddb2ceebe30809c690d48af0e56'


@bot.message_handler(commands=['google'])
def google(message):
    query = message.text.strip()
    print(1)
    print(query)
    print(message)
    for i in search(query, tld='co.in', lang='ru', num=3, stop=10, pause=2):
        bot.send_message(message.chat.id, i)


@bot.message_handler(commands=['video'])
def video(message):
    vid = message.text.strip()
    print(vid)
    results = YoutubeSearch(vid).to_dict()
    print(results)
    for i in range(3):
        bot.send_message(message.chat.id, f"https://www.youtube.com{results[i]['url_suffix']}")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓")
    markup.add(btn1)
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города, чтобы узнать погоду.', reply_markup=markup)


@bot.message_handler()
def registration(message):
    if message.text.lower == "регистрация":
        conn = sqlite3.connect('users.sql')
        cur = conn.cursor()

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    morph = pymorphy2.MorphAnalyzer()
    city_parse = morph.parse(city)[0].inflect({"loct"}).word
    s = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if s.status_code == 200:
        data = json.loads(s.text)
        print(city)
        print(data)
        if data["weather"][0]["description"] == "weather condition":
            word1 = "мало облаков"
            print(word1)
        elif data["weather"][0]["description"] == "overcast clouds":
            word1 = "пасмурные облака"
        else:
            word1 = Translator(from_lang="english", to_lang="russian").translate(data["weather"][0]["description"])
        #s2 = morph.parse(word1)[1].inflect({"ADJF"}).inflect({"femn"})
        #print(morph.parse(word1)[1])
        bot.reply_to(message, f'Сейчас погода в {city_parse.capitalize()}: {word1.lower()}. Температура воздуха:'
                              f' {data["main"]["temp"]}°C')
        if word1.lower() == "ясно":
            image = 'sunny3.png'
        elif word1.lower() == "мало облаков":
            image = 'obla.png'
        elif word1.lower() == "облачно":
            image = 'obl.png'
        elif word1.lower() == "пасмурные облака":
            image = 'ty4a.jpg'
        elif word1.lower() == "дым":
            image = 'tyman.jpg'
        else:
            image = 'loading-13.gif'
        file = open('img/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Город не найден. Попробуйте снова.")



bot.polling(none_stop=True)
