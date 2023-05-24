import random  # 1 УРОК

# first_var = 22 # тип данных int
# second_var = 3.5 # тип данных float
#
# print(first_var + second_var)
# print(first_var - second_var)
# print(first_var / second_var)
# print(first_var * second_var)
#
# print(type(first_var), type(second_var))
#
# res_var = first_var + second_var
#
# print(type(res_var))

# str_var = 'Привет, мир'
# print(str_var)
# sub_string_hello = str_var[:6]
# sub_string_world = str_var[8:]
# print(sub_string_hello)
# print(sub_string_world)


# IF ELISE ELSE (try, except)

# try:
#       # Код который мы хотим выполнить и который может вызвать ошибку
# except тип ошибки:
#       # Действия программы если ошибка возникла
# else:
#       # Действия программы если ошибки не возникло

# try:
#     input_num_1 = int(input('Введите первое число: '))
#     input_num_2 = int(input('Введите второе число: '))
# except ValueError:
#     print('Вы ввели неправильное значение!!!')
#
# else:
#     if input_num_1 > input_num_2:
#         print(f'{input_num_1} больше чем {input_num_2}.')
#         print(str(input_num_1) + ' больше чем ' + str(input_num_2))
#         print(input_num_1, 'больше чем', input_num_2)
#
#     elif input_num_1 < input_num_2:
#         print(f'{input_num_1} меньше чем {input_num_2}.')
#     else:
#         print(f'{input_num_1} равно {input_num_2}.')

# СПИСКИ

# home_list = ['кухня', 'комната', 'зал']
# home_list.append('спальная')
# print(home_list)
# home_list[1] = 'детская'
# print(home_list)
#
# print(len(home_list))
#
# for h in home_list:
#     print(h)

# ЦИКЛЫ

# for i in range(6):
#     print(i)

# for i in range(5, 11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# ФУНКЦИИ

# def add1(x, y):
#     return x + y
#
# def add2(x, y):
#     print(x + y)
#
# summ = add1(5, 5)
# print(summ)

# def hello():
#     name = input('Как тебя зовут: ')
#     print(f'Приятно познакомиться {name}')
#     hello()
#
# hello()

# def calculate():
#     try:
#         number_1 = int(input("Введите первое число: "))
#         number_2 = int(input("Введите второе число: "))
#     except ValueError:
#         print('Вы ввели неправильное значение')
#     else:
#         print('Укажите нужную вам операцию: ')
#         print('* - умножение')
#         print('/ - деление')
#         print('+ - сложение')
#         print('- - вычитание')
#
#         operation = input()
#
#         result = None
#         if operation == '*':
#             result = int(number_1) * int(number_2)
#         elif operation == '/':
#             result = int(number_1) / int(number_2)
#         elif operation == '+':
#             result = int(number_1) + int(number_2)
#         elif operation == '-':
#             result = int(number_1) - int(number_2)
#         else:
#             print('Операция неизвестна, повторите ввод')
#         print(result)
#
#
# calculate()

        # 2 УРОК

