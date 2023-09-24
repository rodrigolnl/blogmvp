import django.test
from django.test import TestCase
from django.test.client import JSON_CONTENT_TYPE_RE
from ..models import User
from rest_framework.test import APIRequestFactory


class UserTest(TestCase):
    def setUp(self):
        pass
        User.objects.create(email='rodrigonunes97@hotmail.com', username='rodrigo', password="345190")

    def test_register_valid_user(self):
        response = self.client.post('/users/register/', {
            "password": "345190",
            "email": "rodrigonunes972@hotmail.com",
            "username": "rodrigo2"
        }, content_type='application/json')
        self.assertEquals(201, response.status_code)

    def test_register_invalid_user(self):
        response = self.client.post('/users/register/', {
            "password": "345190",
            "email": "rodrigonunes97@hotmail.com",
            "username": "rodrigo"
        }, content_type='application/json')
        self.assertEquals(400, response.status_code)

    def test_get_user(self):
        pass

    def test_get_all_users(self):
        pass

    def test_login_valid(self):
        response = self.client.post('/users/login/', {
            "email": "rodrigonunes972@hotmail.com",
            "password": "345190",
        }, content_type='application/json')
        self.assertEquals(200, response.status_code)

    def test_login_invalid(self):
        response = self.client.post('/users/login/', {
            "email": "rodrigonunes973@hotmail.com",
            "password": "345190",
        }, content_type='application/json')
        self.assertEquals(401, response.status_code)
