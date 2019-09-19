#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
KEY_API = 'trnsl.1.1.20190704T182934Z.17f33d8db55385c6.e6d41260c9ccabfba9197455fd6d6679fec9bf38'

# в итоге поменяю диалоги программы с пользователем только на русский
# функция понадобится для перевода встроенных оповещений на русский
def translate(text, from_='ru', to='en'):
    '''
    translation input text

    :return:
    translated text
    '''
    params = {
        'key': KEY_API,
        'text': text,
        'lang': f'{from_}-{to}',
        'options': 1,
    }
    response = requests.get(URL, params=params)
    return ''.join(response.json()['text'])
