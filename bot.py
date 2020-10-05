#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from config import TOKEN
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup  # import buttons
import os
import json
import tg_analytic
#from telegram import ParseMode
#telebot.apihelper.proxy={'https':'socks5://Selroman358:L1e3OdN@185.230.88.187:45786'}

bot = telebot.TeleBot(TOKEN)
#os.chdir('nn_bot')

js = open("dict_final.json").read()
dict_recipes = json.loads(js)
reklama = 'Небольшой пример рекламы. Хочешь пиццу? Звони +3898989894894'


@bot.message_handler(commands=['start'])  # it is welcome part
def welcome(message):
    tg_analytic.statistics(message.chat.id, message.text)
    global ingredients_user
    ingredients_user = ''
    start_text = ('Привет, я бот по поиску рецептов. Я помогу тебе найти рецепты блюд, ' +
                  'которые ты сможешь приготовить прямо сейчас. Просто нажми кнопку /search ' +
                  'и выбери из списка продукты, лежащие у тебя в холодильнике🤗')
    bot.send_message(message.chat.id, start_text)
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Выбрать рецепт", callback_data='search')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Приятного аппетита! =)', reply_markup=markup)

# category of food
@bot.message_handler(commands=['search'])
def search(message):
    tg_analytic.statistics(message.chat.id, message.text)
    # bot.send_message(message.chat.id, 'help')
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton("Крупы", callback_data='cereals')
    item2 = types.InlineKeyboardButton("Овощи", callback_data='vegs')
    item20 = types.InlineKeyboardButton("Молочные продукты", callback_data='milks')
    item3 = types.InlineKeyboardButton("Фрукты", callback_data='fruits')
    item4 = types.InlineKeyboardButton("Рыба", callback_data='fish')
    item5 = types.InlineKeyboardButton("Мясо", callback_data='meat')
    item6 = types.InlineKeyboardButton("Специи", callback_data='spice')
    item61 = types.InlineKeyboardButton("Бакалея", callback_data='grocery')
    item62 = types.InlineKeyboardButton("Птица", callback_data='birds')
    item620 = types.InlineKeyboardButton("Сухофрукты", callback_data='dfruits')
    item63 = types.InlineKeyboardButton("Ягоды", callback_data='berry')
    item64 = types.InlineKeyboardButton("Сладости", callback_data='candy')
    item65 = types.InlineKeyboardButton("Зелень", callback_data='green')
    item66 = types.InlineKeyboardButton("Макаронные изделия", callback_data='pasta')
    item73 = types.InlineKeyboardButton("Орехи", callback_data='nuts')
    item74 = types.InlineKeyboardButton("Хлеб", callback_data='bread')
    item75 = types.InlineKeyboardButton("Яйца", callback_data='eggs')
    item76 = types.InlineKeyboardButton("Грибы", callback_data='lsd')
    item7 = types.InlineKeyboardButton("🤗 Подобрать рецепт 🤗", callback_data='give_recipes1')
    markup.add(item1, item2, item20, item3, item4, item5, item6, item61, item62, item620, item63, item64, item65, item66, item73, item74, item75, item76)
    markup.add(item7)
    bot.send_message(message.chat.id, 'Выберите категорию:', reply_markup=markup)

@bot.message_handler(commands=['give_recipes1'])
def give_recipes1(message):
    tg_analytic.statistics(message.chat.id, message.text)
    global ingredients_user
    dict_links = []
    for rec in dict_recipes:
        l_ing = dict_recipes[rec][1]
        count_ = 0
        for i in l_ing:
            if i not in ingredients_user:
                count_ += 1
        if count_ == 0:
            dict_links.append(rec)
    if len(dict_links) > 0:
        string_ = ''
        for j in dict_links:
            string_ += j
            string_ += '\n'
    else:
        string_ = 'Не найдено рецепта с такими ингредиентами =('
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("Новый поиск", callback_data='search'))
    bot.send_message(message.chat.id, string_ + '\n\n' + reklama, reply_markup=markup)
    ingredients_user = ''

@bot.message_handler(commands=['done_add'])
def done_add(message, text):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, text+ ' успешно добавлено.')

