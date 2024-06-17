import telebot
from telebot import types
import pymorphy2
import sqlite3
from translate import Translator
import passss
import json
import requests
import pole
import mani
# import googlesearch  библиотека нужна для поиска, но работает в локальной сети, хост ее не воспринимает
import smtplib
from youtube_search import YoutubeSearch

REPL = ""  # для использования в локальной сети уберите /data/, для хоста используйте /data/
bot = telebot.TeleBot("6392696125:AAETy96cioNjK3XIMm97Tkh_OPBmohbZRqI")  # yeap
API = 'f2d22ddb2ceebe30809c690d48af0e56'
EMOJIES = ['CAACAgIAAxkBAAEGMEhmbxtP12lTH-6Xro0WEd3mZJEtFQACG1IAAowQeUuDLK3SWk2y7TUE',
           'CAACAgIAAxkBAAEGMEZmbxtNsL-KYunOvnr9mfnyumbUWwACRE0AAryBeUt4BrdPKPvaPDUE',
           'CAACAgIAAxkBAAEGMERmbxtMZElajC1Dae8AAdnxGMvAPRsAAn5JAAKVmnlLBwAB0Icc3xgSNQQ',
           'CAACAgIAAxkBAAEGMExmbxtRwtjK64DFT_kRvNoIGhv_UAACT00AAjM_eEv_pagVw7mUjDUE',
           'CAACAgIAAxkBAAEGMEpmbxtQfhrv5f8bzER6tOC40rn-HgAC008AAnCleEtbGaePzX7lnTUE',
           'CAACAgIAAxkBAAEGMEJmbxtMcViNdeWBswJPv5TTFKxN5QACWU8AAuh1eUvd6lZWQIHLSDUE'

NAME = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
        '4', '5', '6', '7', '8', '9', '0']
ENGLISH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
PASSWORD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
            '%', '^', '&', '*', '_']
with open(REPL + 'hesh.txt', 'r') as file:
    qq = str(file.read().split(' '))
    hesh = {}
    for i in range(0, len(qq) // 2):
        hesh[qq[i * 2]] = qq[i * 2 + 1]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напишите /help чтобы узнать больше команд')


@bot.message_handler(commands=['help'])
def qwark(message):
    bot.send_message(message.from_user.id, "Вот вам список команд, которые может выполнять бот \n "
                                           "/start - Начните общение с ботом \n  "
                                           "/contacts - аккаунты разработчиков \n"
                                           "/towns - Укажите любимые города, чтобы легче смотреть погоду \n"
                                           "/weather - Узнайте погоду в городе \n"
                                           "/clear - Напиши, чтобы выйти из команды \n"
                                           "/recepts - Узнайте рецепт для блюда! \n"
                                           "/addrecepts - Добавьте рецепт своего блюда и поделитесь"
                                           " им с другими пользователями! \n"
                                           "/leaderboard - Узнайте топ игроков в крестики-нолики  \n"
                                           "/registration - Зарегистрируйтесь для игры в крестики нолики онлайн"
                                           " и сохранении нужных городов \n"
                                           "/weather - Узнайте погоду в городе \n "
                                           "/registration - Зарегистрируйтесь для игры в крестики нолики онлайн "
                                           "и сохранении нужных городов \n"
                                           "/google - Выводит ссылки на самые популярные по запросу из интернете \n"
                                           "/video - Выводит ссылки на самые популярные видео из YouTube \n"
                                           "/close - Закрой кнопки \n"
                                           "/game - Напишите и играйте в крестики-нолики!")


@bot.message_handler(commands=['close'])
def all_messages(message):
    sq = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.from_user.id, "Кнопки закрыты", reply_markup=sq)
    bot.delete_message(message.from_user.id, msg.message_id)


@bot.message_handler(commands=['game'])
def game(message):
    global mesid
    with open(REPL + 'game_lobby.txt', 'r') as file:
        s = file.read().split(',')
        toft = ','.join(s)
    qua = s[-1].split('.')
    print(qua)
    id = str(message.from_user.id)
    ro = False
    if id not in toft:
        if len(qua) == 6:
            mesid = bot.send_message(message.chat.id, "Вы зашли в очередь. Ожидайте...")
            game_lobby = ",".join(s) + ',' + id + '.' + str(mesid.id)
            with open(REPL + 'game_lobby.txt', 'w') as file:
                file.write(game_lobby)
        elif len(qua) == 2 and qua[-1] != "":
            mesid = bot.send_message(message.chat.id, "Ожидайте хода соперника")
            idn1 = s[-1].split(".")
            bot.delete_message(idn1[0], idn1[1])
            s = s[0:-2]
            game_lobby = ','.join(s) + idn1[0] + '.' + id + '.' + "1" + '.' + "?/?/?/?/?/?/?/?/?" + "." + str(mesid.id) + "." + "0"
            with open(REPL + 'game_lobby.txt', 'w') as file:
                file.write(game_lobby)
            play(message)
        else:
            mesid = bot.send_message(message.chat.id, "Вы зашли в очередь. Ожидайте...")
            game_lobby = id + '.' + str(mesid.id)
            with open(REPL + 'game_lobby.txt', 'w') as file:
                file.write(game_lobby)
    elif id in toft:
        for i in s:
            if (id in s) and int(i.split(".")[2]) > 1:
                ro = True
        if ro:
            bot.register_next_step_handler(message, play)
        else:
            bot.send_message(message.chat.id, f"Вы уже в очереди, ожидайте")


