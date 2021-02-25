from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import user_register, user_login, user_logout


class TestUrls(SimpleTestCase):

    def test_user_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, user_register)
