import pprint

from dm_api_forum.apis.forum_api import ForumApi


def test_get_v1_fora_id_topics():

    forum_api = ForumApi(host='http://185.185.143.231:5051')
    fora_id = 'Общий'
    response = forum_api.get_v1_fora_id_topics(fora_id)
    print(response.status_code)
    pprint.pprint(response.json())
    assert response.status_code == 200, f'Список доступных топиков не был получен {response.json()}'
