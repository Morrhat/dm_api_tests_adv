import json
import pprint
import time
from json import loads

from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi


def test_put_v1_account_email():

    account_api = AccountApi(host='http://185.185.143.231:5051')
    login_api = LoginApi(host='http://185.185.143.231:5051')
    mailhog_api = MailhogApi(host='http://185.185.143.231:5025')


    # Регистрация пользователя
    login = 'Astarion_test_38'
    password = '1234567890'
    email = f'{login}@mail.com'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'

    # Получить письма из почтового сервера

    response = mailhog_api.get_api_v2_messages()

    print(response.status_code)
    # print(response.text)
    # pprint.pprint(response.json())
    assert response.status_code == 200, f'Письма не были получены {response.json()}'

    # Получить активационный токен
    token = get_activation_token_by_login(login, response)

    assert token is not None, f'Токен не был получен {response.json()}'

    # # Активация пользователя
    response = account_api.put_v1_account_token(token=token)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f'Пользователь не был активирован {response.json()}'

    # Авторизовать нового пользоваетля
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = login_api.post_v1_account_login(json_data=json_data)

    print(response.status_code)
    print(response.text)
    # print(response.headers['X-Dm-Auth-Token'])
    active_token = response.headers['X-Dm-Auth-Token']
    assert response.status_code == 200, f'Пользователь не смог авторизоваться {response.json()}'


    # Смена электронной почты пользователя
    headers = {
        'X-Dm-Auth-Token': active_token
    }

    json_data = {
        'login': login,
        'password': password,
        'email': 'Astarion_test@mail.com',
    }

    response = account_api.put_v1_account_email(headers=headers, json_data=json_data)
    print(response.status_code)
    print(response.text)


    # Получить новые письма из почтового сервера
    response = mailhog_api.get_api_v2_messages()

    print(response.status_code)
    # print(response.text)
    # pprint.pprint(response.json())

    assert response.status_code == 200, f'Письма не были получены {response.json()}'

    # Получить новый активационный токен смены почты
    token = get_activation_token_by_login(login, response)

    assert token is not None, f'Токен не был получен {response.json()}'

    # Повторная Активация пользователя с новыми данными
    response = account_api.put_v1_account_token(token=token)

    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f'Пользователь не был активирован {response.json()}'

    # Авторизовать пользоваетля с новыми данными
    json_data = {
        'login': login,
        'email': 'Astarion_test@mail.com',
        'password': password,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    active_token = response.headers['X-Dm-Auth-Token']
    print(response.status_code)
    print(response.text)


    # Получить данные текущего пользователя
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': active_token,
    }

    response = account_api.get_v1_account(headers=headers)
    print(response.status_code)
    print(response.text)






def get_activation_token_by_login(login: str, response):
    token = None
    for item in response.json()['items']:
        body = item['Content']['Body']
        # Проверяем, что body похож на JSON (начинается с '{' или '[')
        if not isinstance(body, str) or not (body.startswith('{') or body.startswith('[')):
            continue  # пропускаем не-JSON данные
        try:
            user_data = loads(body)
        except json.JSONDecodeError:
            continue  # если не распарсилось, пропускаем
        user_login = user_data.get('Login')
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            break
    return token
