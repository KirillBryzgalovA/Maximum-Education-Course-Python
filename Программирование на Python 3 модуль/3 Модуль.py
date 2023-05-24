import math  # 1 УРОК

# Простая реализация работника

# name = input('Введите имя сотрудника: ')
# salary = int(input('Введите зарплату сотрудника: '))
# print(f'У {name}а зарплата в год состовляет {salary * 12} руб.')

# Реализация в виде словаря, 1 сотрудник.

# employee = {
#     'name':'Данил',
#     'salary':200
# }
#
# print(f'У {employee["name"]}а зарплата в год состовляет {employee["salary"] * 12} руб.')
#
# print(f'У {employee.get("name")}а зарплата в год состовляет {employee.get("salary") * 12} руб.')
#
# employee['age'] = 20
#
# print(f'У {employee.get("name")}а зарплата в год состовляет {employee.get("salary") * 12} руб.' +
#       f'Ему {employee.get("age")} лет')

# Реализация в виде списка если сотрудников много

# employees_list = [
#     {
#         'name': 'Данил',
#         'salary': 200,
#         'on_vacation': 'False'
#     },
#     {
#         'name': 'Антон',
#         'salary': 150,
#         'on_vacation': 'False'
#     },
#     {
#         'name': 'Иван',
#         'salary': 180,
#         'on_vacation': 'False'
#     }
# ]
#
# # print(employees_list[0])
# # print(employees_list[-1])
#
# # i = 0
# # for employee in employees_list:
# #     i += 1
# #     print(f"Итерация - {i}")
# #     print(f'У {employee.get("name")}а зарплата в год составляет {employee.get("salary") * 12} руб.')
# #     print()
# #
# # # Увольняем Ивана (метод remove)
# # for employee in employees_list:
# #     if employee.get('name') == 'Иван':
# #         employees_list.remove(employee)
# #         break
# # print(employees_list)
# #
# # # Нанимаем Кирилла (метод append)
# # new_employee = {
# #     'name': 'Кирилл',
# #     'salary': 120
# # }
#
# employees_list.append(new_employee)
# print(employees_list)

# Как узнать сколько сотрудников? (Длина списка)
# print(len(employees_list))
#
# for i in range(5):  # 0 1 2 3 4
#     print(f"Итерация - {i + 1}")
#
# print()
#
# for i in range(5, 10):  # 5 6 7 8 9
#     print(f"Итерация - {i}")

# class Employee:
#     def __init__(self, name, salary, on_vacation):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#
#     def get_info(self):
#         # return f'У {self.name}а зарплата в год составляет {employee.salary * 12} руб. Отпуск {self.on_vacation}'
#         print(f'У {self.name}а зарплата в год составляет {employee.salary * 12} руб. Отпуск {self.on_vacation}')
#
# employees_list = [
#     Employee('Данил', 200, False),
#     Employee('Иван', 180, False),
#     Employee('Кирилл', 120, False)
# ]
#
# for employee in employees_list:
#     # print(f'У {employee.name}а зарплата в год составляет {employee.salary * 12} руб. Отпуск {employee.on_vacation}')
#     employee.get_info()


        # 2 УРОК

# import vk_api           # pip install vk_api (Выбор версии интерпретатора Python: ctr + shift + p -> Python: Select Interpreter)
# # from course import *    # нужно чтобы файл course.py находился в той же папке что и этот код
# import requests # pip install requests
# from bs4 import BeautifulSoup # pip install bs4
# from datetime import datetime
#
# url = "http://www.cbr.ru/scripts/XML_daily.asp?"
#
# today = datetime.today()
# today = today.strftime("%d/%m/%Y")
#
# payload = {"date_req": today}
#
# response = requests.get(url, params=payload)
#
# xml = BeautifulSoup(response.content, 'html.parser')
#
#
# def get_course(currency):
#     return str(xml.find("valute", {'id': currency}).value.text)
#
#
# if __name__ == '__main__':
#     print(get_course("R01235"), "рублей за 1 доллар")
#     print(get_course("R01239"), "рублей за 1 евро")
#     print(get_course("R01375"), "рублей за 10 юаней")
#
# my_token = 'vk1.a.zx9qvSsJXa10pcWXEAgnf_joYO6noueBNEwRKy2iSwlLgg6DrjlunfMp3Z2a_UYVSdUWAbAODdWu3daZKoet8UoS-Q9KwJ40na5UxvyTOpP26d3ZJTGJac-XcKUM-7Zg2syQxThIluYWNEBX23LOjatyQbD_ybsEysNj91RcimTbjWxVz0a9roZMJU9pzFteIc36K0ZkfJwE7JBJ8wxzvA' # не забудьте вставить токен!!!
#
#
# vk = vk_api.VkApi(token=my_token)
# vk._auth_token()
#
# # print(messages)
# # print(messages['items'][0])
#
# # Если возникает ошибка: vk_api.exceptions.ApiError: [901] Can't send messages for users without permission
# # тогда нужно что-то написать именно в чат сообщества
# while True:
#
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:
#
#         user_id = messages['items'][0]['last_message']['from_id']   # id пользователя который пишет
#         message_id = messages['items'][0]['last_message']['id']     # id сообщения
#         message_text = messages['items'][0]['last_message']['text'] # текст сообщения
#
#         print(user_id, message_id, message_text)
#
#         # Курс доллара
#         if message_text.lower() == 'рублей за 1 доллар':
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01235")} руб.'})
#         # Курс доллара
#         elif message_text.lower() == 'рублей за 1 евро':
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01239")} руб.'})
#         # Курс доллара
#         elif message_text.lower() == 'рублей за 10 юаней':
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': f'{get_course("R01375")} руб.'})
#         # Фото котика
#         elif message_text.lower() == 'котик фото':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'attachment': 'photo642790826_457239624'})
#         # Котик видео
#         elif message_text.lower() == 'котик видео':
#             vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'attachment': 'video-173126618_456243948'})
#         # Неизвестная команда
#         else:
#             vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': 'Неизвестная команда :()'})


        # 3 УРОК

