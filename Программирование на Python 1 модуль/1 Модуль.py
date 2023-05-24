     # 1 УРОК

# name = input("Введите ваше имя: ")
# # print(name + ", " + name)
# import random
import random

import requests
# num_1 = int(input("Первое число: "))
# num_2 = int(input("Второе число: "))
#
# mult = num_1 * num_2
# div = num_1 / num_2
#
# print("Сумма:" + str(mult))
# print("Разность:" + str(div))

# obj = input("Кто?: ")
# action = input("Что делал?: ")
# place = input("Где произошло?: ")
#
# print(obj, action, place)

# client = "Петя"
#
# pet = "Кот"
#
# print(client)
#
# print("и")
#
# print(pet)

# Создайте две переменные с именами «Первое животное» и «Второе животное» на английском языке.
# Запишите в первую переменную слово «Заяц», а во вторую — «Черепаха».
# Используя эти переменные, выведите на экран текст «Заяц спит, Черепаха идёт» в одну строку.

# pet1 = input("Первое животное: ")
# pet2 = input("Второе животное: ")
#
# print(pet1, "спит,", pet2, "идёт")

# print(pet1 + str("спит,"), pet2 + str("идёт"))

# num_1 = int(input("Первое число: "))
# num_2 = int(input("Второе число: "))
#
# mult = num_1 * num_2
# div = num_1 / num_2
#
# print("Умножение:" + str(mult))
# print("Деление:" + str(div))

# number = int(input('Введите число: '))
# summa = 0
#
# while number != 0:
#     summa += number
#     number = int(input('Введите следующее число: '))
#
# print(summa)

# password = int(input('Введите пароль: '))
#
# while password != 235:
#     print('Пароль не верный! ')
#     password = int(input('Повторите попытку: '))
#
# print('Добро пожаловать!')


        # 2 УРОК

# ВАЖНО ЗНАТЬ

# СОЗДАНИЕ
# Индексы   0         1        2       3.....
# films = ['film1', 'film2', 'film3', 'film4']

# # ДОБАВЛЕНИЕ
# films.append('film1')
# film = 'film1'
# films.append(film)

# # ИЗМЕНИЕНИЕ
# films[0] = 'Начало'
# print(films[0])

# # УДАЛЕНИЕ
# del films[1]
# films.remove('film5')

# # ДЛИНА
# print(len(films))



# films = ['film1', 'film2', 'film3']

# score_list = [5, 5, 4, 3]

# cords = [[5, 4], [3, 2], [4, 6]]

# films = []

# film_1 = input('Введите 1 фильм: ') # film1
# film_2 = input('Введите 2 фильм: ') # film2
# film_3 = input('Введите 3 фильм: ') # film3

# films.append('film1') # ['film1']
# films.append('film2') # ['film1', 'film2']
# films.append('film3') # ['film1', 'film2', 'film3']

#           0         1        2
# films = ['film1', 'film2', 'film3', 'film4']

# films[0] = 'Начало'
# print(films[0])

# print(films[-1])

# film_4 = films[3]

# print(films)
# film_2 = films.pop(1) # film_4 = films[3]
# print(film_2)
# print(films)

# del films[1]
# films.remove('film5')

# print(films)

# print(len(films))




# facts = ['Хамелеоны могут двигать глазами в разных направлениях одновременно.',
#     'Змеи видят через веки.',
#     'У коал отпечатки пальцев похожи на человеческие.',
#     'Белые медведи-левши.']

# fact_number = int(input('Введите число от 1 до 4: '))
# print(facts[fact_number - 1])


# nums = [4, 5, 8, 0, -5, -2]

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(nums)
# nums.sort(reverse=True)
# print(nums)

# index = nums.index(8)
# print(index)

# nums_2 = nums.copy()
# print(nums)
# print(nums_2)

# nums.clear()
# print(nums)

# listt = list('Hello')
# print(listt)

# score = [5, 4, 5, 4, 3, 3, 4, 5]
# avg = sum(score) / len(score)
# maxx = max(score)
# minn = min(score)
# count_5 = score.count(5)