# import telebot # pip install pyTelegramBotAPI
# import requests
# import random
# from bs4 import BeautifulSoup
#
# # НЕ ЗАБУДЬТЕ ВСТАВИТЬ СВОЙ ТОКЕН!!!!
# token = '5916478728:AAHpbfVt10qCF0sJHSNennp6_aCEP92PRiI'
# bot = telebot.TeleBot(token)
#
# # /start  /help
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
#     button_poem = telebot.types.KeyboardButton('Стихотворение')
#     button_fact = telebot.types.KeyboardButton('Факт')
#     button_cat = telebot.types.KeyboardButton('Кот')
#     button_music = telebot.types.KeyboardButton('Песня')
#     keyboard.add(button_poem, button_fact, button_cat, button_music)
#     welcome_text = 'Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!'
#     bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)
#
#
# # /poem
# @bot.message_handler(commands=['poem'])
# def send_poem(message):
#     poem_text = "Муха села на варенье, вот и все стихотворенье..."
#     bot.send_message(message.chat.id, poem_text)
#     keyboard = telebot.types.InlineKeyboardMarkup(row_widt=1)
#     button_url = telebot.types.InlineKeyboardMarkup('Перейти', url='https://stihi.ru/')
#     keyboard.add(button_url)
#     bot.send_message(message.chat.id, 'Больше стихов по ссылке ниже', reply_markup=keyboard)
#
#
# # /fact
# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     content = requests.get('https://i-fakt.ru/').content
#     html = BeautifulSoup(content, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     bot.send_message(message.chat.id, fact.text)
#     fact_link = fact.a.attrs['href']
#     bot.send_message(message.chat.id, fact_link)
#
# # /cat
# @bot.message_handler(commands=['cat'])
# def send_cat(message):
#     cat_number = str(random.randint(1, 10))
#     cat_img = open('img/' + cat_number + '.jpg', 'rb')
#     bot.send_photo(message.chat.id, cat_img)
#
# # /music
# @bot.message_handler(commands=['music'])
# def send_music(message):
#     song = open('happy.mp3', 'rb')
#     bot.send_audio(message.chat.id, song)
#
# # /sticker
# @bot.message_handler(commands=['sticker'])
# def send_sticker(message):
#     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG485joIHoJNo-HhPDyqFr3MgsBhJJlQACJhsAAokPMUrtYe1UVcDAfiwE')
#
#
# @bot.message_handler(content_types=['text'])
# def answer(message):
#     if message.text.strip() == 'Стихотворение':
#         send_poem(message)
#     elif message.text.strip() == 'Факт':
#         send_fact(message)
#     elif message.text.strip() == 'Кот':
#         send_cat(message)
#     elif message.text.strip() == 'Песня':
#         send_music(message)
#     else:
#         bot.send_message(message.chat.id, 'Нет такой команды')
#
#
# bot.polling()


        # 3 УРОК

# from tkinter import *
#
# window = Tk()
#
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# # canvas.create_rectangle(120, 120, 140, 140, fill='red', outline='')
# # canvas.create_rectangle(150, 150, 190, 190, fill='blue', outline='')
# # canvas.create_rectangle(200, 200, 260, 260, fill='green', outline='')
#
# # canvas.create_polygon(10, 180, 60, 120, 110, fill='red', outline='')
#
#
# canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='')
# canvas.create_rectangle(20, 260, 100, 310, fill='green', outline='')
# canvas.create_rectangle(50, 280, 70, 290, fill='SkyBlue1', outline='black')
#
#
# window.mainloop()



# from tkinter import *
#
# window = Tk()
#
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# # canvas.create_rectangle(120, 120, 140, 140, fill='red', outline='')
# # canvas.create_rectangle(150, 150, 190, 190, fill='blue', outline='')
# # canvas.create_rectangle(200, 200, 260, 260, fill='green', outline='')
#
# # canvas.create_polygon(10, 180, 60, 120, 110, fill='red', outline='')
#
#
# # canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='')
# # canvas.create_rectangle(20, 260, 100, 310, fill='green', outline='')
# # canvas.create_rectangle(50, 280, 70, 290, fill='SkyBlue1', outline='black')
#
# class House:
#     def __init__(self, roof_color, wall_color):
#         self.roof_color = roof_color
#         self.wall_color = wall_color
#         self.width = 130
#         self.height = 100
#         self.roof = None
#         self.wall = None
#
#     def build_house(self, x, y):
#         h = self.height
#         w = self.width
#
#         self.roof = canvas.create_polygon(x, y, x + w, y, x + w/2, y - h/2, fill=self.roof_color)
#         self.wall = canvas.create_rectangle(x+20, y, x + w - 20, y + h, fill=self.wall_color)
#
#     def print_info(self):
#         print(f'Цвет дома {self.wall_color}')
#         print(f'Цвет крыши {self.roof_color}')
#         print(f'Ширина дома {self.width}')
#         print(f'Высота дома {self.height}')
#
#
# house_1 = House('red', 'green')
# house_2 = House('black', 'blue')
# house_3 = House('orange', 'purple')
#
# house_1.build_house(40, 100)
# house_2.build_house(250, 250)
# house_3.build_house(450, 450)
#
# window.mainloop()


        # 4 УРОК