# import vk_api        # pip install vk_api (Выбор версии интерпретатора Python: ctr + shift + p -> Python: Select Interpreter)
# from course import *    # нужно чтобы файл course.py находился в той же папке что и этот код
# from vk_api.longpoll import VkLongPoll, VkEventType
# from wiki import get_wiki_article
#
# my_token = 'vk1.a.zx9qvSsJXa10pcWXEAgnf_joYO6noueBNEwRKy2iSwlLgg6DrjlunfMp3Z2a_UYVSdUWAbAODdWu3daZKoet8UoS-Q9KwJ40na5UxvyTOpP26d3ZJTGJac-XcKUM-7Zg2syQxThIluYWNEBX23LOjatyQbD_ybsEysNj91RcimTbjWxVz0a9roZMJU9pzFteIc36K0ZkfJwE7JBJ8wxzvA'
# vk_session = vk_api.VkApi(token=my_token)
# longpoll = VkLongPoll(vk_session)
#
# vk = vk_session.get_api()
#
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         user_id = event.user_id     # id пользователя который пишет
#         message_id = event.message_id # id сообщения
#         message_text = event.text.lower() # текст сообщения
#
#         print(user_id, message_id, message_text)
#
#         if message_text == '-к':
#             response = f'{get_course("R01235")} рублей за 1 доллар\n{get_course("R01239")} рублей за 1 евро' \
#                 f'{get_course("R01375")} рублей за 10 юаней\n{get_course("R01035")} рублей за 1 фунт'
#         # elif message_text[0:2] == '-в':
#         elif message_text.startswith('-в'):
#             article = message_text[3:]
#             response = get_wiki_article(article)
#             if len(response) >= 4000:
#                 response = response[0:4000]
#         else:
#             response = 'Неизвестная команда'
#
#         vk.messages.send(user_id=user_id, random_id=message_id, message=response)


        # 4 УРОК

# # def func(*args, **kwargs):
# #     print(args)
# #     print(kwargs)
#
# # func(1, 2, 4, 4, 8, c = 5, d = 4)
#
# def func_with_unlimited_args_and_kwargs(*args, **kwargs):
#     print(f'Арги {args}\nКварги: {kwargs}')
#
#
# func_with_unlimited_args_and_kwargs(1, 2, b=3, c=4, d=5, f=6, g=7)
#
# # my_file = open("test.txt", "w")
# # my_file.write("Writing some info...")
# # my_file.close()
#
# # with open("test.txt", "w") as my_file:
# #     my_file.write('Writing into file with context manager...')
# #     print(my_file.closed)
#
# # print(my_file.closed)


# import contextlib
#
# # @contextlib.contextmanager
# # def str_reverse(my_str):  # Hell0 -> olleH
# #     print('Входим в контекстный менеджер:')
# #     yield my_str[::-1]
# #     print('Выходим из контекстного менеджера:')
#
# # with str_reverse('Hello, world!') as reversed_str:
# #     print(f'Выполняется код: {reversed_str}')
#
#
# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print('Произошло исключение')
#
# with exc_handler(IndexError):
#     my_list = [1, 2]
#     print(my_list[0])
#     print(my_list[5])