# print(f'Средняя оценка - {avg}')
# print(f'Наивысшая оценка - {maxx}')
# print(f'Наихудшая оценка - {minn}')
# print(f'Количество пятерок - {count_5}')


        # 3 УРОК

# import random
# import emoji # pip install emoji
#
# facts = ['Хамелеоны могут двигать глазами в разных направлениях одновременно.',
#     'Змеи видят через веки.',
#     'У коал отпечатки пальцев похожи на человеческие.',
#     'Белые медведи-левши.']

# print(random.choice(facts))
# print(random.randint(-10, 10))

# print(facts)

# print(emoji.emojize(':smirk: is :green_heart:', language='alias'))

# for fact in facts:
#     print(fact)
#     print('В цикле')

# print('Вне цикла')


# films = []

# #         0 1 2
# for i in range(3):
#     film = input(f'Введите {i + 1} фильм: ')
#     films.append(film)

# print(films)

#            [0, 999]
# for i in range(1000):
#     print(i + 1)


# for i in range(5, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)


# accums = []

# for i in range(6):
#     income = int(input(f'Доход за {i + 1} месяц: '))
#     accums.append(income * 0.3)

# print(f'Ваши накопления составят {sum(accums)} рублей.')


        # 4 УРОК

# week_tamps = []

# for i in range(7):
#     week_tamps.append(int(input(f'Введите температуру за {i + 1} день: ')))

# avg_temp = sum(week_tamps) / len(week_tamps)
# print(f'Средняя температура за {len(week_tamps)} дней: {avg_temp:.2} градусов')

# favorite_actor = 'райн'
# actor = input('Кто играет главную роль в фильме: ').lower()
# rating = int(input('Введите рейтинг фильма: '))

# #  райн  ==     райн    ->    True
# #  Лео   ==     Райн    ->    False
# #  райн  ==     Райн    ->    False
# if actor == favorite_actor or rating > 7:
#     print('Этот фильм стоит посмотреть')
# # elif rating >= 8:
# #     print('Можно посмотреть')
# else:
#     print('Не смотри')

# # if     1
# # elif   0...n
# # else   0...1

# import random
#
# computer_num = random.randint(1, 10)
# print(computer_num)
#
# for i in range(3):
#     user_num = int(input('Угадай число от 1 до 10: '))
#     diff = user_num - computer_num
#
#     if user_num == computer_num:
#         print('Угадал')
#         break
#     elif diff == 1 or diff == -1:
#         print('Почти угадал')
#     else:
#         print('Не угадал')


        # 5 УРОК

# english_dict = {
#     'яблоко':'apple',
#     'молоко':'milk',
#     'кот':'cat'
# }

# print(english_dict["собака"])
# print(english_dict.get("собака"))

# word = input('Введите слово на русском: ').lower()

# if word in english_dict:
#     print(f'{word} - {english_dict.get(word)}')
# else:
#     print('Такого слова нет в нашем словаре')

# english_dict['кот'] = 'dog'
# print(f'{"кот"} - {english_dict.get("кот")}')


# films_dict = {
#     'начало': 'Леонардо Ди Каприо',
#     'пираты карибского моря': 'Джонни Депп',
#     'миссия невыполнима': 'Том Круз'
# }

# favorite_actor = 'Леонардо Ди Каприо'

# film = input('Какой фильм будем смотреть: ').lower()

# if film in films_dict:
#     actor = films_dict.get(film)
#     if actor == favorite_actor:
#         print('Этот фильм точно стоит посмотреть!')
#     else:
#         print('Я бы не стал тратить время!')
# else:
#     print('Такого фильма нет в нашей базе')

