import telebot
from telebot import types
import time
import mmap
from config import *
from python_aternos import Client

atclient = Client()
atclient.login_with_session(AternosToken)
aternos = atclient.account
servs = aternos.list_servers()
serv = servs[0]

bot = TelebotToken
newadmin = []
plarsss = []

@bot.message_handler(commands=['deb'])
def deb(message):
    countt = -1
    fcrecf = ','.join
    for _ in Admins:
        countt += 1
        adminfo = f'ID: {Admins[countt][1]}, Name: {Admins[countt][2]}, IDK: {Admins[countt][3]}'
        newadmin.append(f'{countt+1} / {adminfo} *')
    newtext = fcrecf(newadmin)
    newtextt = newtext.replace('*', '\n')
    newtexttt = newtextt.replace(',', '')
    bot.reply_to(message, f'Админы:\n {newtexttt}')
@bot.message_handler(commands=['debugmess'])
def debug(message):
    bot.send_message(message.chat.id, message)
@bot.message_handler(commands=['myid'])
def myid(message):
    bot.reply_to(message, f'Твой ID: {message.from_user.id}')
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"""Команды:
    /serverstart - Запускает сервер
    /serverstop - Выключает сервер
    /serveronl - Игроки онлайн на сервере
    """)
@bot.message_handler(commands=['serverstart'])
def serverstart(message):
    serv.fetch()
    if serv.status != 'offline':
        bot.send_message(message.chat.id, '⛔️Ес чо сервер уже запущен⛔️')
    else:
        serv.fetch()
        startedd = False
        messagetoedit = bot.send_message(message.chat.id, 'Сервер запускается...🕐')
        serv.start()
        while startedd == False:
            serv.fetch()
            time.sleep(1)
            if serv.status == 'online':
                bot.edit_message_text(chat_id=message.chat.id, message_id=messagetoedit.message_id, text=f"Сервер запустился! ✅✅✅")
                startedd = True
            time.sleep(2)
@bot.message_handler(commands=['serverstop'])
def serverstop(message):
    adminscount = len(Admins)
    countt = 0
    while True:
        if str(Admins[countt][1]) == str(message.from_user.id):
            serv.fetch()
            if serv.status != 'online':
                bot.send_message(message.chat.id, '✅Админ-права найдены // ⛔Сервер уже остановлен!⛔')
            else:
                bot.send_message(message.chat.id, '✅Админ-права найдены // ✅Останавливаю сервер...✅')
                serv.stop()
            break
        elif countt == adminscount-1:
            bot.send_message(message.chat.id, f'⛔Недостаточно прав! (Феменистка)⛔️')
            break
        else:
            countt = countt + 1
            continue
@bot.message_handler(commands=['serveronl'])
def serveronl(message):
    serv.fetch()
    if serv.status == 'offline':
        bot.send_message(message.chat.id, f'⛔Сервер выключен!⛔')
    else:
        plistt = str(serv.players_list).replace('[', '').replace(']', '').replace("""'""", '').replace(',', '\n')
        bot.send_message(message.chat.id, f'✅ На сервере: {serv.players_count} из {serv.slots} игроков!✅\nИгроки:\n {plistt}')
@bot.message_handler(commands=['delmenu'])
def delmenu(message):
    bot.send_message(message.chat.id, "Удалил ебанную панельку", reply_markup=types.ReplyKeyboardRemove(), parse_mode='Markdown')







bot.polling(none_stop=True)

#@bot.message_handler(func=lambda m: True)

