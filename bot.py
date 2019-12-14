token = '940800774:AAFUvP_oxMPx-qwBauD4b--Ypupc9_E1YBk'
import telebot
from telebot import types
import time

Stat_list = ['HI^2', 'Fisher','Likely_hood','Norm distribution']
MOU_list = ['Pontryagin','Princip_max','Diff']
Quant_list = ['Shred','Heizenberg','Wave function']
ML_list = ['Regression','CNN_definition','CNN_archirecture']

Stat_text = ['hi square','Fisher','Likely_hood','Norm distribution']
MOU_text = ['Pontryagin', 'Princip_max','Diff']
Quant_text = ['Shred','Heizenberg','Wave function']
ML_text = ['Regression','CNN_definition','CNN_archirecture']

Stat_path_list = ['mat_stat/hi2.jpg',
                    'mat_stat/Fisher.jpg',
                    'mat_stat/Likely_hood.jpg',
                    'mat_stat/Norm.jpg']

MOU_path_list = ['MOU/Pontyagin.jpg',
                 'MOU/Princip_max.jpg',
                 'MOU/Diff.jpg']

Quant_path_list = ['Quant/Shred.jpg',
                   'Quant/Heizenberg.jpg',
                   'Quant/Wave_function.jpg']

ML_path_list = ['ML/Regression.jpg',
                'ML/CNN_definition.jpg',
                'ML/CNN_archirecture.jpg']

id_list = [160765441,65039442]

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    # if id in id_list:
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def send_anytext(message):
    chat_id = message.chat.id
    client_id = message.from_user.id
    # print(client_id)
    if client_id in id_list:
        if message.text == 'Stati':
            bot.send_message(client_id, 'Stati', reply_markup=keyboard1())
        elif message.text == 'HI^2':
            bot.send_message(client_id,'lol',reply_markup=keyboard())
        # for i in range(len(Stat_list)):
            text = Stat_text[0]
            bot.send_message(client_id, text,reply_markup=keyboard())
            bot.send_photo(client_id, open(Stat_path_list[0], 'rb'))
        elif message.text == 'Fisher':
        # for i in range(len(Stat_list)):
            text = Stat_text[1]
            bot.send_message(client_id, text,reply_markup=keyboard())
            bot.send_photo(client_id, open(Stat_path_list[1], 'rb'))
        elif message.text == 'Likely_hood':
        # for i in range(len(Stat_list)):
            text = Stat_text[2]
            bot.send_message(client_id, text,reply_markup=keyboard())
            bot.send_photo(client_id, open(Stat_path_list[2], 'rb'))
        elif message.text == 'Norm':
        # for i in range(len(Stat_list)):
            text = Stat_text[3]
            bot.send_message(client_id, text,reply_markup=keyboard())
            bot.send_photo(client_id, open(Stat_path_list[3], 'rb'))


        elif message.text == 'MOU':
        # text = ''
            for i in range(len(MOU_list)):
                text = MOU_text[i]
                bot.send_message(client_id, text)
                bot.send_photo(client_id, open(MOU_path_list[i], 'rb'))


        elif message.text == 'Quant':
        # text = ''
            for i in range(len(Quant_text)):
                text = Quant_text[i]
                bot.send_message(client_id, text)
                bot.send_photo(client_id, open(Quant_path_list[i], 'rb'))


        elif message.text == 'ML':
        # text = ''
            for i in range(len(ML_list)):
                text = ML_text[i]
                bot.send_message(client_id, text)
                bot.send_photo(client_id, open(ML_path_list[i], 'rb'))
    else:
        bot.send_message(client_id, 'Sry bro you are not my friend!!!')


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Stati')
    btn2 = types.KeyboardButton('Quant')
    btn3 = types.KeyboardButton('MOU')
    btn4 = types.KeyboardButton('ML')
    markup.add(btn1,btn2)
    markup.add(btn3,btn4)
    return markup

def keyboard1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('HI^2')
    btn2 = types.KeyboardButton('Fisher')
    btn3 = types.KeyboardButton('Likely_hood')
    btn4 = types.KeyboardButton('Norm')
    markup.add(btn1,btn2)
    markup.add(btn3,btn4)
    return markup
bot.polling()