def play(message):
    with open(REPL + 'game_lobby.txt', 'r') as file:
        s = file.read().split(',')
    k = -1
    for i in s:
        k += 1
        player1, player2, round_number, bo, mao, em_mes = i.split('.')
        markup = types.InlineKeyboardMarkup()
        emoji = []
        for i in bo.split("/"):
            if i == "?":
                emoji.append("❓")
            elif i == "x":
                emoji.append("❌")
            elif i == "o":
                emoji.append("🅾️")
        spisokmsg = []
        if em_mes == "-1":
            print(mao)
            spisokmsg = mao.split("^")[2:4]
            print(spisokmsg)
        btn1 = types.InlineKeyboardButton(f'{emoji[0]}', callback_data='left_top')
        btn2 = types.InlineKeyboardButton(f'{emoji[1]}', callback_data='mid_top')
        btn3 = types.InlineKeyboardButton(f'{emoji[2]}', callback_data='right_top')
        btn4 = types.InlineKeyboardButton(f'{emoji[3]}', callback_data='left_mid')
        btn5 = types.InlineKeyboardButton(f'{emoji[4]}', callback_data='mid_mid')
        btn6 = types.InlineKeyboardButton(f'{emoji[5]}', callback_data='right_mid')
        btn7 = types.InlineKeyboardButton(f'{emoji[6]}', callback_data='left_bot')
        btn8 = types.InlineKeyboardButton(f'{emoji[7]}', callback_data='mid_bot')
        btn9 = types.InlineKeyboardButton(f'{emoji[8]}', callback_data='right_bot')
        stick1 = types.InlineKeyboardButton(f'︻デ═一', callback_data='stick1')
        stick2 = types.InlineKeyboardButton(f'😢', callback_data='stick2')
        stick3 = types.InlineKeyboardButton(f'😑', callback_data='stick3')
        stick4 = types.InlineKeyboardButton(f'☕️', callback_data='stick4')
        stick5 = types.InlineKeyboardButton(f'❤️', callback_data='stick5')
        stick6 = types.InlineKeyboardButton(f'😨', callback_data='stick6')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, stick1, stick2, stick3, stick4, stick5, stick6)
        round_number = int(round_number)
        pole.board(bo)
        if round_number % 2 == 1:
            image = 'res.png'
            file = open('img/' + image, 'rb')
            msg = bot.send_photo(int(player1), file)
            spisokmsg.append(str(msg.id))
            if round_number == 1:
                msg = bot.send_message(int(player1), "Вы - крестик. Выберите поле для хода.", reply_markup=markup)
                spisokmsg.insert(0, mao)
                spisokmsg.append(str(msg.id))
            else:
                msg = bot.send_message(int(player1), "Выберите поле для хода.", reply_markup=markup)
                spisokmsg.append(str(msg.id))
                spisokmsg.insert(0, mao.split("^")[0])
                spisokmsg.insert(1, mao.split("^")[1])
        if round_number % 2 == 0:
            image = 'res.png'
            file = open('img/' + image, 'rb')
            msg = bot.send_photo(int(player2), file)
            spisokmsg.append(str(msg.id))
            if round_number == 2:
                msg = bot.send_message(int(player2), "Вы - нолик. Выберите поле для хода.", reply_markup=markup)
                spisokmsg.append(str(msg.id))
                spisokmsg.insert(0, mao.split("^")[0])
                spisokmsg.insert(1, mao.split("^")[1])
            else:
                msg = bot.send_message(int(player2), "Выберите поле для хода.", reply_markup=markup)
                spisokmsg.append(str(msg.id))
                spisokmsg.insert(0, mao.split("^")[0])
                spisokmsg.insert(1, mao.split("^")[1])
        i = f'{player1}.{player2}.{round_number}.{bo}.{"^".join(spisokmsg)}.{em_mes}'
        s[k] = i
    game_lobby = ",".join(s)
    with open(REPL + 'game_lobby.txt', 'w') as file:
        file.write(game_lobby)


