#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vkinder.vk.api_connect import vk_login
import getpass
import json

# БУДЕТ СОЗДАВАТЬ СОЕДИНЕНИЕ С VK.COM
# ВОЗМОЖНО ЕЩЕ ЧТО-ТО БУДЕТ ТУТ ЗАПУСКАТЬСЯ

# def init_variable():
#     global vk_cursor, searcher_id, vk_token
#     two_factor = input('Your account use two factor authorization? (y/n) - ')
#     login = str(input('Please, input your login (better phone number): '))
#     password = getpass.getpass('Input your password and press "Enter" (spy mode): ')
#     if two_factor in ['y', 'yes', 'н', 1, '1']:
#         vk_ = vk_login(login, password, True)
#     else:
#         vk_ = vk_login(login, password)
#     vk_token = vk_.token['access_token']
#     vk_cursor = vk_.get_api()
#     searcher_id = vk_cursor.users.get()[0]['id']
#     return vk_

# временно из файла берутся логин и пароль для подключения пользователя к VK
credentials_test = {}
with open('credentials_test.json') as file:
    credentials_test.update(json.load(file))

vk_ = vk_login(credentials_test['login'], credentials_test['password'])
vk_cursor = vk_.get_api()
searcher_id = vk_cursor.users.get()[0]['id']
# print(searcher_id)
vk_token = vk_.token['access_token']