# questions = [
#     {
#         'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#         'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#         'right_answer': 4
#     },
#
#     {
#         'question': 'Как звучит полное имя младшего брата Тора?',
#         'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#         'right_answer': 3
#     },
#
#     {
#         'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
#         'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#         'right_answer': 1
#     }
# ]
#
# for question in questions:
#     # Вывод вопрса
#     print(question.get('question'))
#
#     # Вывод вариантов ответа
#     answer_number = 1
#     for answer in question.get('answers'):
#         print(f'{answer_number} - {answer}')
#         answer_number += 1  # answer_number = answer_number + 1
#
#     # Ввод ответа пользователя
#     user_answer = int(input('Ваш ответ: '))
#
#     # Проверка правильно ли ответил пользователь
#     if user_answer == question.get('right_answer'):
#         print('Верно')
#     else:
#         print(f'Не верно, правильный ответ: {question.get("right_answer")} ')
#
#     # Печатаем линию
#     print("-" * 40)


        # 6 УРОК

# Начнем с открытия, файл открыть можно в нескольких режимах:
# r - (read) чтение
# w - (write) запись
# a - (append) добавление
# r+ - чтение и запись

# file = open('название файла или путь до этого файла', 'режим')

# file = open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'a')
# file.write('Очень важная информация!!!')
# file.close()

# with open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'a') as file:
#     file.write('Очень важная информация!!!')

# with open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'r') as file:
#     text = file.read()
#     print(text)

# questions = [
#     {'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#      'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#      'right_answer': 4},
# {'question': 'Как звучит полное имя младшего брата Тора?',
#      'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#      'right_answer': 3},
# {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов
# для армии США?',
#      'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#      'right_answer': 1}
# ]
#
# name = input('Как вас зовут: ')
# count_points = 0
#
# for question in questions:
#     print(question.get('question'))
#     answer_number = 1
#     for answer in question.get('answers'):
#         print(answer_number, ' - ', answer)
#         answer_number += 1
#
#     user_answer = int(input('Ваш ответ: '))
#
#     if user_answer == question.get('right_answer'):
#         count_points += 1
#         print('Верно')
#     else:
#         print('Не верно')
#
#     print('-'*40)

    # print(f'Игрок {name} набрал очков: {count_points}')

# with open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'a') as file:
#     file.write(f'Игрок {name} набрал очков: {count_points}\n')
#     file.write('-' *40 + '\n')

# with open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'r') as file:
#     text = file.read()
#     print(text)

# with open('C:\\Users\\андрей\\PycharmProjects\\pythonProject\\result.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# def add(x, y):
#     print(x + y)
#     return x + y

# summ = add(7, 7)
# print(summ)
# print(add(5,7))


# def add(x, y):
#     z = 5
#     return x * y * z
#
# summ = add(7, 7)
# print(summ)

# Калькулятор
# def calculate(num1, num2, symbol):
#     if symbol == '+':
#         return num1 + num2
#     elif symbol == '-':
#         return  num1 - num2
#     else:
#         print('Такой символ не поддерживается')
#
# num = calculate(5, 7, '+')
# print(num)

# def summa_n(n):
#     summa_n = 0
#     for num in range(n):
#         summa += num + 1


        # 7 УРОК

# from tkinter import *

# window = Tk()
# window.geometry('700x500')
# window.title('Самый сложный тест')

# labal_title = Label(text='Тестирование по вселенной Marvel!!!', font=('Arial', 24), fg='red', bg='black')
# labal_title.place(x=0, y=0, width=700, height=50)

# facts = [
# {'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
# {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
# {'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
# {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
# ]
# cur_f = 0
# points = 0

# fact = Message(text=facts[cur_f]['text'], font=('Arial', 14), width=680)
# fact.configure(justify=CENTER)
# fact.place(x=10, y=70)

# var = IntVar()

# true = Radiobutton(text='Правда', variable=var, value=1)
# true.place(x=10, y=120)

# false = Radiobutton(text='Ложь', variable=var, value=0)
# false.place(x=10, y=170)

# def check():
#     global cur_f, points
#     answer = var.get()
#     if answer == facts[cur_f]['right']:
#         points += 1

#     if cur_f < len(facts) - 1:
#         cur_f += 1
#         fact['text'] = facts[cur_f]['text']
#     else:
#         points_label = Label(text=f'Вы набрали такое количество очков: {points}', font=('Arial', 24), fg='red', bg='white')
#         points_label.place(x=0, y=0, width=700, height=250)