@bot.callback_query_handler(func=lambda callback: True)
def callback_mes(callback):
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
    elif callback.data == "stick1":
        t = 11
    elif callback.data == "stick2":
        t = 12
    elif callback.data == "stick3":
        t = 13
    elif callback.data == "stick4":
        t = 14
    elif callback.data == "stick5":
        t = 15
    elif callback.data == "stick6":
        t = 16
    elif callback.data == "yeap":
        t = 20
    elif callback.data == "nope":
        t = 19
    move = str(callback.message.chat.id)
    count = 0
    with open(REPL + 'game_lobby.txt', 'r') as file:
        s = file.read().split(',')
    standart_mes_count = 4
    for i in s:
        count += 1
        if move in i:
            li = i.split(".")
            wait = ""
            if li[0] == move and int(li[2]) % 2 == 1:
                wait = li[1]
            elif li[1] == move and int(li[2]) % 2 == 0:
                wait = li[0]
            pol = li[3].split("/")
            msg = li[4].split("^")
            if int(li[5]) > 10:
                qu1 = bot.send_message(int(wait), "Соперник отправил вам стикер")
                qu2 = bot.send_sticker(int(wait), EMOJIES[int(li[5]) - 11])
                qu = str(qu1.id)
                msg.append(qu)
                msg.append(str(qu2.id))
                li[5] = "1"
            if t == 20:
                if li[0] == move and int(li[2]) % 2 == 1:
                    wait = li[1]
                elif li[1] == move and int(li[2]) % 2 == 0:
                    wait = li[0]
                bot.delete_message(int(move), int(msg[-1]))
                bot.delete_message(int(move), int(msg[-2]))
                qu1 = bot.send_message(int(move), "Стикер отправлен, теперь сделайте свой ход")
                msg.remove(msg[-1])
                msg.remove(msg[-1])
                msg.append(str(qu1.id))
                msg = "^".join(msg)
                pol = "/".join(pol)
                timered = [li[0], li[1], str(li[2]), pol, msg, str(int(li[5]) + 11)]  # 76 # 80
                r = '.'.join(timered)
                s[count - 1] = r
                game_lobby = ','.join(s)
                with open(REPL + 'game_lobby.txt', 'w') as file:
                    file.write(game_lobby)
            elif t == 19:
                bot.delete_message(int(move), int(msg[-1]))
                bot.delete_message(int(move), int(msg[-2]))
                msg.remove(msg[-1])
                msg.remove(msg[-2])
                msg = "^".join(msg)
                pol = "/".join(pol)
                timered = [li[0], li[1], str(li[2]), pol, msg, "0"]  # 76 # 80
                r = '.'.join(timered)
                s[count - 1] = r
                game_lobby = ','.join(s)
                with open(REPL + 'game_lobby.txt', 'w') as file:
                    file.write(game_lobby)
            elif t > 10:
                markup = types.InlineKeyboardMarkup(row_width=3)
                btn1 = types.InlineKeyboardButton("Отправить", callback_data='yeap')
                btn2 = types.InlineKeyboardButton("Не отправлять", callback_data='nope')
                markup.add(btn1, btn2)
                qu1 = bot.send_message(int(move), "Вы выбрали такой эмодзи, отправить его сопернику? Эмодзи можно отправлять"
                                                  "1 раз за ход", reply_markup=markup)
                qu2 = bot.send_sticker(int(move), EMOJIES[t-11])
                qu = str(qu1.id) + "^" + str(qu2.id)
                msg.append(qu)
                msg = "^".join(msg)
                pol = "/".join(pol)
                timered = [li[0], li[1], str(li[2]), pol, msg, str(t - 11)]  # 76 # 80
                r = '.'.join(timered)
                s[count - 1] = r
                game_lobby = ','.join(s)
                with open(REPL + 'game_lobby.txt', 'w') as file:
                    file.write(game_lobby)
            else:
                if pol[t - 1] == "?":
                    if li[0] == move and int(li[2]) % 2 == 1:
                        pol[t - 1] = "x"
                        pol = "/".join(pol)
                        wait = li[1]
                    elif li[1] == move and int(li[2]) % 2 == 0:
                        pol[t - 1] = "o"
                        pol = "/".join(pol)
                        wait = li[0]
                    if li[2] == "1":
                        bot.delete_message(wait, int(msg[0]))
                        bot.delete_message(move, int(msg[1]))
                        bot.delete_message(move, int(msg[2]))
                        for x in range(3):
                            msg.remove(msg[0])
                    if li[2] != "1":
                        bot.delete_message(wait, int(msg[0]))
                        bot.delete_message(move, int(msg[1]))
                        bot.delete_message(move, int(msg[2]))
                        bot.delete_message(move, int(msg[3]))
                        for x in range(4):
                            msg.remove(msg[0])
                    if li[5] == "-1":
                        bot.delete_message(move, int(msg[-1]))
                        bot.delete_message(move, int(msg[-2]))
                        li[5] = "0"
                        msg = []
                    elif li[5] == "1":
                        bot.delete_message(move,int(msg[-3]))
                        msg.remove(msg[-3])
                        li[5] = "-1"
                    # bot.delete_message(int(move), int(li[4]) + 2)  # 75 # 78 # 82
                    # bot.delete_message(int(move), int(li[4]) + 1)  # 74 # 77 #81
                    # if int(li[2]) == 1:
                    #     bot.delete_message(int(wait), int(li[4]))  # 73
                    # elif int(li[2]) != 1:
                    #     bot.delete_message(int(wait), int(li[4]))  # 76
                    #     bot.delete_message(int(move), int(li[4]) + 3)  # 79
                    if (pol[0] == "o" and pol[2] == "o" and pol[4] == "o" or
                            pol[6] == "o" and pol[8] == "o" and pol[10] == "o" or
                            pol[12] == "o" and pol[14] == "o" and pol[16] == "o" or
                            pol[0] == "o" and pol[6] == "o" and pol[12] == "o" or
                            pol[2] == "o" and pol[8] == "o" and pol[14] == "o" or
                            pol[4] == "o" and pol[10] == "o" and pol[16] == "o" or
                            pol[0] == "o" and pol[8] == "o" and pol[16] == "o" or
                            pol[12] == "o" and pol[8] == "o" and pol[4] == "o"):
                        s.remove(i)
                        game_lobby = ','.join(s)
                        with open(REPL + 'game_lobby.txt', 'w') as file:
                            file.write(game_lobby)
                        bot.send_message(int(wait), "Победа игрока о")
                        bot.send_message(int(move), "Победа игрока о")
                        conn = sqlite3.connect(REPL + "users.db")
                        cur = conn.cursor()
                        tabl = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''',
                                           (int(move),)).fetchone()
                        if tabl:
                            ss = cur.execute('''SELECT * FROM leaderboard WHERE nickname = ?''',
                                             (tabl[1],)).fetchone()
                            if not ss:
                                cur.execute('''INSERT INTO leaderboard (nickname, wins) VALUES (?, ?)''',
                                            (tabl[1], 1))
                            if ss:
                                cur.execute('''INSERT INTO leaderboard (nickname, wins) VALUES (?, ?)''',
                                            (tabl[1], ss[2] + 1))
                            conn.commit()
                            conn.close()
                    elif (pol[0] == "x" and pol[2] == "x" and pol[4] == "x" or
                          pol[6] == "x" and pol[8] == "x" and pol[10] == "x" or
                          pol[12] == "x" and pol[14] == "x" and pol[16] == "x" or
                          pol[0] == "x" and pol[6] == "x" and pol[12] == "x" or
                          pol[2] == "x" and pol[8] == "x" and pol[14] == "x" or
                          pol[4] == "x" and pol[10] == "x" and pol[16] == "x" or
                          pol[0] == "x" and pol[8] == "x" and pol[16] == "x" or
                          pol[12] == "x" and pol[8] == "x" and pol[4] == "x"):
                        s.remove(i)
                        game_lobby = ','.join(s)
                        with open(REPL + 'game_lobby.txt', 'w') as file:
                            file.write(game_lobby)
                        bot.send_message(int(wait), "Победа игрока x")
                        bot.send_message(int(move), "Победа игрока x")
                        conn = sqlite3.connect(REPL + "users.db")
                        cur = conn.cursor()
                        tabl = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''',
                                           (int(move),)).fetchone()
                        if tabl:
                            ss = cur.execute('''SELECT * FROM leaderboard WHERE nickname = ?''',
                                             (tabl[1],)).fetchone()
                            if not ss:
                                cur.execute('''INSERT INTO leaderboard (nickname, wins) VALUES (?, ?)''',
                                            (tabl[1], 1))
                            if ss:
                                cur.execute('''INSERT INTO leaderboard (nickname, wins) VALUES (?, ?)''',
                                            (tabl[1], ss[2] + 1))
                            conn.commit()
                            conn.close()
                    elif int(li[2]) == 9:
                        bot.send_message(int(wait), "ничья")
                        bot.send_message(int(move), "ничья")
                    else:
                        qu1 = bot.send_message(int(move), "Ваш ход принят. Ожидайте соперника")
                        qu2 = bot.send_message(int(wait), "Соперник сделал ход")
                        if li[5] == "-1":
                            msg.insert(0, str(qu1.id))
                        else:
                            msg.append(str(qu1.id))
                        msg.append(str(qu2.id))
                        timered = [li[0], li[1], str(int(li[2]) + 1), pol, "^".join(msg), li[5]]  # 76 # 80
                        r = '.'.join(timered)
                        s[count - 1] = r
                        game_lobby = ','.join(s)
                        with open(REPL + 'game_lobby.txt', 'w') as file:
                            file.write(game_lobby)
                        play(int(wait))
                else:
                    if li[0] == move:
                        wait = li[1]
                    elif li[1] == move:
                        wait = li[0]
                    qu1 = bot.send_message(int(wait), "Ваш ход принят. Ожидайте соперника")
                    qu2 = bot.send_message(int(move), "Соперник сделал ход")
                    qu = str(qu1.id) + "^" + str(qu2.id)
                    bot.delete_message(wait, int(msg[0]))
                    bot.delete_message(move, int(msg[1]))
                    bot.delete_message(move, int(msg[2]))
                    bot.delete_message(move, int(msg[3]))
                    pol = "/".join(pol)
                    timered = [li[0], li[1], str(int(li[2])), pol, str(qu), li[5]]
                    r = '.'.join(timered)
                    s[count - 1] = r
                    game_lobby = ','.join(s)
                    with open(REPL + 'game_lobby.txt', 'w') as file:
                        file.write(game_lobby)
                    play(int(move))


