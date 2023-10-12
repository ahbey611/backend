import unittest

from django.test import Client, TestCase
from django.urls import reverse

from user import views as user_views
from user.models import User
from utils.jwt import encrypt_password


class APITestCase(TestCase):

    def setUp(self):
        user = User(username="testuser", password=encrypt_password(str("testuser")),
                    nickname="test", mobile="+86.123456789012", magic_number=0, url="https://baidu.com")
        user.save()
        self.client = Client()

    def test_login(self):
        """
        使用错误的信息进行登录，检查返回值为失败
        """
        data = {"username": "123", "password": "21321"}
        response = self.client.patch(
            reverse(user_views.login),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        self.assertEqual(json_data['message'], "Invalid credentials")
        self.assertEqual(response.status_code, 401)

        """
        使用正确的信息进行登录，检查返回值为成功
        """
        # 获取setUp函数中存储的密码
        data = {"username": "testuser", "password": "testuser"}
        response = self.client.patch(
            reverse(user_views.login),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        self.assertEqual(json_data['username'], "testuser")

        """
        进行登出，检查返回值为成功
        """
        # 模拟用户登录，要获取jwt
        response = self.client.patch(
            reverse(user_views.login),
            data=data,
            content_type="application/json",
        )

        json_data = response.json()
        # 获取jwt令牌
        jwt_token = json_data["jwt"]

        response = self.client.patch(
            reverse(user_views.logout),
            HTTP_AUTHORIZATION=f"{jwt_token}"
        )
        json_data = response.json()
        self.assertEqual(json_data['message'], "ok")

    def test_register(self):
        """
        Example: 使用错误信息进行注册，检查返回值为失败
        在完成register_params_check后，你需要修改这里的错误信息和返回码
        """
        data = {"username": "123", "password": "21321"}
        response = self.client.post(
            reverse(user_views.register_user),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        # username格式不正确
        self.assertEqual(json_data['message'], "Invalid arguments: username")
        self.assertEqual(response.status_code, 400)

        """
        使用正确的信息进行注册，检查返回值为成功
        """
        data = {
            "username": "testUser123",
            "password": "89-S*d^aW_t^s*d",
            "nickname": "test123",
            "mobile": "+86.123456789012",
            "magic_number": 123,
            "url": "https://baidu.com"
        }
        response = self.client.post(
            reverse(user_views.register_user),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        self.assertEqual(json_data['message'], "ok")

        """
        TODO: 使用正确注册信息进行登录，检查返回值为成功
        """
        response = self.client.patch(
            reverse(user_views.login),
            data=data,
            content_type="application/json"
        )
        json_data = response.json()
        self.assertEqual(json_data['username'], "testUser123")
        self.assertEqual(json_data['nickname'], "test123")

    def test_logout(self):
        """
        未登录直接登出
        """
        response = self.client.post(
            reverse(user_views.logout),
        )
        json_data = response.json()

        # print("返回的错误：",json_data)
        self.assertEqual(json_data['message'], "User must be authorized.")


if __name__ == '__main__':
    unittest.main()
