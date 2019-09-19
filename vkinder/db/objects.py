#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from playhouse.sqlite_ext import SqliteExtDatabase
from peewee import Model, SqliteDatabase, MySQLDatabase
from peewee import AutoField, TextField, DateTimeField, IntegerField, CharField, FloatField, PrimaryKeyField, TimestampField, fn
from peewee import InternalError, IntegrityError
# from peewee import *
from vkinder.init_app import searcher_id
# import json
from datetime import datetime


db = SqliteExtDatabase('vkinder.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -64 * 1000,
    'synchronous': 0})
table = 'searcher_%s' % searcher_id

# database
class Vkinder(Model):
    class Meta:
        database = db

# table
class Searcher(Vkinder):
    id = AutoField()
    user_id = IntegerField(null=False, unique=True)
    name = CharField(null=False)
    page_url = CharField(null=False)
    top_photo = TextField(null=False)
    date_search = DateTimeField(default=datetime.now())

    class Meta:
        db_table = table
        order_by = ('id',)