# @bot.message_handler(commands=['google'])
# def google(message):
#   query = bot.send_message(message.chat.id, "Напишите что вы хотите узнать")
#   bot.register_next_step_handler(query, tests_google)
# def tests_google(message):
#    if message.text.strip().lower() == "/clear":
#        bot.send_message(message.chat.id, "Команда отменена")
#        bot.clear_step_handler(message)                            ************Код работает в локальной сети********
#        all_messages(message)
#    else:
#        name = message.text.strip()
#        for i in googlesearch.search(name, lang='russian', num_results=2):
#            bot.send_message(message.chat.id, i)


@bot.message_handler(commands=['video'])
def video(message):
    query = bot.send_message(message.chat.id, "Напишите что вы хотите узнать")
    bot.register_next_step_handler(query, tests_video)


def tests_video(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        name = message.text.strip()
        results = YoutubeSearch(name).to_dict()
        for i in range(3):
            bot.send_message(message.chat.id, f"https://www.youtube.com{results[i]['url_suffix']}")


@bot.message_handler(commands=['admin'])
def listorian(message):
    global iddus
    print(message)
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    sos1 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ? AND admin > ?''', (message.from_user.id, 0, )).fetchone()
    print(sos1)
    if sos1:
        bot.send_message(message.chat.id, f'Введите пароль от аккаунта для входа в админскую систему')
        iddus = sos1[0]
        bot.register_next_step_handler(message, autorization)
    else:
        bot.send_message(message.chat.id, f'У вас нет прав для входа.')


def autorization(message):

    sip = message.text
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    sos1 = cur.execute('''SELECT * FROM passwords WHERE id = ?''', (iddus, )).fetchone()
    aut = True
    with open(REPL + 'hesh.txt', 'r') as file:
        k = file.read().split(" ")
        heshing = {}
        for i in range(len(k) // 2):
            heshing[k[i * 2]] = k[i * 2 + 1]
        hesh_password = ""
        for i in sip:
            if i not in PASSWORD:
                aut = False
            else:
                hesh_password += heshing[i]
    print(hesh_password,)
    if hesh_password == sos1[2] and aut:
        global markup_admin
        sos2 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ? AND admin > ?''',
                           (message.from_user.id, 0,)).fetchone()
        markup_admin = types.ReplyKeyboardMarkup(row_width=1)
        markup_admin.add(types.InlineKeyboardButton("Изменить список играющих"))
        markup_admin.add(types.InlineKeyboardButton("Изменить таблицу лидеров"))
        if sos2[-2] == 2:
            markup_admin.add(types.InlineKeyboardButton("Изменить таблицу аккаунтов"))
            markup_admin.add(types.InlineKeyboardButton("Заявки в администрацию"))
        markup_admin.add(types.InlineKeyboardButton("Выход"))
        bot.send_message(message.chat.id, f'Доступ разрешён', reply_markup=markup_admin)
        bot.send_message(message.chat.id, f'----------------------------WARNING----------------------------\nНаходясь'
                                          f' в системе администрирования, вы не можете использовать функции которые не '
                                          f'относятся к функциям администратора \nДля отмены действия пропишите: "назад"'
                                          f'\nДля выхода из системы администрирования пропишите: "выход" или воспользуйтесь '
                                          f'специальной кнопкой')
        bot.register_next_step_handler(message, list_blinks)
    else:
        bot.send_message(message.chat.id, f'В доступе отказано')
        bot.clear_step_handler(message)
        all_messages(message)


