#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vkinder.init_app import searcher_id, vk_cursor # заменить
from vkinder.vk.functions import bdate_to_age

from pprint import pprint

fields_searcher = 'domain,sex,bdate,activities,interests,books,about,music,movies,quotes,city'
fields_found = 'domain,activities,interests,games,books,about,music,movies,tv,quotes,common_count'

# общий класс
class UserVK:
    def __init__(self, id_=searcher_id):
        self.resp = vk_cursor.users.get(user_ids=id_, fields=fields_searcher)[0]
        # pprint(self.resp)
        if 'deactivated' in self.resp.keys():
            self.delete = True
            self.close = True
            self.can_access_closed = False
        elif self.resp['is_closed'] & (not self.resp['can_access_closed']):
            self.close = True
            self.can_access_closed = False
            self.delete = False
        elif self.resp['is_closed'] & self.resp['can_access_closed']:
            self.close = True
            self.can_access_closed = True
            self.delete = False
        else:
            self.can_access_closed = True
            self.close = False
            self.delete = False
        self.user_id = self.resp['id']
        self.family = self.resp['last_name']
        self.name = self.resp['first_name']
        self.groups = vk_cursor.groups.get(user_id=id_, count=1000)['items']

# класс пользователя программой
class UserSearcher(UserVK):
    def about_searcher(self):
        self.sex = self.resp['sex']
        keys_ = self.resp.keys()
        if 'bdate' in keys_:
            self.bdate = self.resp['bdate']
            self.age = bdate_to_age(self.bdate)
        else:
            self.age = 29 #int(input('How old are you? - '))
        if 'city' in keys_:
            self.city = self.resp['city']['id']
        else:
            self.city = 119 # find_city()
        if 'activities' in keys_:
            self.activities = self.resp['activities']
        else:
            self.activities = input('Какова деятельность искомого партнера? - ')
        if 'interests' in keys_:
            self.interests = self.resp['interests']
        else:
            self.interests = input('Каковы интересы искомого партнера? - ')
        if 'about' in keys_:
            self.about = self.resp['about']
        else:
            self.about = input('Что интересно в поле "О себе" у искомого партнера? - ')
        if 'books' in keys_:
            self.books = self.resp['books']
        else:
            self.books = input('Какие книги интересны искомому партнеру? - ')
        if 'movies' in keys_:
            self.movies = self.resp['movies']
        else:
            self.movies = input('Какие фильмы интересны искомому партнеру? - ')
        if 'music' in keys_:
            self.music = self.resp['music']
        else:
            self.music = input('Какая музыка/исполнители интересны искомому партнеру? - ')
        if 'games' in keys_:
            self.games = self.resp['games']
        else:
            self.games = 'WOW' #input('Какие игры интересны искомому партнеру? - ')
        if 'tv' in keys_:
            self.tv = self.resp['tv']
        else:
            self.tv = '' #input('Какие ТВ-шоу интересны искомому партнеру? - ')
        if 'quotes' in keys_:
            self.quotes = self.resp['quotes']
        else:
            self.quotes = input('Какие цитаты нравятся искомому партнеру? - ')

    def search(self):
        # пока нахожу всех максимально подходящих. потом может поменяю условия поиска
        ''' sum the most important criteria return up to 4800 unique people (not friend):
            sort: 0 - populate, 1 - registered
            status: 6 - active search, 1 - not married
        '''
        self.about_searcher()
        sex_target = 1 #gender_determination(self.sex)
        response = []
        resp1 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=1,
            status=6,
        )
        response.extend(resp1['items'])
        resp2 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=0,
            status=6,
        )
        response.extend(resp2['items'])
        resp3 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=1,
            status=1,
        )
        response.extend(resp3['items'])
        resp4 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=0,
            status=1,
        )
        response.extend(resp4['items'])
        resp5 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=1,
        )
        response.extend(resp5['items'])
        resp6 = vk_cursor.users.search(
            count=1000,
            age_from=self.age - 2,
            age_to=self.age + 2,
            sex=sex_target,
            city=self.city,
            has_photo=1,
            fields=fields_found,
            is_friend=0,
            sort=0,
        )
        response.extend(resp6['items'])
        return response

    def __dict__(self):
        self.about_searcher()
        return {
            'about': self.about,
            'activities': self.activities,
            'books': self.books,
            'interests': self.interests,
            'movies': self.movies,
            'music': self.music,
            'quotes': self.quotes,
            'games': self.games,
            'tv': self.tv,
            'groups': self.groups,
        }

    def __str__(self): # ????????? after debug delete ????????????
        self.domain = self.resp['domain']
        self.fio = self.family + ' ' + self.name
        self.url = f'https://vk.com/{self.domain}'
        self.about_searcher()
        return f'{self.fio} - {self.url}\n{self.close, self.delete, self.can_access_closed}' \
               f'\n{self.groups}\n{self.city}'

# класс искомых персон
class UserFound(UserVK):
    def about_found(self):
        # ???переопределить self.resp = vk_cursor.users.get(user_ids=self.user_id, fields=fields_searcher)[0]
        # pprint(self.resp)
        # self.friends_mutual = vk_cursor.friends.getMutual(source_uid=self.user_id, target_uid=searcher_id)
        pass

    def top_photo(self):
        pass

    def __dict__(self):
        self.about_found()
        # for everyone of top 10 people
        # with top 3 photo

        # result_analise = [
        #     {'user_id': 123, 'name': 'Bla Bla 123', 'page_url': 'https://vk.com/id123',
        #      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},

        return {}

    def __str__(self): # ????????? after debug delete ????????????
        self.domain = self.resp['domain']
        self.fio = self.family + ' ' + self.name
        self.url = f'https://vk.com/{self.domain}'
        # self.about_finder()
        self.about_found()
        return f'{self.fio} - {self.url}\n{self.close, self.delete, self.can_access_closed}' \
               f'\n{self.groups}' #\n{self.friends_mutual}\n{self.city}'

if __name__ == '__main__':
    iam = UserSearcher().search()
    # from vkinder.common_functions import write_json
    # write_json(iam, 'data.json')
    print(len(iam))