# b = Button(text='Ответь', font=('Arial', 24), fg='black', command=check)
# b.place(x=200, y=130)


# window.mainloop()


# Программа Кликер

# from tkinter import *
# import random
# import time
#
# window = Tk()
# window.geometry('700x500')
# window.title('Кликер')
#
# points = 0
#
# def check():
#     global points
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     points +=1
#     points_label['text'] = points
#     time.sleep(2)
#
#
# b = Button(text='Нажми меня', font=('Arial', 20), fg='black', command=check)
# b.place(x=200,y=130)
#
# point_label = Label(text = points, font=('Arial',15), fg='black')
# point_label.place(x=10,y=10)

# window.mainloop()
#
# from tkinter import *
# import tkinter # window = tkinter.Tk()
#
# window = Tk()
#
# label = Label
#
# from random import *
#
# num = randint(1, 10)


        # 8 УРОК

# from tkinter import *
#
# window = Tk()
# window.geometry('900x300')
# window.title('WARNING')
#
# window.config(bg='red')
# window.resizable(width=False, height=False) # либо можно 0 поставить
#
# text = Label(text='Ваш компьютер заражён!!!', fg='red', bg='black', font=('Courier New', 34))
# text.place(x=100, y=100, width=700, height=100)
#
# count_text = Label(text='6', fg='red', bg='black', font=('Courier New', 38))
#
# def on_close():
#     if int(count_text['text']) > 0:
#         count_text['text'] = int(count_text['text']) - 1
#         count_text.place(x=250, y=25, width=400, height=100)
#         window.after(1000, on_close)
#     else:
#         screen_width = window.winfo_screenwidth()
#         screen_height = window.winfo_screenheight()
#         window.geometry(str(screen_width) + 'x' + str(screen_height))
#
#         photo = PhotoImage(file='C:\\Users\\андрей\\Desktop\\jeff.png')
#         photo_lable = Label(image=photo, bg='red')
#         photo_lable.image = photo
#         photo_lable.place(width=screen_width, height=screen_height, x=0, y=0)
#
# window.protocol('WM_DELETE_WINDOW', on_close)
#
# window.mainloop()


        # 9 УРОК

# import requests # pip install requests
# from bs4 import BeautifulSoup # pip install bs4    # pip install BeautifulSoup
# import random
#
#
# def get_fact():
#     response = requests.get('https://i-fakt.ru/')  		    # получаем доступ к сайту
#     site_content = response.content				            # берём с сайта весь HTML код
#     html_code = BeautifulSoup(site_content, 'html.parser')	# превращаем HTML код в BeautifulSoup (в то что мы теперь можем распарсить)
#     fact = random.choice(html_code.find_all(class_='p-2 clearfix')) # находим все теги с классом (p-2 clearfix) и выбираем случайный из них
#     print(fact.text)            # печатаем весь текст из тега
#     print(fact.a.attrs['href']) # печатаем ссылку (a - тег ссылки, attrs['href'] - параметр тега а, где хранится текст ссылки)
#
#
# def get_event():
#     response = requests.get('https://kudago.com/msk/festival/')
#     site_content = response.content
#     html_code = BeautifulSoup(site_content, 'html.parser')
#     event = random.choice(html_code.find_all(class_='post-title post-title-free'))
#     print(event.text)
#     print(event.a.attrs['href'])
#
# def get_concert():
#     response = requests.get('https://kudago.com/msk/concerts/')
#     site_content = response.content
#     html_code = BeautifulSoup(site_content, 'html.parser')
#     concert = random.choice(html_code.find_all(class_='post-title'))
#     print(concert.text)
#     print(concert.a.attrs['href'])
#
#
#
# get_concert()


        # 10 УРОК

# работа с циклом while (цикл с условием)

# выводим на экран все натуральные числа, которые меньше или равны num, в порядке возрастания
# num = int(input('Введите чиссло: '))
#
# while num > 0:
#     print(num)
#     num -= 1 # Тоже самое, что и num = num - 1

# num = int(input('Введите число: '))
# cur_num = 1 # хранит в себе текущее число
# while cur_num <= num:
#     print(cur_num)
#     cur_num += 1 # Тоже самое, что и num = num - 1