def list_blinks(message):
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    sos2 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ? AND admin > ?''',
                       (message.from_user.id, 0,)).fetchone()
    with open(REPL + "game_lobby.txt", "r") as file:
        k = file.read().split(",")
    if message.text == "Изменить список играющих":
        sec = ""
        if k == [""]:
            bot.send_message(message.chat.id, "На данный момент нет активных пар")
            bot.register_next_step_handler(message, list_blinks)
        else:
            for i in k:
                ii = i.split(".")
                sec += f"Пара {k.index(i) + 1}: id1:{ii[0]}, id2:{ii[1]}, turn:{ii[2]}, board:{ii[3]}, sticker_info:{ii[4]}\n\n"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.InlineKeyboardButton("Назад"))
            bot.send_message(message.chat.id, sec)
            bot.send_message(message.chat.id, "Напишите номер пары для удаления", reply_markup=markup)
            bot.register_next_step_handler(message, list_players)
    elif message.text == "Изменить таблицу лидеров":
        sos1 = cur.execute('''SELECT * FROM leaderboard ORDER BY wins DESC''').fetchall()
        print(sos1)
        sec = ""
        if sos1 == [""]:
            bot.send_message(message.chat.id, "На данный момент нет лидеров", reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
        else:
            for i in sos1:
                print(i)
                sec += f"{sos1.index(i) + 1}: id:{i[0]}, nickname:{i[1]}, wins:{i[2]}\n\n"
                print(sec)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.InlineKeyboardButton("Назад"))
            bot.send_message(message.chat.id, sec)
            bot.send_message(message.chat.id, "Напишите номер игрока для удаления", reply_markup=markup)
            bot.register_next_step_handler(message, list_leaderbord)
    elif message.text == "Изменить таблицу аккаунтов" and sos2[-2] == 2:
        sos1 = cur.execute('''SELECT * FROM userinfo''').fetchall()
        print(sos1)
        sec = ""
        for i in sos1:
            print(i)
            sec += f"{sos1.index(i) + 1}: id:{i[0]}, login:{i[1]}, email:{i[2]}, nickname:{i[3]}, tg_id:{i[4]}, " \
                   f"admin:{i[5]}, towns_weather:{i[6]}\n\n"
            print(sec)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        markup.add(types.InlineKeyboardButton("Назад"))
        bot.send_message(message.chat.id, sec)
        bot.send_message(message.chat.id, "Напишите номер пользователя для выбора действия", reply_markup=markup)
        bot.register_next_step_handler(message, list_accounts)
    elif message.text == "Заявки в администрацию" and sos2[-2] == 2:
        sos1 = cur.execute('''SELECT * FROM request''').fetchone()
        if sos1 == None:
            bot.send_message(message.chat.id, "Нет заявок на пост администратора")
            bot.register_next_step_handler(message, list_blinks)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup.add(types.InlineKeyboardButton("Принять"))
            markup.add(types.InlineKeyboardButton("Отклонить"))
            bot.send_message(message.chat.id, f"Ник: {sos1[1]} \n tg_id: {sos1[2]} \n"
                                          f"Возраст: {sos1[3]} \n Причина: {sos1[-1]}", reply_markup=markup)
            bot.register_next_step_handler(message, list_tickets)
    elif message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда")
        bot.register_next_step_handler(message, list_blinks)
    conn.close()


def list_players(message):
    ss = message.text
    print(ss)
    with open(REPL + "game_lobby.txt", "r") as file:
        k = file.read().split(",")
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    elif ss.isdigit():
        print(1, "da")
        if int(ss) > 0 and int(ss) < len(k) + 1:
            k.remove(k[int(ss) - 1])
            k = ",".join(k)
            with open(REPL + 'game_lobby.txt', 'w') as file:
                file.write(k)
            bot.send_message(message.chat.id, "Пара успешно удалена. Выберите дальнейшее действие", reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
        else:
            bot.send_message(message.chat.id, "Неверное значение")
            bot.register_next_step_handler(message, list_players)
    else:
        bot.send_message(message.chat.id, "Неверное значение")
        bot.register_next_step_handler(message, list_players)


def list_leaderbord(message):
    ss = message.text
    print(ss)
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    k = cur.execute('''SELECT * FROM leaderboard''').fetchall()
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    elif ss.isdigit():
        if int(ss) > 0 and int(ss) < len(k) + 1:
            cur.execute('''DELETE FROM leaderboard WHERE id = ?''', (k[int(ss) - 1][0],))
            conn.commit()
            bot.send_message(message.chat.id, "Лидер успешно удалён. Выберите дальнейшее действие", reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
        else:
            bot.send_message(message.chat.id, "Неверное значение")
            bot.register_next_step_handler(message, list_leaderbord)
    else:
        bot.send_message(message.chat.id, "Неверное значение")
        bot.register_next_step_handler(message, list_leaderbord)


def list_accounts(message):
    ss = message.text
    print(ss)
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    k = cur.execute('''SELECT * FROM userinfo''').fetchall()
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    elif ss.isdigit():
        if int(ss) > 0 and int(ss) < len(k) + 1:
            global accounteee
            markup = types.ReplyKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Повысить пользователя до админа"))
            markup.add(types.InlineKeyboardButton("Понизить админа"))
            markup.add(types.InlineKeyboardButton("Удалить пользователя"))
            markup.add(types.InlineKeyboardButton("Назад"))
            all_messages(message)
            accounteee = ss
            print(accounteee)
            if k[int(ss) - 1][-3] == message.chat.id:
                all_messages(message)
                bot.send_message(message.chat.id, "Вы не можете выполнять действия со своим аккаунтом",
                                 reply_markup=markup_admin)
                bot.register_next_step_handler(message, list_blinks)
            else:
                bot.send_message(message.chat.id, "Пользователь выбран. Выберите дальнейшее действие", reply_markup=markup)
                bot.register_next_step_handler(message, rasp_punkt)
        else:
            bot.send_message(message.chat.id, "Неверное значение")
            bot.register_next_step_handler(message, list_accounts)
    else:
        bot.send_message(message.chat.id, "Неверное значение")
        bot.register_next_step_handler(message, list_accounts)

def rasp_punkt(message):
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    elif message.text.lower() == "повысить пользователя до админа":
        all_messages(message)
        accounts_redact(message, 1)
    elif message.text.lower() == "понизить админа":
        all_messages(message)
        accounts_redact(message, 2)
    elif message.text.lower() == "удалить пользователя":
        all_messages(message)
        accounts_delete(message)
    else:
        bot.send_message(message.chat.id, "Неверное значение")
        bot.register_next_step_handler(message, rasp_punkt)


def accounts_redact(message, rep):
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    k = cur.execute('''SELECT * FROM userinfo''').fetchall()
    if rep == 1:
        proverb = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (k[int(accounteee) - 1][-3],)).fetchone()
        print(proverb)
        print(k)
        print(k[int(accounteee) - 1][2])
        if proverb[-2] == 2:
            bot.send_message(message.chat.id, "Пользователь имеет максимальный уровень, повышение не работает"
                                              ". Выберите дальнейшее действие",
                             reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
        if proverb[-2] < 2:
            cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (proverb[-3],))
            cur.execute('''INSERT INTO userinfo (id, login, email, nickname, tg_id, admin, 
                towns_weather) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (proverb[0], proverb[1], proverb[2], proverb[3], proverb[4], proverb[-2] + 1, proverb[-1],))
            conn.commit()
            bot.send_message(message.chat.id, "Пользователь успешно повышен на 1 уровень. Выберите дальнейшее действие", reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
    elif rep == 2:
        proverb = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (k[int(accounteee) - 1][-3],)).fetchone()
        print(proverb)
        print(k)
        print(k[int(accounteee) - 1][2])
        if proverb[-2] == 0:
            bot.send_message(message.chat.id, "Пользователь не имеет повышенного уровня, понижение не сработало"
                                              ". Выберите дальнейшее действие",
                             reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)
        if proverb[-2] != 0:
            cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (proverb[-3],))
            cur.execute('''INSERT INTO userinfo (id, login, email, nickname, tg_id, admin, 
                towns_weather) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (proverb[0], proverb[1], proverb[2], proverb[3], proverb[4], proverb[-2] - 1, proverb[-1],))
            conn.commit()
            bot.send_message(message.chat.id, "Пользователь успешно понижен на 1 уровень. Выберите дальнейшее действие", reply_markup=markup_admin)
            bot.register_next_step_handler(message, list_blinks)


def accounts_delete(message):
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    k = cur.execute('''SELECT * FROM userinfo''').fetchall()
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    else:
        proverb = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (k[int(accounteee) - 1][-3],)).fetchone()
        print(proverb)
        print(k)
        print(k[int(accounteee) - 1][2])
        cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (proverb[-3],))
        conn.commit()
        bot.send_message(message.chat.id, "Пользователь успешно удалён. Выберите дальнейшее действие", reply_markup=markup_admin)
        bot.register_next_step_handler(message, list_blinks)


def list_tickets(message):
    ss = message.text
    print(ss)
    all_messages(message)
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    k = cur.execute('''SELECT * FROM request''').fetchone()
    print(11111111111111111111, k[1])
    if message.text.lower() == "выход":
        bot.clear_step_handler(message)
        all_messages(message)
    elif message.text.lower() == "назад":
        all_messages(message)
        bot.register_next_step_handler(message, list_blinks)
        bot.send_message(message.chat.id, "Вы в главном меню", reply_markup=markup_admin)
    elif ss.lower() == "принять":
        cur.execute('''DELETE FROM request WHERE id = ?''', (k[0],))
        print(k[2])
        proverb = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (k[2],)).fetchone()
        cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (proverb[-3],))
        cur.execute('''INSERT INTO userinfo (id, login, email, nickname, tg_id, admin, 
            towns_weather) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (proverb[0], proverb[1], proverb[2], proverb[3], proverb[4], 1, proverb[-1], ))
        conn.commit()
        conn.commit()
        bot.send_message(message.chat.id, "Пользователь успешно принят на пост администратора. Выберите дальнейшее действие", reply_markup=markup_admin)
        bot.send_message(proverb[4], "Вы успешно приняты на пост администратора. За информацией о своих обязанностях "
                                     "вы можете обратиться к создателям. Их контакты можно найти в команде /contacts. "
                                     "Специальная команда для админ меню - /list")
        bot.register_next_step_handler(message, list_blinks)
    elif ss.lower() == 'отклонить':
        print(k[1])
        cur.execute('''DELETE FROM request WHERE tg_id = ?''', (k[2],))
        conn.commit()
        bot.send_message(message.chat.id, "Пользователь отклонён. Выберите дальнейшее действие",
                         reply_markup=markup_admin)
        bot.register_next_step_handler(message, list_blinks)
    else:
        bot.send_message(message.chat.id, "Неверное значение")
        bot.register_next_step_handler(message, list_leaderbord)


