#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from pandas))) import bla-bla-bla ???
import json
from vkinder.data_operation.functions import delete_exist_id, str_to_list
from vkinder.vk.objects import UserSearcher


# временная замена выборки из БД id прошлых поисков
patch_list_userid_from_db = [555007153, 556357138, 558370929, 559721024, 525246846, 499544698, 494211559, 478940773]
userid_from_db = patch_list_userid_from_db


# временная замена результатов анализа для записи в БД
patch_result_analise = [
    {'user_id': 123, 'name': 'Bla Bla 123', 'page_url': 'https://vk.com/id123',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
    {'user_id': 456, 'name': 'Bla Bla 456', 'page_url': 'https://vk.com/id456',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
    {'user_id': 789, 'name': 'Bla Bla 789', 'page_url': 'https://vk.com/id789',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
    {'user_id': 321, 'name': 'Bla Bla 312', 'page_url': 'https://vk.com/id123',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
    {'user_id': 654, 'name': 'Bla Bla 654', 'page_url': 'https://vk.com/id456',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
    {'user_id': 987, 'name': 'Bla Bla 987', 'page_url': 'https://vk.com/id789',
     'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
]
result = patch_result_analise


# описание пользователя нашей программы с его интересами
reference = UserSearcher().__dict__()
print(reference)


# data_search - временная замена результату поиска API VK
# по сути датасет из 4800 уникальных найденных персон
# не прикрепляю файл, т.к. может содержать не публичные данные
data_search = []
def tmp_data():
    with open('data.json') as file:
        data_search.extend(json.load(file))
tmp_data()


# удаление тех кто уже был найден ранее
data_search = delete_exist_id(data_search, userid_from_db)


# варианты весов
weights1 = {
    'activities': 0.6,
    'about': 0.48,
    'interests': 0.68,
    'music': 0.54,
    'movies': 0.19,
    'tv': 0.05,
    'books': 0.5,
    'games': 0.16,
    'quotes': 0.23,
    'groups': 0.45,
    'common_count': 0.15,
}
weights = {
    'activities': 15,
    'about': 12,
    'interests': 17,
    'music': 13,
    'movies': 5,
    'tv': 1,
    'books': 12,
    'games': 4,
    'quotes': 6,
    'groups': 11,
    'common_count': 4,
}


# связка id и кол-ва голосов
vote = {}


# присвоение голосов
# (пока без групп и общих друзей - отдельные функции напишу)
def vote_put(list_dicts, reference, key, weight=0):
    for dict_ in list_dicts:
        try:
            list_searcher = reference[key]
            list_found = str_to_list(dict_[key])
        except Exception as err:
            continue
        else:
            for word in list_searcher:
                if word in list_found:
                    try:
                        tmp = vote[dict_['id']]
                    except Exception as err:
                        vote[dict_['id']] = weight
                    else:
                        vote[dict_['id']] += weight


if __name__ == '__main__':
    # подсчитываем голоса
    vote_put(data_search, reference, 'quotes', weights['quotes'])
    vote_put(data_search, reference, 'about', weights['about'])
    vote_put(data_search, reference, 'music', weights['music'])
    vote_put(data_search, reference, 'activities', weights['activities'])
    vote_put(data_search, reference, 'interests', weights['interests'])
    vote_put(data_search, reference, 'books', weights['books'])
    vote_put(data_search, reference, 'movies', weights['movies'])
    vote_put(data_search, reference, 'tv', weights['tv'])
    vote_put(data_search, reference, 'games', weights['games'])

    print(vote)
    print(len(vote))