# import random
#
# films = ['Форсаж', 'Терминатор', 'Аватар', 'Оно 2', 'Властелин колец',
#          'Железный человек', 'Джон Уик', 'Невидимая сторона', 'Мстители',
#          'Мандалорец', 'Конан-варвар', 'Интерстеллар', 'Человек-Паук', 'Матрица',
#          'Законопослушный гражданин', 'Очень странные дела']
#
# print('Привет! Сейчас я буду показывать тебе случайный фильм. Тебе понравится =)')
# print(random.choice(films))
# answer = input('Нужно еще? Y/N: ')
# while answer == 'Y'.lower():
#     print(random.choice(films))
#     answer = input('Нужно еще? Y/N: ')
#
# print('Приятного просмотра!')

# import random
#
# films = ['Форсаж', 'Терминатор', 'Аватар', 'Оно 2', 'Властелин колец',
#          'Железный человек', 'Джон Уик', 'Невидимая сторона', 'Мстители',
#          'Мандалорец', 'Конан-варвар', 'Интерстеллар', 'Человек-Паук', 'Матрица',
#          'Законопослушный гражданин', 'Очень странные дела']
#
# print('Привет! Сейчас я буду показывать тебе случайный фильм. Тебе понравится =)')
# # создаем бесконечный цикл
# while True:
#     print(random.choice(films))
#     answer = input('Нужно еще? Y/N: ')
#     while answer != 'Y'.lower() and answer != 'N'.lower():
#         answer = input('Пожалуйста, введите ответ в формате Y/N: ')
#
#     # точка выхода из цикла
#     if answer == 'N'.lower():
#         # оператор досрочного выхода из цикла
#         break
#
# print('Приятного просмотра!')


# n = int(input())
# s = 0
# for i in range(n):
#     x = int(input())
#     s = s + x
# print(s)
# ---------------------------------------------------------------------------------------------------------
# Генерация PDF-файлов

# Подключаем из библиотеки объект, отвечающий за ссоздание PDF-файла

# from fpdf import FPDF
#
# создаем объект PDF-файла
# pdf_file = FPDF('P', 'cm', (10, 15))
#
# добавляем страницу с заданными параметрами в наш файл
# pdf_file.add_page()

# задаем шрифт текста внутри файла (с маленькой буквы)
# pdf_file.set_font('arial', size=16)

# задаем цвет текста (RGB - red, green, blue) (0 - 255)
# pdf_file.set_text_color(120, 35, 90)

# задаем цвет заливки (заднего фона)
# pdf_file.set_fill_color(0, 0, 120)

# задаем цвет рисования
# pdf_file.set_draw_color(0, 255, 0)

# создаем ячейку с текстом
# pdf_file.cell(8, 5, txt='Welcome!', align='C', border=5, fill=True)

# добавляем картинку
# pdf_file.image('pic.jpg', h=0, w=10, x=0, y=5)


# создаем заданный PDF-файл в текущей папки
# эта строчка должа быть в самом конце кода
# pdf_file.output('my_pdf.pdf')

# --------------------------------------------------------------------------------------------------------
# i = 1
# while i <= 10:
#     print(i**2)
#     i += 1
# else:
#     print(f'Цикл окончен i = {i}')

# n = int(input())
# length = 0

# while n > 0:
#     n //= 10  #    n = n // 10         57 // 10 = 5  ->  5 // 10 = 0
#               #                        578 // 10 = 57 ->  57 // 10 = 5 -> 5 // 10 = 0
#     length += 1

# print(length)


# summ = int(input('Какую сумму копим: '))
# accum = int(input('Сколько откладываем в месяц: '))
# m = 0

# while summ > 0:
#     summ -= accum
#     m += 1
# else:
#     print(m)