@bot.message_handler(commands=["ticket"])
def ticket(message):
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    sos2 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''',
                       (message.from_user.id,)).fetchone()
    sos3 = cur.execute('''SELECT * FROM request WHERE tg_id = ?''',
                       (message.from_user.id,)).fetchone()
    if not sos2 or sos2[5] > 0:
        bot.send_message(message.chat.id, "Для подачи заявки вы должны быть зарегистрированным и не являться администратором")
        bot.clear_step_handler(message)
    elif sos3:
        bot.send_message(message.chat.id,"Вы уже подали заявку, ожидайте ответа")
        bot.clear_step_handler(message)
    else:
        bot.send_message(message.chat.id, "Введите свой возраст")
        bot.register_next_step_handler(message, old)


def old(message):
    global old
    old = message.text
    print(old)
    bot.send_message(message.chat.id, "Почему именно вы должны стать администратором?")
    bot.register_next_step_handler(message, prichina)


def prichina(message):
    nickname = message.from_user.first_name
    tgid = message.from_user.id
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    prichina = message.text
    print(1, prichina)
    print(2, old)
    cur.execute("INSERT INTO request (nickname, tg_id, old, prichina) VALUES ('%s', '%s', '%s', '%s')" % (nickname, tgid, old, prichina,))
    conn.commit()
    bot.send_message(message.chat.id, "Заявка успешно отправлена. Ожидайте результата")


# @bot.message_handler(commands=['contacts'])
# def site(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('lanfrod', url='https://vk.com/lanfrod'))
#     markup.add(types.InlineKeyboardButton('intestine1', url='https://vk.com/intestine1'))
#     bot.send_message(message.chat.id, f'Привет, вот контакты разработчиков', reply_markup=markup)


@bot.message_handler(commands=['registration'])
def registration(message):
    conn = sqlite3.connect(REPL + "users.db")
    cur = conn.cursor()
    sos2 = cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''',
                       (message.from_user.id,)).fetchone()
    if message.text.lower() == '/registration':
        if sos2:
            bot.send_message(message.chat.id, 'Данный аккаунт уже зарегистрирован')
            bot.clear_step_handler(message)
        else:
            bot.send_message(message.chat.id, f'{message.from_user.username.capitalize()}, '
                                              f'чтобы зарегистрироваться'
                                              f' напиши желаемый login. Он будет использован '
                                              f'как никнейм. Ник может состоять '
                                              f'из латинских букв разного регистра, цифр')
            bot.register_next_step_handler(message, user_name)
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)


