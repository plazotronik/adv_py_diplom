#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
from pprint import pprint
from datetime import datetime
from vkinder.init_app import vk_cursor
from vkinder.data_operation.translate import translate

# превращаем дату рождения в возраст полных лет
def bdate_to_age(bdate):
    date_list = bdate.split('.')
    birth_date = datetime(year=int(date_list[2]), month=int(date_list[1]), day=int(date_list[0]))
    age = (datetime.now() - birth_date).days // 365
    return age

# ищем страну для определения города
def find_country():
    list_country = []
    with open('countries.json') as file:
        list_country.extend(json.load(file))
    your_country = input('Please, input country (in english): ').lower()
    for country in list_country:
        if your_country in country['Name'].lower():
            find_country_ = country['Code']
            return find_country_

# определяем город для поиска
def find_city():
    try:
        id_country = vk_cursor.database.getCountries(code=find_country())['items'][0]['id']
    except Exception as err:
        print('Error in input. Detailed: ', err, '\nSet to default city Moscow.')
        return 1
    else:
        your_city = input('Please, input city: ').lower()
        try:
            id_city = vk_cursor.database.getCities(country_id=id_country, q=your_city)['items'][0]
        except Exception as err:
            print('Error in input. Detailed: ', err, '\nSet to default city Moscow.')
            return 1
        else:
            city = translate(id_city["title"])
            answer = input(f'Your city {city}? (y/n) - ').lower()
            if answer in ['y', 'yes', 'н']:
                return id_city['id']
            else:
                print('Congratulation! Set to default city Moscow ))))')
                return 1

# определяем пол кого будем искать
def gender_determination(integer):
    list = [0, 'girls/woman', 'boys/man']
    sex_inverse = {1: 2, 2: 1}
    value = sex_inverse.pop(integer)
    answer = input(f'You search {list.pop(value)}? (y/n) - ').lower()
    if answer in ['y', 'yes', 'н']:
        print('Good choice')
        return value
    else:
        answer2 = input(f'You search {list.pop(1)}??.. (y/n) - ').lower()
        if answer2 in ['y', 'yes', 'н']:
            print('So... Welcome to tolerance.')
            return sex_inverse.values().__iter__().__next__()
        else:
            print('Oookay... We understand. Search all.')
            return list[0]


if __name__ == '__main__':
    print(bdate_to_age('1.1.1980'))
    # find_city()
    # print(gender_determination(1))

