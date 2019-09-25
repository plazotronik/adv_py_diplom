#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from vkinder.common_functions import translate_auto

# def delete_double_dict(list_dicts):
#     # удаление всех возможных дублей
#     for dict in list_dicts:
#         count = list_dicts.count(dict)
#         if count > 1:
#             for _ in range(count - 1):
#                 list_dicts.remove(dict)
#     return list_dicts


# удаление найденных ранее
# def delete_exist_id2(list_dicts, list_id):
#     # data = list_dicts
#     data = [dict(t) for t in {tuple(d.items()) for d in list_dicts}]
#     for dict_ in data:
#         if dict_['id'] in list_id:
#             print(data.count(dict_))
#             data.remove(dict_)
#     return data

def delete_exist_id(list_dicts, list_id):
    data = []
    for dict_ in list_dicts:
        if dict_['id'] not in list_id:
            data.append(dict_)
    return data

# удаление лишних слов. список еще будет корректироваться
def delete_stop(list_):
    list_result = []
    stop_list = ['него', 'а', 'ж', 'нее', 'со', 'без', 'же', 'ней', 'так', 'за', 'такой', 'будет',  'ни', 'там',
                 'будто', 'здесь', 'нибудь', 'бы', 'и', 'тем', 'из', 'ним', 'из-за', 'них', 'то', 'были',
                 'или', 'ничего', 'тогда', 'им', 'но', 'но', 'того', 'ну', 'тоже', 'в', 'их', 'о', 'вам', 'к', 'об',
                 'вас', 'тот', 'он', 'три', 'ведь', 'какая', 'тут', 'во', 'какой', 'вот', 'у', 'впрочем',
                 'от', 'уж', 'которого', 'перед', 'уже', 'которые', 'по', 'кто', 'под', 'хоть', 'куда', 'после',
                 'чего', 'всю', 'ли', 'потому', 'чем', 'г', 'между', 'почти', 'через', 'где', 'при', 'что', 'мне',
                 'про', 'чтоб', 'да', 'чтобы', 'даже', 'чуть', 'два', 'можно', 'с', 'для', 'мой', 'до', 'другой',
                 'этом', 'его', 'на', 'этот', 'ее', 'над', 'эту', 'ей', 'надо', 'ему', 'если', 'том', 'не']
    for word in list_:
       if word.lower() not in stop_list:
           list_result.append(word)
    return list_result

# удаление пустых значений
def delete_space(list_set):
    list_result = []
    for i in list_set:
        if (len(i) > 0) & (i not in ['-', '—', '!', '"', "'", '`']):
            list_result.append(i)
    return list_result


def delete_end_of_word(list_):
    list_result = []
    for word in list_:
        if len(word) in [4, 5,]:
            list_result.append(word[:-1])
        elif len(word) >= 6:
            list_result.append(word[:-2])
    return list_result

# превращение строки в список
def str_to_list(string):
    if string:
        # print(string)
        pattern_cirill = r'[а-я]{4,}'
        if re.findall(pattern_cirill, string, re.I):
            str_ = string
        else:
            str_ = translate_auto(string)
        # str_ = string
        pattern = r'\s|[^\w^-]|_'
        list_ = re.split(pattern, str_.lower())
        list_ = delete_end_of_word(list_)
        set_ = set(list_)
        list_ = delete_space(set_)
        list_ = delete_stop(list_)
        # print(list_)
        return list_
    else:
        # print(string)
        return []


def tmp_save(dict_):
    pass

if __name__ == '__main__':
    print(str_to_list("""Успешный человек меняет себя,остальных меняет жизнь!\nЖить сложнее, когда воспринимаешь всё 
    близко к сердцу...\n\nСамое офигенное — это самостоятельно зарабатывать деньги. Не страдать фигней,
     не пить фигню, не есть фигню, не спать с фигней. А работать и жить достойно, при этом осознавая, что 
    всего этого ты добился сам!\n\nВ воле человека есть сила стремления, которая превращает туман внутри нас в
     солнце (Джебран Халиль Джебран)\n\nЧеловек ценен, когда его слова совпадают с его действиями (Фридрих Ницше).
     \n\nНе беспокойся о том, что люди тебя не знают, но беспокойся о том, что ты не знаешь людей (Конфуций)"""))
    print(str_to_list("""'Семья. Психология, \xa0мотивационные тренинги, личностный рост, '
              'самопознание, бизнес, \xa0цель, \xa0успех, упорство, \xa0'
              'уверенность, \xa0силы, \xa0понимание, \xa0семинары, \xa0'
              'рост, \xa0тренинги, \xa0коуч, инициатива, \xa0инновации, \xa0'
              'мотивация.\xa0Инфобизнес, \xa0Реклама проектов, \xa0развитие '
              'бизнеса, \xa0Анализ рынка. Саморазвитие, \xa0личностный '
              'рост, \xa0техники работы с подсознанием и сознанием, \xa0'
              'йога.Раскрутка и продвижение проектов, \xa0развитие бизнеса. '
              'Коммуникативные стратегии Вегетарианство',"""))
