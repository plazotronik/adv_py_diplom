#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
import getpass


APP_ID = 7136810
# +2+4+8+16+64+128+1024+131072+262144
SCOPE = 394462 # expires in 86400 seconds
# +2+4+8+16+64+128+1024+131072+262144+65536
# SCOPE = 459998 # offline - expires in 0 seconds


def two_factor_auth():
    """ При двухфакторной аутентификации вызывается эта функция."""
    # key = input("Enter authentication code: ")
    key = getpass.getpass("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True
    return key, remember_device


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
        https://vk-api.readthedocs.io/en/latest/exceptions.html#vk_api.exceptions.Captcha
    """
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


def vk_login(login, password, two_factor=False):
    if two_factor:
        vk_session = vk_api.VkApi(login, password, app_id=APP_ID, scope=SCOPE,
                                  auth_handler=two_factor_auth())
    else:
        vk_session = vk_api.VkApi(login, password, app_id=APP_ID, scope=SCOPE)
    try:
        vk_session.auth(token_only=True)
    except vk_api.Captcha as err:
        print('need captcha') # check - work it is?
        vk_session = vk_api.VkApi(login, password, app_id=APP_ID, scope=SCOPE,
                                  captcha_handler=captcha_handler)
    except vk_api.AuthError as err:
        print(err)
    else:
        return vk_session

#
# if __name__ == '__main__':
#     vk_ = vk_login()
#     vk = vk_.get_api()
#     print(vk.friends.get())
#     print(vk_.token['access_token'])
