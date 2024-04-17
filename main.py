import telebot
import pymorphy2
import sqlite3
from translate import Translator
import json
import requests

bot = telebot.TeleBot('6392696125:AAGyTVi-0XKujfhTMY8MhgyfhtWWQFgLVPM')
API = '14a04328ce615e1e649216386834a1a1'
with open('hesh.txt', 'r') as file:
    qq = str(file.read().split(' '))
    hesh = {}
    for i in range(0, len(qq) // 2):
        hesh[qq[i * 2]] = qq[i * 2 + 1]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города, чтобы узнать погоду.')

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