import requests


class LoginApi:
    def __init__(
            self,
            host,
            headers=None
    ):
        self.host = host
        self.headers = headers

    def post_v1_account_login(
            self,
            json_data: dict[str, str]
    ):
        """
        POST
        /v1/account/login
        :param json_data:
        :return:
        Authenticate via credentials
        """
        response = requests.post(
            url=f'{self.host}/v1/account/login',
            json=json_data
        )
        return response

    def delete_v1_account_login(
            self,
            headers: dict[str, str]
    ):
        """
        Logout current user
        :param headers:
        :return:
        """
        response = requests.delete(
            url=f'{self.host}/v1/account/login',
            headers=headers
        )
        return response

    def delete_v1_account_login_all(
            self,
            headers: dict[str, str]
    ):
        """
        Logout from every device
        :param headers:
        :return:
        """
        response = requests.delete(
            url=f'{self.host}/v1/account/login/all',
            headers=headers
        )
        return response