@bot.message_handler(commands=['cereals'])
def cereals(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['рис', 'перловка', 'овсяные хлопья', 'гречка', 'овсяные отруби', 'крупа кукурузная', 'крупа кукуруза', 'пшено', 'гречневая крупа', 'хлопья', 'киноа', 'булгур', 'крупа ячневая', 'крупа гречневая', 'каша', 'крупа', 'нут', 'крупа манка']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите крупы:', reply_markup=markup)

@bot.message_handler(commands=['milks'])
def milks(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['молоко', 'сыр', 'сметана', 'творог', 'майонез', 'йогурт', 'пармезан', 'сливки', 'масло', 'кефир', 'ряженка', 'моцарелла', 'масло сливочное']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите продукты:', reply_markup=markup)

@bot.message_handler(commands=['vegs'])
def vegs(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['кабачок', 'помидор', 'перец болгарский', 'чеснок', 'имбирь', 'горох', 'свекла', 'тыква', 'картошка', 'морковь', 'оливки', 'овощи', 'капуста', 'лук', 'сельдерей', 'брокколи', 'огурец', 'цуккини', 'нут', 'перец маринованный']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите овощи:', reply_markup=markup)

@bot.message_handler(commands=['fruits'])
def fruits(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['банан', 'киви', 'груши', 'апельсин', 'манго', 'лимон', 'яблоко', 'гранат', 'дыня']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите фрукты:', reply_markup=markup)

@bot.message_handler(commands=['fish'])
def fish(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['хек', 'тунец', 'треска', 'рыба окунь', 'филе рыбы', 'рыба лосось']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите рыбу:', reply_markup=markup)

@bot.message_handler(commands=['meat'])
def meat(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['фарш', 'печень', 'кролик', 'мясо кролика', 'филе кролика', 'мясо говядины', 'телятина', 'колбаса', 'мясо', 'ветчина', 'сосиски', 'мясо говядины', 'свинина', 'фрикадельки', 'ребра свиные']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите мясо:', reply_markup=markup)

@bot.message_handler(commands=['spice'])
def spice(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['ванилин', 'перец чёрный', 'лавровый лист', 'корица', 'имбирь', 'ваниль', 'стружка кокосовая', 'орех мускатный', 'тмин', 'базилик', 'паприка', 'специи', 'куркума', 'кориандр', 'кардамон', 'кумин', 'розмарин', 'пищевой краситель', 'агар-агар', 'гвоздика', 'хмели-сунели']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['grocery'])
def grocery(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['масло оливковое', 'мука', 'разрыхлитель', 'дрожжи', 'томатный соус', 'сахар', 'крахмал', 'соевый соус', 'масло кокосовое', 'масло растительное', 'масло кунжутное', 'масло подсолнечное', 'сода', 'соль', 'нут', 'уксус']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['birds'])
def birds(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['курица', 'мясо индейки', 'куриное филе', 'утка', 'филе индейки', 'куриные грудки']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['dfruits'])
def dfruits(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['изюм', 'курага', 'чернослив', 'сухофрукты']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['berry'])
def berry(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['клубника', 'малина', 'клюква', 'арбуз', 'смородина']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['candy'])
def candy(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['шоколад', 'мед', 'какао', 'конфеты']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['green'])
def green(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['укроп', 'петрушка', 'листья салатные', 'базилик', 'зелень', 'кинза']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['pasta'])
def pasta(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['макароны', 'вермишель', 'лапша', 'спагетти', 'канелонни']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['nuts'])
def nuts(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['орехи', 'миндаль', 'орех миндаль', 'орех мускатный', 'орех кедровый']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['bread'])
def bread(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['хлеб', 'лаваш', 'гренки', 'сухари']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['eggs'])
def eggs(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['яйцо', 'яичный белок', 'яичный желток']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(commands=['lsd'])
def lsd(message):
    tg_analytic.statistics(message.chat.id, message.text)
    list_of_vegs = ['грибы', 'грибы шампиньоны']
    button_list = []
    for each in list_of_vegs:
        button_list.append(types.InlineKeyboardButton(each, callback_data = each))
    markup = InlineKeyboardMarkup(row_width=3)
    for i in button_list:
        markup.add(i)
    markup.add(InlineKeyboardButton("назад", callback_data='search'))
    bot.send_message(message.chat.id, 'Выберите специи:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    tg_analytic.statistics(message.chat.id, message.text)
    if message.chat.type == 'private':
        user_text = message.text
        if user_text == 'А автор кто?':
            bot.send_message(message.chat.id, "Вовка Доронин https://github.com/DoroninDobro")
        elif message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
            st = message.text.split(' ')
            if 'txt' in st or 'тхт' in st:
                tg_analytic.analysis(st,message.chat.id)
                with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                    bot.send_document(message.chat.id,file)
                tg_analytic.remove(message.chat.id)
            else:
                messages = tg_analytic.analysis(st,message.chat.id)
                bot.send_message(message.chat.id, messages)
        else:
            welcome(message)

# function proccesing answer
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global ingredients_user
    if call.message:
        if call.data == 'search':
            search(call.message)
        elif call.data == 'cereals':
            cereals(call.message)
        elif call.data == 'vegs':
            vegs(call.message)
        elif call.data == 'fruits':
            fruits(call.message)
        elif call.data == 'fish':
            fish(call.message)
        elif call.data == 'meat':
            meat(call.message)
        elif call.data == 'milks':
            milks(call.message)
        elif call.data == 'spice':
            spice(call.message)
        elif call.data == 'grocery':
            grocery(call.message)
        elif call.data == 'birds':
            birds(call.message)
        elif call.data == 'dfruits':
            dfruits(call.message)
        elif call.data == 'berry':
            berry(call.message)
        elif call.data == 'candy':
            candy(call.message)
        elif call.data == 'green':
            green(call.message)
        elif call.data == 'pasta':
            pasta(call.message)
        elif call.data == 'nuts':
            nuts(call.message)
        elif call.data == 'bread':
            bread(call.message)
        elif call.data == 'eggs':
            eggs(call.message)
        elif call.data == 'lsd':
            lsd(call.message)
        elif call.data == 'give_recipes1':
            give_recipes1(call.message)
        else:
            ingredients_user += call.data
            ingredients_user += ' + '
            done_add(call.message, call.data)

#bot.polling()
bot.polling(none_stop=True) #, timeout = 120)  # bot work non-stop