# from tkinter import *
# import random
#
# window = Tk()
# window.title('Игра Дракон')
#
#
# w = 600
# h = 600
#
# window.geometry(str(w) + 'x' + str(h))
# window.resizable(width=False, height=False)
#
# canvas = Canvas(window, width=w, height=h)
# canvas.pack()
#
# bg_photo = PhotoImage(file='bg_2.png')
#
#
# # Класс рыцарь
# class Knight:
#     def __init__(self):
#         # Координаты центра рыцаря
#         self.x = 70
#         self.y = h / 2
#         # Скорость рыцаря (в начале игры он стоит)
#         self.v = 0
#         # Скорость рыцаря по Оси Х (в начале игры он стоит)
#         self.v_x = 0
#         # Изображение рыцаря
#         self.photo = PhotoImage(file='knight.png')
#
#     # Движение вверх
#     def up(self, event):
#         self.v = -6
#
#     # Движение вниз
#     def down(self, event):
#         self.v = 6
#
#     # Движение вправо
#     def right(self, event):
#         self.v_x = 6
#
#     # Движение влево
#     def left(self, event):
#         self.v_x = -6
#
#     # Остановка
#     def stop(self, event):
#         self.v = 0
#         self.v_x = 0
#
#
# knight_obj = Knight()
#
#
# # Класс для создания дракона
# class Dragon:
#     def __init__(self):
#         self.x = w + 150
#         self.y = random.randint(100, h - 100)
#         self.v = random.randint(1, 3)
#         self.photo = PhotoImage(file='dragon.png')
#
#
# # Создаём список драконов
# dragons_list = []
# for i in range(3):
#     dragons_list.append(Dragon())
#
#
# def game():
#     canvas.delete('all')
#     canvas.create_image(w // 2, h // 2, image=bg_photo)
#     canvas.create_image(knight_obj.x, knight_obj.y, image=knight_obj.photo)
#     knight_obj.y += knight_obj.v
#     knight_obj.x += knight_obj.v_x
#
#     current_dragon = 0
#     dragon_to_kill = -1
#
#     for dragon in dragons_list:
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
#         if ((dragon.x - knight_obj.x) ** 2) + ((dragon.y - knight_obj.y) ** 2) <= (96) ** 2:
#             dragon_to_kill = current_dragon
#
#         current_dragon += 1
#
#         # Поражение
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w // 2, h // 2, text="Ты проиграл!", font="TimesNewRoman 40", fill='green')
#             break
#
#     if dragon_to_kill >= 0:
#         del dragons_list[dragon_to_kill]
#
#     # Победа
#     if len(dragons_list) == 0:
#         canvas.delete('all')
#         canvas.create_text(w // 2, h // 2, text="Ты победил!", font="TimesNewRoman 40", fill='red')
#
#     # Расставление границ для передвижения рыцаря
#     if knight_obj.y <= 52:
#         knight_obj.y = 53
#     if knight_obj.y >= 544:
#         knight_obj.y = 543
#     if knight_obj.x <= 50:
#         knight_obj.x = 51
#     if knight_obj.x >= 550:
#         knight_obj.x = 551
#     else:
#         window.after(20, game)
#
#
# game()
#
# window.bind('<Key-Up>', knight_obj.up)
# window.bind('<Key-Down>', knight_obj.down)
# window.bind('<Key-Right>', knight_obj.right)
# window.bind('<Key-Left>', knight_obj.left)
# window.bind('<KeyRelease>', knight_obj.stop)
#
# window.mainloop()


        # 5 УРОК

