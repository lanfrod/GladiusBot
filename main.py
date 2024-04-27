import telebot
from telebot import types
import pymorphy2
from PIL import Image, ImageDraw
import sqlite3
from translate import Translator
import passss
import json
import requests
import pole
import mani
import smtplib
from youtube_search import YoutubeSearch
from googlesearch import search

bot = telebot.TeleBot(passss.api_bot)
API = 'f2d22ddb2ceebe30809c690d48af0e56'
NAME = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
        '4', '5', '6', '7', '8', '9', '0']
PASSWORD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
            '%', '^', '&', '*', '_']
with open('hesh.txt', 'r') as file:
    qq = str(file.read().split(' '))
    hesh = {}
    for i in range(0, len(qq) // 2):
        hesh[qq[i * 2]] = qq[i * 2 + 1]


@bot.message_handler(commands=['close'])
def all_messages(message):
    sq = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Done with Keyboard", reply_markup=sq)


@bot.message_handler(commands=['game'])
def game(message):
    with open('game_lobby.txt', 'r') as file:
        s = file.read().split(',')
        print(s)
        toft = ','.join(s)
    qua = s[-1].split('.')
    id = str(message.from_user.id)
    print(toft)
    ro = False
    if id not in toft:
        if len(qua) == 4:
            game_lobby = ",".join(s) + ',' + id
            with open('game_lobby.txt', 'w') as file: file.write(game_lobby)
        elif len(qua) == 1 and qua[-1] != "":
            game_lobby = ','.join(s) + '.' + id + '.' + "1" + '.' + "?/?/?/?/?/?/?/?/?" # изменить
            with open('game_lobby.txt', 'w') as file: file.write(game_lobby)
            bot.send_message(message.chat.id, "Ожидайте хода соперника")
            play(message)
        else:
            game_lobby = id
            with open('game_lobby.txt', 'w') as file: file.write(game_lobby)
    elif id in toft:
        for i in s:
            print(i)
            if (id in s) and int(i.split(".")[2]) > 1:
                ro = True
        if ro:
            bot.register_next_step_handler(message, play)
        else:
            bot.send_message(message.chat.id, f"Вы уже в очереди, ожидайте")


def play(message):
    print(1)
    with open('game_lobby.txt', 'r') as file:
        s = file.read().split(',')
    for i in s:
        print(i.split('.'))
        player1, player2, round_number, bo = i.split('.')
        markup = types.InlineKeyboardMarkup()
        emoji = []
        for i in bo.split("/"):
            if i == "?":
                emoji.append("❓")
            elif i == "x":
                emoji.append("❌")
            elif i == "o":
                emoji.append("🅾️")
        btn1 = types.InlineKeyboardButton(f'{emoji[0]}', callback_data='left_top')
        btn2 = types.InlineKeyboardButton(f'{emoji[1]}', callback_data='mid_top')
        btn3 = types.InlineKeyboardButton(f'{emoji[2]}', callback_data='right_top')
        btn4 = types.InlineKeyboardButton(f'{emoji[3]}', callback_data='left_mid')
        btn5 = types.InlineKeyboardButton(f'{emoji[4]}', callback_data='mid_mid')
        btn6 = types.InlineKeyboardButton(f'{emoji[5]}', callback_data='right_mid')
        btn7 = types.InlineKeyboardButton(f'{emoji[6]}', callback_data='left_bot')
        btn8 = types.InlineKeyboardButton(f'{emoji[7]}', callback_data='mid_bot')
        btn9 = types.InlineKeyboardButton(f'{emoji[8]}', callback_data='right_bot')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        round_number = int(round_number)
        pole.board(bo)
        if round_number % 2 == 1:
            image = 'res.png'
            file = open('img/' + image, 'rb')
            bot.send_photo(int(player1), file)
            if round_number == 1:
                bot.send_message(int(player1), "Вы - крестик. Выберите поле для хода.", reply_markup=markup)
            else:
                bot.send_message(int(player1), "Выберите поле для хода.", reply_markup=markup)
        if round_number % 2 == 0:
            image = 'res.png'
            file = open('img/' + image, 'rb')
            bot.send_photo(int(player2), file)
            if round_number == 2:
                bot.send_message(int(player2), "Вы - нолик. Выберите поле для хода.", reply_markup=markup)
            else:
                bot.send_message(int(player2), "Выберите поле для хода.", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_mes(callback):
    print(2)
    t = 0
    if callback.data == 'left_top':
        t = 1
    elif callback.data == 'mid_top':
        t = 2
    elif callback.data == 'right_top':
        t = 3
    elif callback.data == 'left_mid':
        t = 4
    elif callback.data == 'mid_mid':
        t = 5
    elif callback.data == 'right_mid':
        t = 6
    elif callback.data == 'left_bot':
        t = 7
    elif callback.data == 'mid_bot':
        t = 8
    elif callback.data == 'right_bot':
        t = 9
    print(callback.message.chat.id)
    move = str(callback.message.chat.id)
    count = 0
    with open('game_lobby.txt', 'r') as file:
        s = file.read().split(',')
    for i in s:
        count += 1
        print(s)
        if move in i:
            print(move)
            li = i.split(".")
            print(li)
            pol = ""
            wait = ""
            if li[0] == move and int(li[2]) % 2 == 1:
                pol = li[3].split("/")
                print(pol)
                pol[t - 1] = "x"
                pol = "/".join(pol)
                wait = li[1]
            elif li[1] == move and int(li[2]) % 2 == 0:
                pol = li[3].split("/")
                pol[t - 1] = "o"
                pol = "/".join(pol)
                wait = li[0]
            timered = [li[0], li[1], str(int(li[2]) + 1), pol]
            r = '.'.join(timered)
            s[count - 1] = r
            print(s)
            print(pol)
            bot.send_message(int(move), "Ваш ход принят. Ожидайте соперника")
            bot.send_message(int(wait), "Соперник сделал ход")
    game_lobby = ','.join(s)
    with open('game_lobby.txt', 'w') as file:
        file.write(game_lobby)
    play(int(wait))
    #bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



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


@bot.message_handler(commands=['site', 'website'])
def site(message):
    print(6)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Vk', url='https://vk.com/lanfrod'))
    bot.send_message(message.chat.id, f'Привет, вот контакты разработчика', reply_markup=markup)


@bot.message_handler(commands=['login'])
def login(message):
    pass


@bot.message_handler(commands=['registration'])
# СДЕЛАТЬ CONTENT_TYPES = TEXT ХЕНДЛЕР ЧТОБЫ ОПРЕДЕЛЯЛ ВСЕ ДРУГИЕ
def registration(message):
    print(message.text.lower())
    print(message)
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    #TYPE - ЗОЛОТАЯ ВЕЩЬ
    sos2 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (message.from_user.id,)).fetchone()
    if message.text.lower() == "регистрация" or message.text.lower() == '/registration':
        if sos2:
            bot.send_message(message.chat.id, 'Данный аккаунт уже зарегистрирован')
            #bot.delete_message(message.chat.id, message.message_id)
            bot.clear_step_handler(message)
        else:
            bot.send_message(message.chat.id, f'{message.from_user.username.capitalize()}, чтобы зарегистрироваться'
                                          f' напиши желаемый login. Он будет использован как никнейм. Ник может состоять '
                                          f'из латинских букв разного регистра, цифр')
            bot.register_next_step_handler(message, user_name)
    else:
        get_weather(message)


def user_name(message):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    proxod = True
    global name
    name = message.text.strip()
    for i in name:
        if i not in NAME:
            proxod = False
    if proxod:
        proverb = cur.execute('''SELECT * FROM passwords WHERE login = ?''', (name,)).fetchall()
        print(proverb)
        conn.close()
        if not proverb:
            bot.send_message(message.chat.id, 'Введите пароль. Он может состоять из латинских букв разного регистра, цифр '
                                              'специальных символов и нижнего подчёркивания.')
            bot.register_next_step_handler(message, user_pass)
        else:
            bot.send_message(message.chat.id, 'Такой пользователь уже существует. Введите другой логин')
            bot.register_next_step_handler(message, user_name)
    else:
        bot.send_message(message.chat.id, 'Недопустимое имя. Введите другой логин')
        bot.register_next_step_handler(message, user_name)


def user_pass(message):
    global password
    global hesh_password
    b = True
    password = message.text.strip()
    for i in password:
        if i not in PASSWORD:
            b = False
    if b:
        bot.send_message(message.chat.id, 'Введите почту для привязки')
        with open('hesh.txt', 'r') as file:
            k = file.read().split(" ")
            heshing = {}
            for i in range(len(k) // 2):
                heshing[k[i * 2]] = k[i * 2 + 1]
            hesh_password = ""
            for i in password:
                hesh_password += heshing[i]
        bot.register_next_step_handler(message, user_email)
    else:
        bot.send_message(message.chat.id, 'Недопустимый пароль. Введите другой пароль')
        bot.register_next_step_handler(message, user_pass)


def user_email(message):
    global email
    email = message.text.strip()
    nickname = message.from_user.first_name
    tgid = message.from_user.id
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    try:
        sos1 = cur.execute('''SELECT * FROM userinfo WHERE email = ?''', (email,)).fetchall()
        if sos1:
            raise Exception()
        mani.send_email(email, 'Registration', f'{nickname}, это капча для подтверждения регистрации. Введите код с капчи'
                                               f' в чате с ботом')
        up = mani.pat()
        res = '' # капча длинная(наслаивается вероятно), сделать кнопку отмены/выхода из действия
        for i in up:
            res += i
        print(res)
        cur.execute('''INSERT INTO captchatab (nickname, captcha) VALUES (?, ?)''', (tgid, res, ))
        bot.send_message(message.chat.id, 'Проверьте вашу почту и введите код с капчи')
        conn.commit()
        conn.close()
        bot.register_next_step_handler(message, cap)
        print(1)
    except Exception: #ошибка с некорректной почтой
        bot.send_message(message.chat.id, 'Неправильная почта. Введите другую почту ещё раз')
        bot.register_next_step_handler(message, user_email)
        print(3)
    except smtplib.SMTPRecipientsRefused:
        bot.send_message(message.chat.id, 'Неправильная почта. Введите другую почту ещё раз')
        bot.register_next_step_handler(message, user_email)
        print(2)
    #образец send_email("akolelow@mail.ru", 'Registration', f'Вот капча для подтверждения регистрации')


def cap(message):
    captcha = message.text.strip()
    num = message.message_id
    if captcha != mani.pat():
        bot.send_message(message.chat.id, 'Неверная капча. Проверьте вашу почту и введите код с капчи')
        print(num, 'num')
        print(message.message_id)
        bot.register_next_step_handler(message, cap)
    elif captcha == mani.pat():
        bot.send_message(message.chat.id, 'Почта подтверждена')
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        nickname = message.from_user.first_name
        tg_id = message.from_user.id
        print(nickname)
        cur.execute("INSERT INTO passwords (login, pass) VALUES ('%s', '%s')" % (name, hesh_password))
        cur.execute("INSERT INTO userinfo (login, email, nickname, tg_id) VALUES ('%s', '%s', '%s', '%s')" % (name, email, nickname, tg_id))
        conn.commit()
        conn.close()
        markup = telebot.types.InlineKeyboardMarkup()
        #markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
        bot.send_message(message.chat.id, f'Пользователь {name} зарегистрирован', reply_markup=markup)


@bot.message_handler(commands=['weather'])
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