# try:
#   Код для курса....
#     currency_name = currency.Name.text
#     currency_value = currency.Value.text
#     currency_nominal = currency.Nominal.text
# except AttributeError:
#     currency_info = "Валюта не была найдена"


# import time
#
# my_list = [time.sleep(x**2) for x in range(1, 3)] # строгие
# my_list = (time.sleep(x) for x in range(1, 3))   # ленивые
#
# for elem in my_list:
#     print(elem)
#
# print(my_list)


# # my_range = range(1, 11)
# # print(my_range)
# # print(list(my_range))
#
# def my_lazy_func():
#     for i in range(1, 11):
#         print(f'До {i}')
#         yield i
#         print(f'После {i}')
#
# for i in my_lazy_func():
#     print(i)
#
# my_list = list(my_lazy_func())
# print(my_list)
#
# # print(my_lazy_func())


# def my_lazy_func(items):
#     yield from items

# items = ['Яблоко', 'Банан', 'Апельсин']

# for i in my_lazy_func(range(1, 11)):
#     print(i)


        # 5 УРОК

# with open('text.txt', 'w') as my_file:
#     my_file.write('Hello')

# import time
#
#
# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb)
#         t = time.time() - self.start
#         print(f'Время работы кода: {t}')
#
#         if exc_type is TypeError:
#             return True
#         # return True
#
#
# with RunningCodeJudge() as t1:
#     # __enter__()
#     my_list = [x for x in range(1, 10000000)]
#     my_list -= 's'

    # __exit__()

# with open('text.txt', 'w') as my_file:
#     my_file.write('Hello')

# import time
#
#
# class RunningCodeJudge:
#     def __init__(self):
#         self.start = None
#
#     def __enter__(self):
#         self.start = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # print(exc_type)
#         # print(exc_val)
#         # print(exc_tb)
#         t = time.time() - self.start
#         print(f'Время работы кода: {t}')
#
#         if exc_type is TypeError:
#             return True
#         # return True
#
#
# with RunningCodeJudge() as t1:
#     # __enter__()
#     my_list = [x for x in range(1, 10000000)]
#     my_list -= 's'

# __exit__()



    # my_list = [1, 2, 3, 4, 5]
    # list_iterator = iter(my_list)
    # print(next(list_iterator))
    # print(next(list_iterator))
    # print(next(list_iterator))
    # print(next(list_iterator))
    # print(next(list_iterator))
    #
    # print(next(list_iterator))
    # # for i in list_iterator:
    # #     print(i)

    # import random
    #
    #
    # class RandomIter:
    #     def __init__(self, limit):
    #         self.limit = limit
    #         self.__reload = limit
    #
    #     def __iter__(self):
    #         self.limit = self.__reload
    #         return self
    #
    #     def __next__(self):
    #         if self.limit == 0:
    #             raise StopIteration
    #         self.limit -= 1
    #         return random.randint(0, 100)
    #
    #
    # rand_iter = RandomIter(3)
    # # print(next(iter(rand_iter)))
    #
    # for rand_int in rand_iter:
    #     print(rand_int)
    #
    # print('-' * 20)
    #
    # for rand_int in rand_iter:
    #     print(rand_int)


        # 6 УРОК

# class Year:
#     def __init__(self, days, season):
#         self.__days = days
#         self.__season = season
#
#     def get_days(self):
#         return self.__days
#
#     def get_season(self):
#         return self.__season
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
#     def set_season(self, season):
#         if season == 'Лето' or season == 'Осень' or season == 'Зима' or season == 'Лето':
#             self.__season = season
#         else:
#             raise Exception('Некорректное значение')
#
# year = Year(365, 'Зима')
# print(year.get_days(), year.get_season())
# year.set_days(365)
# year.set_season('Осень')
# print(year.get_days(), year.get_season())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age <= 0:
#             raise ValueError('Вы ещё не родились')
#         elif age <= 101:
#             raise ValueError('Вы что долгожитель?')
#         self.__age = age
#
# person = Person('Иван', 40)
# print(person.name)
# print(person.age)
# person.name = 'Данил'
# person.age = 16
# print(person.name)
# print(person.age)


        # 7 УРОК

# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price + other
#
#     def __sub__(self, other):
#         if isinstance(other, Item):
#             return self.price - other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price - other
#
#     def __mul__(self, other):
#         if isinstance(other, Item):
#             return self.price * other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price * other
#
#     def __truediv__(self, other):
#         if isinstance(other, Item):
#             return self.price / other.price
#         elif isinstance(other, int) or isinstance(other, float):
#             return self.price / other
#
# # __sub__() - для операции вычитания;
# # __mul__() - для операции умножения;
# # __truediv__() - для операции деления.
#
# item_1 = Item('Видеокарта', 25_000, 0.8)
# item_2 = Item('Процессор', 15_000, 0.3)
#
# total_price_1 = item_1 + item_2   # total_price = item_1.price + item_2.price
# total_price_2 = item_1 + 1000
# total_price_3 = item_1 + 1000.99
# print(total_price_1, total_price_2, total_price_3, sep='\n')