# import requests  # pip install requests
#
# url = 'https://swapi.dev/api/'  # Сайт со звёздными войнами, здесь информация о всей вселенной
#
# response = requests.get(url).json()
#
# people_api = response.get('people')  # Если хотите работать с персонажами из вселенной
#
#
# def check_people(url):
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()  # https://swapi.dev/api/people + / + i(1 - 5)
#         print(response['name'] + '-' + response['height'])
#
#
# planets_api = response.get('planets')  # Если хотите работать с планетами
#
#
# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()  # https://swapi.dev/api/people + / + i(1 - 5)
#         print(response.get('name'))
#
#
# def check_planets_diameter(url):
#     diameters_list = []
#     for i in range(1, 6):
#         response = requests.get(f'{url}/{i}').json()  # https://swapi.dev/api/people + / + i(1 - 5)
#         diameters_list.append({response.get('name'): response.get('diameter')})
#
#     print(diameters_list)
#
#
# # listt = [2, 5, 11]
#
# # for i in listt:
#
#
# check_people(people_api)
# check_planets_diameter(planets_api)
#
# # var_1 = True
# # var_2 = False
#
# # var_3 = 6 > 5
# # # print(var_3)
#
# # hour = 2
#
# # # hour = 18  True(1)  *   False(0)
# # if hour > 12 and hour <= 16:
# #     print('день')
# # elif hour > 16 and hour <= 23:
# #     print('вечер')
#
# # # hour = 2  False(0)  +   True(1)
# # elif hour > 23 or hour <= 3:
# #     print('ночь')
# # elif hour > 3 and hour <= 12:
# # 	print("Утро")
#
#
# # var = not(5 > 10)
#
# # print(var)


        # 6 УРОК

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
#
#
# today = datetime.today()            # сегодняшняя дата
# # print(today)
# today = today.strftime('%d/%m/%Y')  # сегодняшняя дата в формате день/месяц/год
# # print(today)
# payload = {'date_req':today}
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
#
# # date = 'date_req=20/01/2023'
#
# responce = requests.get(url, params=payload)
#
# # responce = requests.get(url + date)
#
#
#
# xml = BeautifulSoup(responce.content, 'html.parser')
#
# def getCourse(id):
#     return xml.find('valute', {'id':id}).value.text
#
# print(f'{getCourse("R01235")} рублей за 1 доллар')
# print(f'{getCourse("R01239")} рублей за 1 евро')
# print(f'{getCourse("R01375")} рублей за 1 юань')
#
# with open('file.txt', 'a') as my_file:
#     my_file.write(f'Курс за {today}:\n')
#     my_file.write(f'{getCourse("R01235")} рублей за 1 доллар\n')
#     my_file.write(f'{getCourse("R01239")} рублей за 1 евро\n')
#     my_file.write(f'{getCourse("R01375")} рублей за 1 юань\n\n')
#
#
#
#
# print(responce.url)


# СЛОВАРИ
# eng_dict = {
#     'Apple':'яблоко',
#     'Cat':'Кот',
#     'Dog':'Собака'
# }

# print(eng_dict.get('Milk'))

# eng_dict['Milk'] = 'Молоко'

# print(eng_dict.get('Milk'))



# ФАЙЛЫ

# my_file = open('file.txt', 'w')
# my_file.write('Hello')
# my_file.close()


# with open('file.txt', 'a') as my_file:
#     my_file.write('Hello')

# with open('file.txt', 'r') as my_file:
#     text = my_file.read()
#     print(text)


# Начнем с открытия, файл открыть можно в нескольких режимах:
# r - (read) - чтение;
# w - (write) - запись;
# a - (append) - добавление;
# r+ - (read + write) - чтение и запись (r + w).


        # 7 УРОК

# import os
# from gtts import gTTS  # pip install gtts
# from playsound import playsound # pip install playsound==1.2.2
# # from pygame import mixer # pip install pygame
#
#
# # голосовое воспроизведение текста
# with open('some.txt', 'r', encoding='utf-8') as my_file:
#     my_string = my_file.read()
#
# # print(my_string)
# # mixer.init()
#
# mp3_name = 'ru.mp3'
# tts = gTTS(text=my_string, lang='ru')  # также можно tts = gTTS(text='text', lang='ru')
# tts.save(mp3_name)
# playsound(mp3_name)
# # mixer.music.load(mp3_name)
# # mixer.music.play()
#
#
# # голосовой помощник
# import pyaudio  # pip install pyaudio
# import speech_recognition as sr  # pip install SpeechRecognition
#
# a = 3
# while a != 0:
#     # Ну а в том случае, если у вас к компьютеру подключено сразу много разных микрофонов, то
#     # нужно посмотреть их список и выбрать подходящий индекс. Для этого вам понадобится
#     # выполнить эту команду: print(sr.Microphone.list_microphone_names())
#
#     recognizer = sr.Recognizer()  # распознаватель
#     # если не работает можно попробовать оставить пустые скобки в sr.Microphone() ниже
#     with sr.Microphone(device_index=1) as source:
#         # если не помогли пустые скобки то вызывайте строчку ниже
#         # recognizer.adjust_for_ambient_noise(source, duration=3)
#         print('Скажи что-нибудь')
#         audio = recognizer.listen(source)
#
#     speech = recognizer.recognize_google(audio, language='ru_RU').lower()
#     print(speech)
#
#     if 'привет' in speech:
#         print('Привет')
#     elif 'пока' in speech:
#         print('Пока')
#     else:
#         print('Я вас не понимаю')
#
#     a -= 1
#
#
#
# from datetime import datetime
#
# today = datetime.today().strftime('%d.%m.%Y')
#
# print(today)


        # 8 УРОК

