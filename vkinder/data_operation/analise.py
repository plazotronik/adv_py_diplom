#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tqdm._main import tqdm
from vkinder.vk.objects import UserVK
from vkinder.data_operation.functions import delete_exist_id, str_to_list


# временная замена выборки из БД id прошлых поисков
# patch_list_userid_from_db = [555007153, 556357138, 558370929, 559721024, 525246846, 499544698, 494211559, 478940773]
# # userid_from_db = patch_list_userid_from_db
# userid_from_db = list_ids()
# userid_from_db = [123, 321, 456, 654, 789, 987, 822505, 1153476, 2228637, 3905194, 4819484, 7293334, 8743424,
#                   9858118, 10547609, 10806455, 11203874, 11274554, 15993296, 16043506, 17253538, 17406140,
#                   21252072, 26684937, 30159457, 30581410, 31687790, 32428920, 33224090, 33982223, 34091567,
#                   37545765, 38036004, 40013129, 47562498, 48193670, 54753543, 57892315, 57925359, 83956009,
#                   85701300, 99302626, 106191879, 106221610, 106540522, 111375182, 111505617, 112865007, 135347023,
#                   140084040, 140660056, 154343066, 159842189, 177152694, 208778999, 220095377, 256824531,
#                   282200702, 299525884, 305973427, 332638108, 349634592, 386636225, 396807671, 508369755,
#                   539495206, 544052708, 546588781, 549513923, 551104725, 552087614, 554235044]

# временная замена результатов анализа для записи в БД
# patch_result_analise = [
#     {'user_id': 123, 'name': 'Bla Bla 123', 'page_url': 'https://vk.com/id123',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
#     {'user_id': 456, 'name': 'Bla Bla 456', 'page_url': 'https://vk.com/id456',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
#     {'user_id': 789, 'name': 'Bla Bla 789', 'page_url': 'https://vk.com/id789',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
#     {'user_id': 321, 'name': 'Bla Bla 312', 'page_url': 'https://vk.com/id123',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
#     {'user_id': 654, 'name': 'Bla Bla 654', 'page_url': 'https://vk.com/id456',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
#     {'user_id': 987, 'name': 'Bla Bla 987', 'page_url': 'https://vk.com/id789',
#      'top_photo': ['https://photo_1', 'https://photo_2', 'https://photo_3']},
# ]
# result = patch_result_analise


# описание пользователя нашей программы с его интересами
# reference = UserSearcher().__dict__()
# print(reference)


# data_search - временная замена результату поиска API VK
# по сути датасет из 4800 уникальных найденных персон
# не прикрепляю файл, т.к. может содержать не публичные данные
# data_search = []
# def tmp_data():
#     with open('data.json') as file:
#         data_search.extend(json.load(file))
# tmp_data()


# удаление тех кто уже был найден ранее
# data_search = delete_exist_id(data_search, userid_from_db)