# ИГРА АЛХИМИЯ

# from tkinter import *
# from random import randint
#
# # https://www.flaticon.com/search?word=soil - где искать картинки
#
# window = Tk()
# window.geometry('600x600')
#
# class Fire:
#     image = PhotoImage(file='elements/fire.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Clay
#
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Steam
#
# class Water:
#     image = PhotoImage(file='elements/water.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Steam
#
# class Air:
#     image = PhotoImage(file='elements/air.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Dust
#
# class Earth:
#     image = PhotoImage(file='elements/earth.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Dust
#
# class Steam:
#     image = PhotoImage(file='elements/steam.png').subsample(4, 4)
#
# class Dust:
#     image = PhotoImage(file='elements/dust.png').subsample(4, 4)
#
# class Clay:
#     image = PhotoImage(file='elements/clay.png').subsample(4, 4)
#
#
# canvas = Canvas(window, width=600, height=600)
# canvas.pack()
#
# elements = [Earth(), Fire(), Water(), Air()]
#
# for elem in elements:
#     canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)
#
# def move(event):
#     # print(event.x, event.y)
#     image_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
#     # print(image_id)
#
#     if len(image_id) == 2:
#         elem_id_1, elem_id_2 = image_id[0], image_id[1]
#         element_1 = elements[elem_id_1 - 1]
#         element_2 = elements[elem_id_2 - 1]
#
#         new_element = None
#         try:
#             new_element = element_1 + element_2
#         except TypeError:
#             print('Нет такого элемента')
#         if new_element:
#             if new_element not in elements:
#                 canvas.create_image(randint(50, 550), randint(50, 550), image=new_element.image)
#                 elements.append(new_element)
#
#     canvas.coords(image_id, event.x, event.y)
#
# window.bind('<B1-Motion>', move)
# window.mainloop()


        # 8 УРОК

# from pprint import pprint
# from typing import Iterator
#
# # игорь.capitalize() -> Игорь
#
# goods = [
#     {
#         'name': 'Iphone',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'REALME C25s',
#         'brand': 'REALME',
#         'price': 650
#     }
# ]
#
# print(__name__)
#
# if __name__ == "__main__":
#
#     # SORTED
#     def item_price(item):
#         return item['price']
#
#     # print(sorted(goods, key=item_price))
#     pprint(sorted(goods, key=lambda item: item['price'])) # lambda
#
#     # FILTER
#     apple_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
#     # pprint(isinstance(apple_list, Iterator))
#     pprint(apple_list)
#
#     # MAP
#     numbers_list = ['1', '2', '3', '4', '5']
#
#     numbers_list = list(map(int, numbers_list))
#     print(numbers_list)
#
#     names_list = ['Данил', 'Никита', 'Настя']
#     surnames_list = ['Петров', 'Иванов', 'Белкова']
#     full_names_list = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames_list))
#     print(full_names_list)
#
#     # ENUMERATE
#     indexed_goods = []
#                   # (index, item)
#     for i, item in enumerate(goods):
#         # indexed_goods.append({i: item})
#         print(i, item)
#     pprint(indexed_goods)
#
#     # ZIP
#     names_list = ['Данил', 'Никита', 'Настя']
#     surnames_list = ['Петров', 'Иванов', 'Белкова']
#     patronymic_list = ['Данилович', 'Никитич', 'Ивановна']
#                         #   (elem_list_1, elem_list_2)
#     for name, surname, patronymic in zip(names_list, surnames_list, patronymic_list):
#         print(name, surname, patronymic)
#
#     print(__name__)
#
# # import M3Les8
# #
# # print(M3Les8.goods)

# goods = [
#     {
#         'name': 'Iphone',
#         'brand': 'Apple',
#         'price': 1200
#     },
#     {
#         'name': 'Samsung Galaxy A',
#         'brand': 'Samsung',
#         'price': 500
#     },
#     {
#         'name': 'REALME C25s',
#         'brand': 'REALME',
#         'price': 650
#     }
# ]
#
# def item_price(item):
#     return item['price']
#
# print(sorted(goods, key=item_price))


        # 9 УРОК




        # 10 УРОК




        # 11 УРОК




        # 12 УРОК