# # ОБЫЧНОЕ ОКНО
# from tkinter import *

# count = 0
# def change_label():
#     global count
#     count += 1
#     label_1['text'] = count

# window = Tk()
# window.title('Моё приложение')
# window.geometry('500x500+200+200')

# label_1 = Label(window, text='Текст', font='16', bg='#137836', fg='black')
# label_1.place(x=100, y=100)

# # label_1['text'] = 'Поменяли'
# # label_1['fg'] = '#ff0000'

# btn = Button(text='Кнопка', bg='#16c751', fg='black', font='16', command=change_label)
# btn.place(x=200, y=200)

# window.mainloop()


# ИНТЕРФЕЙС-ТАБЛО ДЛЯ КУРСА ВАЛЮТ
# from tkinter import *
# import requests                 # pip install requests
# from bs4 import BeautifulSoup   # pip install bs4
# from datetime import datetime
#
# window = Tk()
# window.geometry('400x350+300+300')
# window.title('Курс валют')
#
# img = PhotoImage(file='logo.png')
# logo = Label(window, image=img)
# logo.place(x=0, y=0)
#
# tablo = Label(window, text='Курс валют \n MAXIMUM банк', font=('Arial', 22))
# tablo.place(x=150, y=25)
#
# # Код с предыдущего урока
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
#
# payload = {"date_req" : today}
#
# responce = requests.get(url, params=payload)
#
# xml = BeautifulSoup(responce.content, "html.parser")
#
# def getCourse(id):
# 	return xml.find("valute",  {'id': id}).value.text
# #------------------------------
#
# course_date = Label(window, text=f'Курс валют на {today.replace("/", ".")}', font=('Arial', 18))
# course_date.place(y=150, x=90)
#
# usd_course = Label(window, text=f'$ {getCourse("R01235")} руб.', font=('Arial', 18))
# usd_course.place(y=190, x=100)
#
# eur_course = Label(window, text=f'€ {getCourse("R01239")} руб.', font=('Arial', 18))
# eur_course.place(y=230, x=100)
#
#
# window.mainloop()


        # 9 УРОК

# #  *args и **kwargs
# def func(a, b,*args, **kwargs):
#     c = kwargs.get('c')
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
# func(1, 2, 3, 4, 5, c = 3, one = 1, two = 2)

# # -----------------------------------------------

# # ТЕРНАРНЫЙ if

# age = 18
# # 2 вариант
# is_allow = True if age >= 18 else False
#
# print(is_allow)
#
# # 1 вариант
# if age >= 18:
#     is_allow = True
# else:
#     is_allow = False
#
# # 3 вариант
# is_allow = age >= 18
#
# num = 0 if age < 18 else age
# print(num)
#
# # # -----------------------------------------------
#
# val = None
# # # 1 вариант
# if val is None:
#     res = []
# else:
#     res = val
#
# # # 2 вариант
# res = [] if val is None else val
#
# # # 3 вариант
# res = val or []
#
# print(res)
#
# # # -----------------------------------------------
#
#
# # ГЕНЕРАЦИЯ СПИСКОВ И СЛОВАРЕЙ
#
# div_5_list = []
#
# # # 1 вариант
# for x in range(100):
#     if x % 5 == 0:     # 5 % 2 = 1     5 % 10 = 5    4 % 2 = 0
#         div_5_list.append(x)
#
# print(div_5_list)
#
# # # 2 вариант
# div_5_list = [x for x in range(100) if x % 5 == 0]
#
# #             |         3         | |       1         | |     2      |
# div_5_list = [x**3 if x > 50 else x for x in range(100) if x % 5 == 0]
#
# # for x in range(100):
# #     div_5_list.append(x)
#
# print(div_5_list)