# import random
# from bs4 import BeautifulSoup
# import requests
#
# def get_interesting_fact():
#     response = requests.get('https://i-fakt.ru/')
#     response = response.content
#     html = BeautifulSoup(response, 'lxml')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     print(fact.text)
#     print(fact.a.attrs['href'])
#
# def get_event():
#     response = requests.get('https://kudago.com/msk/festival/')
#     response = response.content
#     html = BeautifulSoup(response, 'lxml')
#     fest = random.choice(html.find_all(class_='post-title'))
#     print(fest.text)
#     print(fest.a.attrs['href'])
#
# def get_concert():
#     response = requests.get('https://kudago.com/msk/concerts/')
#     response = response.content
#     html = BeautifulSoup(response, 'lxml')
#     concert = random.choice(html.find_all(class_='post-title'))
#     print(concert.text)
#     print(concert.a.attrs['href'])
#
# user_wish = ''
#
# while user_wish != 'хватит':
#     user_wish = input('Чем бы вы хотели заняться: ').lower()
#     if 'факт' in user_wish:
#         get_interesting_fact()
#     elif 'концерт' in user_wish:
#         get_concert()
#     elif 'фестиваль' in user_wish:
#         get_event()
#     else:
#         print('Хмм.. Может лучше посидеть дома...')


        # 11 УРОК

# from fpdf import FPDF
# from datetime import datetime
#
# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
# pdf.image('bg-BG.jpg', h=297, w=210, x=0, y=0)
#
# pdf.add_font('comic', '', 'C:\Windows\Fonts\comic.ttf', uni=True)
# pdf.set_font('comic', size=37)
# pdf.set_text_color(0, 0, 0)
#
# friend_name = input('Кому отправим: ')
#
# pdf.cell(0, 95, ln=1)
# pdf.cell(0, 20, txt=f'Дорогой {friend_name}!', align='C', ln=1)
#
# pdf.set_font('comic', size=18)
# pdf.set_text_color(255, 215, 0)
#
# message = input('Введите текст поздравления: ')
#
# pdf.set_left_margin(50)
# pdf.set_right_margin(50)
# pdf.multi_cell(0, 20, txt=message, align='C')
#
# pdf.set_font('comic', size=15)
# pdf.set_text_color(124, 89, 147)
#
# author_name = input('Введите своё имя: ')
# today_date = datetime.today().strftime('%d.%m.%y')
#
# pdf.cell(0, 10, txt=today_date, align='R', ln=1)
# pdf.cell(0, 10, txt=author_name, align='R', ln=1)
#
#
# pdf.output('card.pdf')








# from fpdf import FPDF
# # добавляем библиотеку для получения текущей даты
# from datetime import datetime
#
# pdf = FPDF('P', 'mm', 'A4')
# pdf.add_page()
#
# # добавляем задний фон для поздравительной открытки
# pdf.image('bg.jpg', h=297, w=210, x=0, y=0)
#
# # добавляем крассивый шрифт из операционной системы
# pdf.add_font('comic', '', 'C:\\Windows\\Fonts\\comic.ttf', uni=True)
# pdf.set_font('comic', size=37)
# pdf.set_text_color(0, 0, 0)
#
# name = input('Кому предназначается открытка? ')
#
# # добавляем линию сверху
# pdf.cell(0, 95, ln=1)
# pdf.cell(0, 20, txt='Дорогая ' + name + '!', align='C', ln=1)
#
# # добавляем текст поздравления
# pdf.set_font('comic', size=18)
# text = input('Введите текст поздравления: ')
# pdf.set_right_margin(50)
# pdf.set_left_margin(50)
# pdf.multi_cell(0, 20, txt=text, align='C')
#
# # добавляем дату поздравления
# today = datetime.today().strftime('%d.%m.%y')
# pdf.set_text_color(124, 89, 147)
# pdf.cell(0, 10, txt=today, align='R', ln=1)
#
# # добавляем имя автора открытки
# author_name = input('Введите свое имя: ')
# pdf.cell(0, 10, txt=author_name, align='R', ln=1)
#
# # последняя строчка в создании pdf-файла
# pdf.output('holiday.pdf')
# -------------------------------------------------------------------------------------------------------------

