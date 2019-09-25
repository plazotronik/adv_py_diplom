#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from vkinder.db.objects import db, Searcher
from peewee import InternalError, IntegrityError


def create_table():
    '''check exist table'''
    try:
        db.connect()
        Searcher.create_table()
    except InternalError as err:
        return err


def add_rows(list_dicts):
    '''write result to db'''
    error = ''
    for dict_ in list_dicts:
        row = Searcher(
            user_id=dict_['user_id'],
            name=dict_['name'],
            page_url=dict_['page_url'],
            top_photo=' | '.join(dict_['top_photo'])
        )
        try:
            row.save()
        except IntegrityError as err:
            error += f'{err}\n'
            continue
    if error:
        return f'Was detected warnings.\n{error}'
    else:
        return 'OK'


def list_ids():
    '''list ids for check exist id'''
    column = Searcher.select(Searcher.user_id)
    ids = [data.user_id for data in column]
    return ids


def close_connect():
    return db.close()


if __name__ == '__main__':
    create_table()
    # from vkinder.data_operation.analise import result
    # print(add_rows(result))
    for i in list_ids():
        print(i)
    print(list_ids())