def user_name(message):
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    proxod = True
    global name
    name = message.text.strip()
    for i in name:
        if i not in NAME:
            proxod = False
    if proxod:
        proverb = cur.execute('''SELECT * FROM passwords WHERE login = ?''', (name,)).fetchall()
        conn.close()
        if not proverb:
            bot.send_message(message.chat.id,
                             'Введите пароль. Он может состоять из латинских букв разного регистра, цифр '
                             'специальных символов и нижнего подчёркивания.')
            bot.register_next_step_handler(message, user_pass)
        else:
            bot.send_message(message.chat.id, 'Такой пользователь уже существует. Введите другой логин')
            bot.register_next_step_handler(message, user_name)
    else:
        if message.text.strip().lower() == "/clear":
            bot.send_message(message.chat.id, "Команда отменена")
            bot.clear_step_handler(message)
            all_messages(message)
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
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    elif b:
        bot.send_message(message.chat.id, 'Введите почту для привязки')
        with open(REPL + 'hesh.txt', 'r') as file:
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
    conn = sqlite3.connect(REPL + 'users.db')
    cur = conn.cursor()
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        try:
            sos1 = cur.execute('''SELECT * FROM userinfo WHERE email = ?''', (email,)).fetchall()
            if sos1:
                raise Exception()
            mani.send_email(email, 'Registration',
                            f'{nickname}, это капча для подтверждения регистрации. Введите код с капчи'
                            f' в чате с ботом')

            up = mani.pat()
            res = ''  # капча длинная(наслаивается вероятно), сделать кнопку отмены/выхода из действия
            for i in up:
                res += i
            cur.execute('''INSERT INTO captchatab (nickname, captcha) VALUES (?, ?)''', (tgid, res,))
            bot.send_message(message.chat.id, 'Проверьте вашу почту и введите код с капчи')
            conn.commit()
            conn.close()
            bot.register_next_step_handler(message, cap)
        except Exception:  # ошибка с некорректной почтой
            bot.send_message(message.chat.id, 'Неправильная почта. Введите другую почту ещё раз')
            bot.register_next_step_handler(message, user_email)

        except smtplib.SMTPRecipientsRefused:
            bot.send_message(message.chat.id, 'Неправильная почта. Введите другую почту ещё раз')
            bot.register_next_step_handler(message, user_email)


def cap(message):
    global mistake
    captcha = message.text.strip()
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        if captcha != mani.pat():
            bot.send_message(message.chat.id, 'Неверная капча. Проверьте вашу почту и введите код с капчи')
            bot.register_next_step_handler(message, cap)
            nickname = message.from_user.first_name
            tgid = message.from_user.id
            conn = sqlite3.connect(REPL + 'users.db')
            cur = conn.cursor()
            mani.send_email(email, 'Registration',
                            f'{nickname}, это капча для подтверждения регистрации. Введите код с капчи'
                            f' в чате с ботом')
            up = mani.pat()
            res = ''  # капча длинная(наслаивается вероятно), сделать кнопку отмены/выхода из действия
            for i in up:
                res += i
            cur.execute('''INSERT INTO captchatab (nickname, captcha) VALUES (?, ?)''', (tgid, res,))
            bot.send_message(message.chat.id, 'Проверьте вашу почту и введите код с новой капчи')
        elif captcha == mani.pat():
            bot.send_message(message.chat.id, 'Почта подтверждена')
            conn = sqlite3.connect(REPL + 'users.db')
            cur = conn.cursor()
            nickname = message.from_user.first_name
            tg_id = message.from_user.id
            cur.execute("INSERT INTO passwords (login, pass) VALUES ('%s', '%s')" % (name, hesh_password))
            cur.execute("INSERT INTO userinfo (login, email, nickname, tg_id) VALUES ('%s', '%s', '%s', '%s')" % (
                name, email, nickname, tg_id))
            conn.commit()
            conn.close()
            markup = telebot.types.InlineKeyboardMarkup()
            bot.send_message(message.chat.id, f'Пользователь {name} зарегистрирован', reply_markup=markup)


@bot.message_handler(commands=['leaderboard'])
def leaderboard(message):
    conn = sqlite3.connect(REPL + "users.db")
    cur = conn.cursor()
    num = cur.execute('''SELECT * FROM leaderboard ORDER BY wins DESC''').fetchall()
    s = 'Ники игроков: \n'
    for i in range(0, len(num)):
        s = f'{s} {num[i][1]} \t {num[i][-1]} \n'
    bot.send_message(message.chat.id, s)