# # -----------------------------------------------

# a = {x:len(x) for x in ["orange", "red", "blue", "green"]}
# print(a)


# Самостоятельное задание
# Попробуйте самостоятельно написать генератор списков,
# который генерирует список чисел кратных 30 или 31 в промежутке от 0 до 250.

# div_5_list = [x for x in range(250) if x % 30 == 0 or x % 31 == 0]
# print(div_5_list)

# # СПИСОК
# listt1 = []
# listt2 = list()

# # КОРТЕЖ
# tuple1 = ()
# tuple2 = tuple()

# some_dict = {
#     (1, 2, 3) : 'Hello'
# }
# a = some_dict.get((1, 2, 3))
# print(a)


# some_tuple = (1, 2, 3)
# print(some_tuple, type(some_tuple))
# some_list = list(some_tuple)
# print(some_list, type(some_list))
# some_tuple = tuple(some_list)
# print(some_tuple, type(some_tuple))


# some_tuple = ([1, 2, 3], "qwe")
# print(some_tuple)
# some_tuple[0].append(4)
# print(some_tuple)


        # 10 УРОК

# # процедура
# def f_1():
#     print(4)

# # функция
# def f_2():
#     return(4)

# f_1()
# print(f_2())



# class Human:
#     def __init__(self, name, color_hair, height, weight):
#         self.name = name
#         self.color_hair = color_hair
#         self.height = height
#         self.weight = weight
#
#     def breathe(self):
#         print(f'{self.name} дышит')
#
# human1 = Human('Антон', 'red', 190, 80)
# print(human1.name)
# human1.name = 'Иван'
# print(human1.name)
#
# # human2 = Human('Костя', 'red', 190, 80)
# # print(human2.name)
#
#
# import random
#
#
# class Tank:
#     """Template of tanks"""
#
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         self.model = model
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
#         self.health = health
#
#     def print_info(self):
#         print(f'{self.model} имеет лобовую броню {self.armor}мм. при {self.health} здоровье и урон {self.damage}')
#
#     def health_down(self, enemy_damage):
#         self.health -= enemy_damage - (self.armor / 10)
#         print(f"\n{self.model}:")
#         if self.health <= 0:
#             self.health = 0
#         print(f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")
#
#     def shot(self, enemy):
#         enemy.health_down(self.damage)
#         if enemy.health > 0:
#             print(f"\n{self.model}:")
#             print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
#         else:
#             print(f'Экипаж танка {enemy.model} уничтожен')
#
#
# class SuperTnk(Tank):
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         super().__init__(model, armor, min_damage, max_damage, health)
#         self.forceArmor = True
#
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage / 2)


# tank_1 = Tank('ИС-3', 90, 20, 30, 100)
# tank_2 = Tank('Tiger', 90, 10, 40, 100)

# tank_1.print_info()
# tank_2.print_info()

# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)
# tank_1.shot(tank_2)


# tank_1 = Tank('ИС-3', 90, 20, 30, 100)
# tank_super = SuperTnk('MAUS', 90, 10, 40, 100)
#
# tank_1.print_info()
# tank_super.print_info()
#
# tank_1.shot(tank_super)
# # tank_1.shot(tank_super)
# # tank_1.shot(tank_super)
# # tank_1.shot(tank_super)
#
#
# class A:
#     def one(self):
#         print(1)
#
#     def two(self):
#         print(2)
#
#
# class B(A):
#     def one(self):
#         print('one')
#
#     def three(self):
#         print(3)
#
#
# class C(A):
#     pass
#
#
# a = A()
# b = B()
#
# a.one()
# # a.two()
#
# b.one()
# b.two()

# b.three()


        # 11 УРОК