# заготовка для проекта
#
# from tkinter import *
#
# def find_fact():
#     clear()
#     draw_home_button()
#
# def show_cat():
#     clear()
#     draw_home_button()
#
# window = Tk()
# window.geometry('700x600')
#
# def draw_menu():
#     clear()
#     label_title = Label(text='Что бы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
#     label_title.place(width=700, height=50, x=0, y=0)
#
#     b_1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=find_fact)
#     b_1.place(x=25, y=75, width=300)
#
#     b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=show_cat)
#     b_2.place(x=375, y=75, width=300)
#
# def clear():
#     all_widjets = window.place_slaves()
#     for wid in all_widjets:
#         wid.destroy()
#
# def draw_home_button():
#     b_home = Button(text='Домой', font=('Arial', 18), fg='black', command=draw_menu)
#     b_home.place(x=25, y=500, width=150)
#
# draw_menu()
#
# window.mainloop()


# from tkinter import *
#
# # создаем 3 функции - для отображения меню, для очистки окна, для отображения кнопки
# def draw_menu():
#     clear()
#     menu_title = Label(text='Что бы вы хотели сделать?', font=('Arial', 24), fg='white', bg='orange')
#     menu_title.place(width=700, height=50, x=0, y=0)
#     b_1 = Button(text='Узнать что-то новое', font=('Arial', 18), fg='black', command=clear)
#     b_1.place(x=25, y=75, width=300)
#
#     b_2 = Button(text='Посмотреть на котиков', font=('Arial', 18), fg='black', command=clear)
#     b_2.place(x=375, y=75, width=300)
#
# def clear():
#     # получаем расположение всех объектов на виджете
#     all_widgets = window.place_slaves()
#     for wid in all_widgets:
#         wid.destroy()
#     draw_home_button()
#
# def draw_home_button():
#      b_home = Button(text='Домой', font=('Arial', 24), fg='black', command=draw_menu)
#      b_home.place(x=25, y=500, width=150)
#
# window = Tk()
# window.geometry('700x600')
#
# draw_menu()
#
# # последняя строчка в коде
# window.mainloop()


        # 12 УРОК

# import telebot # pip install pyTelegramBotAPI
# import requests
# import random
# from bs4 import BeautifulSoup
#
# # ВСТАВИТЬ ТОКЕН СВОЕГО БОТА
# token = '5916478728:AAHpbfVt10qCF0sJHSNennp6_aCEP92PRiI'
#
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_message(message):
#     print(message.from_user)
#     welcome_text = 'Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показывать милых котиков!'
#     bot.send_message(message.chat.id, welcome_text)
#
# @bot.message_handler(commands=['poem'])
# def send_poem(message):
#     poem_text = 'Муха села на варенье, вот и все стихотворенье...'
#     bot.send_message(message.chat.id, poem_text)
#
# @bot.message_handler(commands=['fact'])
# def send_fact(message):
#     response = requests.get('https://i-fakt.ru/').content
#     html = BeautifulSoup(response, 'html.parser')
#     fact = random.choice(html.find_all(class_='p-2 clearfix'))
#     bot.send_message(message.chat.id, fact.text)
#     link_fact = fact.a.attrs['href']
#     bot.send_message(message.chat.id, link_fact)
#
# @bot.message_handler(commands=['cat'])
# def send_cat(message):
#     cat_number = str(random.randint(1, 10))
#     cat_img = open('img/'+ cat_number + '.jpg', 'rb')
#     bot.send_photo(message.chat.id, cat_img)
#
# @bot.message_handler(commands=['music'])
# def send_music(message):
#     song = open('happy.mp3', 'rb')
#     bot.send_photo(message.chat.id, song)
#
#
# bot.polling()



# def my_decorator(func_to_decorate):     # функция - обертка
#     def decorated_func():               #
#         print(('Я начинаю работать.'))  # код, который выполнится перед началом работы функции
#         func_to_decorate()              # функция, которой требуется обертка
#         print('Я закончил работать.')   # который выполнится после завершения работы функции
#     return decorated_func               # вернем функцию - обертку код,
#
# @my_decorator
# def my_func():
#     print('Я работаю')
#
# @my_decorator
# def func2():
#     print('Hello')
# my_func()
# func2()