@bot.message_handler(commands=['towns'])
def favourite(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.InlineKeyboardButton(f'Добавить город')
        btn2 = types.InlineKeyboardButton(f'Удалить город')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите действие, которое хотите сделать с вашим списком любимых городов', reply_markup=markup)
        bot.register_next_step_handler(message, towny)


def towny(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        all_messages(message)
        tgid = message.from_user.id
        conn = sqlite3.connect(REPL + 'users.db')
        cur = conn.cursor()
        if cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone():
            proverb = cur.execute('''SELECT towns_weather FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone()
            if not proverb[0]:
                bot.send_message(message.chat.id, 'Напишите город')
                bot.register_next_step_handler(message, addit)
            elif message.text == "Добавить город" and len(proverb[0].split(",")) < 3:
                bot.send_message(message.chat.id, 'Напишите город')
                bot.register_next_step_handler(message, addit)
            elif message.text == "Добавить город" and len(proverb[0].split(",")) >= 3:
                bot.send_message(message.chat.id, 'Достигнут лимит городов(3)')
                bot.clear_step_handler(message)
                all_messages(message)
            elif proverb and message.text == "Удалить город" and len(proverb) >= 1 and 0 not in proverb:
                proverb = list(cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone())
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                for i in proverb[-1].split(','):
                    markup.add(types.InlineKeyboardButton(f'{i}'))
                bot.send_message(message.chat.id, 'Напишите город', reply_markup=markup)
                bot.register_next_step_handler(message, deleteit)
            elif proverb and message.text == "Удалить город" and len(proverb) < 1:
                bot.send_message(message.chat.id, 'Не найдено городов для удаления')
                bot.clear_step_handler(message)
                all_messages(message)
            else:
                bot.send_message(message.chat.id, 'Не найдено результатов по данной команде')
                bot.clear_step_handler(message)
                all_messages(message)
        else:
            bot.send_message(message.chat.id, 'Вы не зарегистрированы. Данная команда разрешена только зарегистрированным пользователям')
            bot.clear_step_handler(message)
            all_messages(message)


def addit(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        tgid = message.from_user.id
        conn = sqlite3.connect(REPL + 'users.db')
        cur = conn.cursor()
        city = message.text
        s = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={API}&units=metric')
        proverb = list(cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone())
        if s.status_code == 200 and (city not in str(proverb[-1])):
            if proverb[-1]:
                check = proverb[-1].split(",")
                check.append(city.capitalize())
                proverb[-1] = ",".join(check)
            elif not proverb[-1]:
                proverb[-1] = city.capitalize()
            cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (tgid,))
            cur.execute('''INSERT INTO userinfo (id, login, email, nickname, tg_id, admin, 
        towns_weather) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (proverb[0], proverb[1], proverb[2], proverb[3], proverb[4], proverb[5], proverb[-1], ))
            conn.commit()
            bot.send_message(message.chat.id, f'Город {city.capitalize()} добавлен')
            bot.clear_step_handler(message)
            all_messages(message)
        elif city in str(proverb[-1]):
            bot.send_message(message.chat.id, f'Город {city.capitalize()} уже есть в списке')
            bot.clear_step_handler(message)
            all_messages(message)
        elif s.status_code != 200:
            bot.send_message(message.chat.id, f'Город {city.capitalize()} не существует')
            bot.clear_step_handler(message)
            all_messages(message)


def deleteit(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        tgid = message.from_user.id
        conn = sqlite3.connect(REPL + 'users.db')
        cur = conn.cursor()
        proverb = list(cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone())
        bot.send_message(message.chat.id, f'Выберите город, нажав на кнопку, чтобы удалить его из списка')
        city = message.text
        s = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={API}&units=metric')
        if s.status_code == 200 and city in proverb[-1]:
            if proverb[-1]:
                check = proverb[-1].split(",")
                check.remove(city.capitalize())
                proverb[-1] = ",".join(check)
            cur.execute('''DELETE FROM userinfo WHERE tg_id = ?''', (tgid,))
            cur.execute('''INSERT INTO userinfo (id, login, email, nickname, tg_id, admin, 
        towns_weather) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (proverb[0], proverb[1], proverb[2], proverb[3], proverb[4], proverb[5], proverb[-1], ))
            conn.commit()
            bot.send_message(message.chat.id, f'Город {city.capitalize()} удалён')
            bot.clear_step_handler(message)
            all_messages(message)
        else:
            bot.send_message(message.chat.id, f'Город {city.capitalize()} нет в списке')
            bot.clear_step_handler(message)
            all_messages(message)


@bot.message_handler(commands=['weather'])
def get_weather(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        conn = sqlite3.connect(REPL + "users.db")
        cur = conn.cursor()
        tgid = message.from_user.id
        proverb = list(cur.execute('''SELECT * FROM userinfo WHERE tg_id = ?''', (tgid,)).fetchone())
        if len(proverb) >= 1 and proverb[-1] != 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=len(proverb[-1].split(",")))
            print(proverb[-1].split(","))
            for i in proverb[-1].split(","):
                markup.add(types.InlineKeyboardButton(f'{i}'))
            bot.send_message(message.chat.id, 'Напишите город, в котором хотите увидеть погоду', reply_markup=markup)
            bot.register_next_step_handler(message, answer)
        else:
            bot.send_message(message.chat.id, 'Напишите город, в котором хотите увидеть погоду')
            bot.register_next_step_handler(message, answer)


def answer(message):
    if message.text.strip().lower() == "/clear":
        bot.send_message(message.chat.id, "Команда отменена")
        bot.clear_step_handler(message)
        all_messages(message)
    else:
        city = message.text.strip().lower()
        eng = False
        for i in city:
            if i in ENGLISH:
                eng = True
        if eng:
            city_parse = city
        if not eng:
            morph = pymorphy2.MorphAnalyzer()
            city_parse = morph.parse(city)[0].inflect({"loct"}).word
        s = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if s.status_code == 200:
            data = json.loads(s.text)
            if data["weather"][0]["description"] == "weather condition":
                word1 = "мало облаков"
            elif data["weather"][0]["description"] == "overcast clouds":
                word1 = "пасмурные облака"
            else:
                word1 = Translator(from_lang="english", to_lang="russian").translate(data["weather"][0]["description"])
            bot.reply_to(message, f'Сейчас погода в {city_parse.capitalize()}: {word1.lower()}. Температура воздуха:'
                                  f' {data["main"]["temp"]}°C')
            if word1.lower() == "ясно":
                image = REPL + 'img/sunny3.png'
                file = open(image, 'rb')
                bot.send_photo(message.chat.id, file)
            elif word1.lower() == "мало облаков":
                image = REPL + 'img/obla.png'
                file = open(image, 'rb')
                bot.send_photo(message.chat.id, file)
            elif word1.lower() == "облачно":
                image = REPL + 'img/obl.png'
                file = open(image, 'rb')
                bot.send_photo(message.chat.id, file)
            elif word1.lower() == "пасмурные облака":
                image = REPL + 'img/ty4a.jpg'
                file = open(image, 'rb')
                bot.send_photo(message.chat.id, file)
            elif word1.lower() == "дым":
                image = REPL + 'img/tyman.jpg'
                file = open(image, 'rb')
                bot.send_photo(message.chat.id, file)
            all_messages(message)
        else:
            bot.reply_to(message, "Город не найден. Попробуйте снова.")
            all_messages(message)


bot.polling(none_stop=True)
