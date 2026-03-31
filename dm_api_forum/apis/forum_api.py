import requests


class ForumApi:
    def __init__(
            self,
            host,
            headers=None
    ):
        self.host = host
        self.headers = headers


    def get_v1_fora(self):
        """
        Get list of available fora
        :return:
        """
        response = requests.get(
            url=f'{self.host}/v1/fora',
        )
        return response

    def get_v1_fora_id(self, fora_id: str):
        """
        Get certain fora by id
        :param fora_id:
        :return:
        """
        response = requests.get(
            url=f'{self.host}/v1/fora/{fora_id}'
        )
        return response

    def get_v1_fora_id_moderators(self, fora_id: str):
        """
        Get moderators of certain fora by id
        :param fora_id:
        :return:
        """
        response = requests.get(
            url=f'{self.host}/v1/fora/{fora_id}/moderators'
        )
        return response

    def get_v1_fora_id_topics(self, fora_id: str):
        """
        Get topics of certain fora by id
        :param fora_id:
        :return:
        """
        response = requests.get(
            url=f'{self.host}/v1/fora/{fora_id}/topics'
        )
        return response

    def post_v1_fora_id_topics(
            self,
            headers: dict[str, str],
            json_data: dict[str, str],
            fora_id: str
    ):
        """
        Post new topics in fora
        :param headers:
        :param json_data:
        :param fora_id:
        :return:
        """
        response = requests.post(
            url=f'{self.host}/v1/fora/{fora_id}/topics',
            headers=headers,
            json=json_data,
        )
        return response

    def delete_v1_fora_id_comments_unread(
            self,
            headers: dict[str, str],
            fora_id: str
    ):
        """
        Mark all forum comments as read
        :param headers:
        :param fora_id:
        :return:
        """
        response = requests.delete(
            url=f'{self.host}/v1/fora/{fora_id}/comments/unread',
            headers=headers
        )
        return response
