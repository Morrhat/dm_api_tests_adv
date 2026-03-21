import pprint

import requests
from json import loads


def test_post_v1_account():
    # Регистрация пользователя

    login = 'Astarion_test_6'
    password = '1234567890'
    email = f'{login}@mail.com'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://185.185.143.231:5051/v1/account', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 201, f'Пользователь не был создан {response.json()}'

    # Получить письма из почтового сервера

    params = {
        'limit': '50',
    }

    response = requests.get('http://185.185.143.231:5025/api/v2/messages', params=params, verify=False)
    print(response.status_code)
    print(response.text)
    # pprint.pprint(response.json())
    assert response.status_code == 200, f'Письма не были получены {response.json()}'

    # Получить активационный токен
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            print(user_login)
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            print(token)
    assert token is not None, f'Токен не был получен {response.json()}'

    # # Активация пользователя
    #
    response = requests.put(f'http://185.185.143.231:5051/v1/account/{token}')
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f'Пользователь не был активирован {response.json()}'

    # Авторизовать нового пользоваетля

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://185.185.143.231:5051/v1/account/login', json=json_data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200, f'Пользователь не смог авторизоваться {response.json()}'