# # print(id(1), type(1))
# # print(id(id), type(id))
# # print(id(type), type(type))
#
#
# class A:
#     def public(self):
#         return 42
#
#     def _private(self):
#         return 'test'
#
#     def __protect(self):
#         return True
#
#     def wrapper_protect(self):
#         return self.__protect()
#
#
# a = A()
#
# print(a.public())
# print(a._private())
# print(a._A__protect())


# # ПАТТЕРН Singleton
# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

# s = Singleton()
# print(s, id(s))
# s1 = Singleton()
# print(s1, id(s1))


# ДЕКОРАТОРЫ

# def f():
#     return 2 + 2

# q = f

# print(q())

# def repair_deco(func): # тут постоянный аргумент это func
#     def wrapper(a, b): # тут аргументы которые получает функция
#         return func(a, b) - 1
#     return wrapper
#
# @repair_deco
# def wrong_func(a, b):
#     return a + b + 1
#
# print(f'2 + 2 = {wrong_func(2, 2)}')
# print(f'5 + 5 = {wrong_func(5, 5)}')


# from datetime import datetime
#
#
# def timeit(func):
#     def wrapper(val):
#         start = datetime.now()
#         res = func(val)
#         end = datetime.now()
#         print(f'time: {end - start}')
#         return res
#
#     return wrapper
#
#
# @timeit
# def get_list_1(val):
#     return [x for x in range(val) if x % 2]
#
#
# @timeit
# def get_list_2(val):
#     new_list = []
#     for x in range(val):
#         if x % 2:
#             new_list.append(x)
#     return new_list
#
#
# val = 100000000
#
# a = get_list_1(val)
# b = get_list_2(val)


        # 12 УРОК

# from tkinter import *
# import time
#
#
# class Ball():
#
#     def __init__(self, canvas, platform, color):
#         self.canvas = canvas
#         self.platform = platform
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
#         self.dir = [-3, -2, -1, 1, 2, 3]
#         self.x = random.choice(self.dir)
#         self.y = -1     # чтобы мяч двигался вверх
#         self.pos = self.canvas.coords(self.oval)
#         self.touch_bottom = False
#
#
#     def draw(self):
#         self.canvas.move(self.oval, self.x, self.y)
#         self.pos = self.canvas.coords(self.oval)
#         if self.pos[0] <= 0:
#             self.x = 1
#         if self.pos[1] <= 0:
#             self.y = 1
#         if self.pos[2] >= 500:
#             self.x = -1
#         if self.pos[3] >= 400:
#             self.touch_bottom = True
#         if self.touch_platform():
#             self.y = -1
#
#     def touch_platform(self):
#         platform_pos = self.canvas.coords(self.platform.rect)
#         if self.pos[2] >= platform_pos[0] and self.pos[0] <= platform_pos[2]:       # pos = [x1, y1, x2, y2]
#             if self.pos[3] >= platform_pos[1] and self.pos[3] <= platform_pos[3]:
#                 return True
#         return False
#
# class Platform():
#
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('a', self.left)
#         self.canvas.bind_all('d', self.right)
#         self.canvas.bind_all('<KeyRelease>', self.stop)
#         self.pos = self.canvas.coords(self.rect)
#
#     def left(self, event):
#         if self.pos[0] >= 0:
#             self.x = -2
#
#     def right(self, event):
#         if self.pos[2] <= 500:
#             self.x = 2
#
#     def stop(self, event):
#         self.x = 0
#
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#         self.pos = self.canvas.coords(self.rect)
#         if self.pos[0] <= 0:
#             self.x = 0
#
#         if self.pos[2] >= 500:
#             self.x = 0
#
#
# window = Tk()
# window.title("Аркада")
# window.resizable(0, 0)
# window.wm_attributes('-topmost', 1)
#
# canvas = Canvas(window, width=500, height=400)
# canvas.pack()
#
# platform = Platform(canvas, 'green')
# ball = Ball(canvas, platform, 'red')
#
# while True:
#     if ball.touch_bottom:
#         break
#     else:
#         platform.draw()
#         ball.draw()
#     window.update()
#     time.sleep(0.01)
#
# # window.mainloop() # Закомментировать это чтобы после проигрыша закрывалось окно.
