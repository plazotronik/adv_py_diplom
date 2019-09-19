#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

#  для записи в файл *.json
def write_json(text, filename, path='', mode='wt'):
    # доработать path для переопределения \/
    if path:
        make_dir(path)
    out_file = os.path.join(path, f'{filename}')
    txt = json.dumps(text, sort_keys=True, indent=4, ensure_ascii=False)
    with open(out_file, mode=mode, encoding='utf8') as file:
        file.write(txt)

# для создания пути каталогов
def make_dir(path):
    pwd = os.getcwd()
    if '\\' in path:
        lst = path.split('\\')
        for i in lst:
            if i in os.listdir(): # os.path.exists(i)
                os.chdir(i)
            else:
                os.mkdir(i)
                os.chdir(i)
    elif '/' in path:
        lst = path.split('/')
        for i in lst:
            if i in os.listdir():
                os.chdir(i)
            else:
                os.mkdir(i)
                os.chdir(i)
    else:
        if path not in os.listdir():
            os.mkdir(path)
    os.chdir(pwd)


if __name__ == '__main__':
    # write_json(config_db, 'config_db.json')
    pass
