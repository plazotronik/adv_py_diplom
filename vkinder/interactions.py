#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from vkinder.init_app import init_variable


# ФУНКЦИЯ ПРИВЕТСТВИЯ - НАЧАЛЬНОЕ ПРИВЕТСТВИЕ, УПРАВЛЕНИЕ ПРОГРАММОЙ


def hello():
    while True:
        print('Hello. you have find cool friend?')
        # bla-bla-bla
        # init_variable()
        # bla-bla-bla
        break



# def hello():
#     '''
#     1. Вывод сообществ пользователя vk.com, где нет ни одного его друга.
#     2. Вывод сообществ пользователя vk.com, где есть его друзья не более, чем заданное число.
#     9. Вывод этой справки.
#     0. Выйти из программы.
#     '''
#     good_bye = ('\n\n   Надеемся Вам очень понравилась наша программа!'
#                 '\n   Вопросы и предложения присылайте по адресу: info@it-vi.ru',
#                 '\n   Досвидания!'.upper())
#     print('\n\nДобро пожаловать в "bla-bla-bla"'.upper())
#     print('\n\nВам необходимо ввести цифру ниже, чтобы программа выполнила действие: '
#           '\n   9. Вывод справки.')
#     try:
#         while True:
#             prog = str(input(f'\n{"=" * 80}'
#                              '\n\n  номер действия: '.upper()))
#             if prog == '1':
#                 pass
#             elif prog == '2':
#                 try:
#                     pass
#                 except ValueError:
#                     print('\nВведено некорректное количество друзей. Это должно быть целое число. '
#                           'Попробуйте еще раз.')
#             elif prog == '9':
#                 hello().__help__()
#             elif prog == '0':
#                 print(good_bye)
#                 break
#             else:
#                 print('\nТакой функционал программы пока не подвезли)))'
#                       '\nЕсть предложения? Пишите по адресу: info@it-vi.ru')
#     except KeyboardInterrupt:
#         print(good_bye)