class Analise:
    # варианты весов
    # weights1 = {
    #     'activities': 0.6,
    #     'about': 0.48,
    #     'interests': 0.68,
    #     'music': 0.54,
    #     'movies': 0.19,
    #     'tv': 0.05,
    #     'books': 0.5,
    #     'games': 0.16,
    #     'quotes': 0.23,
    #     'groups': 0.45,
    #     'common_count': 0.15,
    # }
    weights = {
        'activities': 14,
        'about': 12,
        'interests': 16,
        'music': 12,
        'movies': 5,
        'tv': 1,
        'books': 11,
        'games': 4,
        'quotes': 6,
        'status': 5,
        'groups': 10,
        'common_count': 4,
    }
    # weights_alt = {
    #     'activities': 15,
    #     'about': 12,
    #     'interests': 17,
    #     'music': 13,
    #     'movies': 5,
    #     'tv': 1,
    #     'books': 12,
    #     'games': 4,
    #     'quotes': 6,
    #     'groups': 11,
    #     'common_count': 4,
    # }



    # связка id и кол-ва голосов
    vote = {}

    def __init__(self, list_dicts, ids_from_db, reference, cursor):
        # объединить анализ в класс и добавить сквозной self.tqdm (self.tqdm.update(13))
        self.tqdm = tqdm(desc='Magic', total=1, unit=' lucks', leave=False)
        self.data = delete_exist_id(list_dicts, ids_from_db)
        # описание пользователя нашей программы с его интересами
        # reference = UserSearcher().__dict__()
        self.reference = reference
        self.cursor = cursor

    def vote_put(self):
        for key_ in self.weights.keys():
            if key_ in ['common_count', 'groups']:
                continue
            else:
                list_searcher = str_to_list(self.reference[key_])
                for dict_ in self.data:
                    self.tqdm.update(3)
                    try:
                        list_found = str_to_list(dict_[key_])
                    except Exception as err:
                        continue
                    else:
                        for word in list_searcher:
                            if word in list_found:
                                self.tqdm.update(5)
                                try:
                                    tmp = self.vote[dict_['id']]
                                except KeyError as err:
                                    self.vote[dict_['id']] = self.weights[key_]
                                else:
                                    self.vote[dict_['id']] += self.weights[key_]

    def vote_friends_mutual(self):
        self.vote_put()
        for dict_ in self.data:
            self.tqdm.update(2)
            try:
                friends = dict_['common_count']
            except Exception as err:
                continue
            else:
                if friends:
                    self.tqdm.update(6)
                    try:
                        tmp = self.vote[dict_['id']]
                    except KeyError as err:
                        self.vote[dict_['id']] = (self.weights['common_count'] * friends)
                    else:
                        self.vote[dict_['id']] += (self.weights['common_count'] * friends)

    def vote_groups(self):
        self.vote_friends_mutual()
        set_searcher = set(self.reference['groups'])
        for dict_ in self.data:
            self.tqdm.update(11)
            if dict_['is_closed'] & (not dict_['can_access_closed']):
                self.tqdm.update(1)
                continue
            else:
                self.tqdm.update(7)
                set_found = set(UserVK(self.cursor, dict_['id']).groups)
                # set_found = set(FastUserVK(dict_['id']).getgroups())
                count_groups = len(set_searcher.intersection(set_found))
                if count_groups:
                    self.tqdm.update(16)
                    try:
                        tmp = self.vote[dict_['id']]
                    except KeyError as err:
                        self.vote[dict_['id']] = (self.weights['groups'] * count_groups)
                    else:
                        self.vote[dict_['id']] += (self.weights['groups'] * count_groups)

    def result(self):
        # self.vote_friends_mutual()
        # self.vote_groups()
        self.tqdm.close()

        # print(len(self.vote))
        # print(self.vote)
        # print(get_top_ids(self.vote))
        return self.vote
        # return [FastUserVK(user_id).__dict__() for user_id in get_top_ids(self.vote)]


if __name__ == '__main__':
    pass
    # from datetime import datetime
    # from pprint import pprint
    # start = datetime.now()
    # print(start)
    # analize = Analise(data_search)
    # # analize.vote_friends_mutual()
    # analize.vote_groups()
    # result = analize.result()
    # add_rows(result)
    # pprint(result)
    # # print(list_ids())
    #
    # # подсчитываем голоса
    # # for key in weights.keys():
    # #     if key in ['common_count', 'groups']:
    # #         continue
    # #     else:
    # #         vote_put(data_search, reference, key, weights[key])
    # # print(datetime.now())
    # # vote_friends_mutual(data_search)
    # # print(datetime.now())
    # # vote_groups(data_search, reference)
    #
    #
    # # vote_put(data_search, reference, 'quotes', weights['quotes'])
    # # vote_put(data_search, reference, 'about', weights['about'])
    # # vote_put(data_search, reference, 'music', weights['music'])
    # # vote_put(data_search, reference, 'activities', weights['activities'])
    # # vote_put(data_search, reference, 'interests', weights['interests'])
    # # vote_put(data_search, reference, 'books', weights['books'])
    # # vote_put(data_search, reference, 'movies', weights['movies'])
    # # vote_put(data_search, reference, 'tv', weights['tv'])
    # # vote_put(data_search, reference, 'games', weights['games'])
    #
    # # print(vote)
    # # print(len(vote))
    # stop = datetime.now()
    # print(stop)
    # print((start - stop).seconds/60)







