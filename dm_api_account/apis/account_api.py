import requests


class AccountApi:
    def __init__(
            self,
            host,
            headers=None
    ):
        self.host = host
        self.headers = headers

    def post_v1_account(
            self,
            json_data: dict[str, str]
    ):
        """
        Register new user
        :param json_data:
        :return:
        """
        response = requests.post(
            url=f'{self.host}/v1/account',
            json=json_data
        )
        return response

    def put_v1_account_token(
            self,
            token
    ):
        """
        Activate registered user
        :param token:
        :return:
        """
        response = requests.put(
            url=f'{self.host}/v1/account/{token}',
        )
        return response

    def get_v1_account(
            self,
            headers: dict[str, str]
    ):
        """
        Get current user
        :param headers:
        :return:
        """
        response = requests.get(
            url=f'{self.host}/v1/account',
            headers=headers
        )
        return response

    def put_v1_account_email(
            self,
            headers: dict[str, str],
            json_data: dict[str, str]
    ):
        """
        Change email address
        :param headers:
        :param json_data:
        :return:
        """
        response = requests.put(
            url=f'{self.host}/v1/account/email',
            headers=headers,
            json=json_data
        )
        return response
