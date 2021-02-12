from django.test import TestCase, RequestFactory, client
from django.urls import reverse
from users.views import user_register, user_login, user_logout
from users.forms import RegistrationForm
from users.models import User


# Create your tests here.
class BaseUserTest(TestCase):
    def setUp(self):
        # Init
        self.factory = RequestFactory()
        self.client = client.Client()
        # URLs
        self.register_url = reverse('register')

        # Test Fields
        self.user_all_non_py_fields = {             # "_non_py_" here means all those fields which are
            'username': 'johndoe',                  # unique to the custom user model and not required
            'password': 'johndoespassword1234',     # from 'super' class
            'email': 'johndoe@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe;'
        }

        self.form = RegistrationForm(self.user_all_non_py_fields)

        # self.user_all_non_py_fields = User.objects.create(
        #     username='johndoe',
        #     password='johndoepassword1234',
        #     email='johndoe@gmail.com',
        #     first_name='John',
        #     last_name='Doe',
        #     country='Ireland'
        # )
        #
        self.user_missing_email = {
            'username': 'johndoe1',
            'password': 'johndoe1234',
            'email': '',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        return super().setUp()


class UserRegisterTest(BaseUserTest):
    # User Registration form is displayed is if the method does not equal to POST
    def test_user_register_view_if_method_not_POST(self):
        request = self.factory.get('register')
        response = user_register(request)
        self.assertEqual(response.status_code, 200)

    # POST method accepted and form is created
    def test_register_POST(self):
        request = self.factory.post('register')
        response = user_register(request)
        self.assertEqual(response.status_code, 200)

    # User can't register without email
    def test_user_can_register_without_email(self):
        request = self.client.post(self.register_url, self.user_missing_email, format='text/html')
        self.assertFormError(request, 'form', 'email', 'This field is required.')


# class UserLoginTest(BaseUserTest):
#     def test_view_page_ok(self):
#         response = self.client.get(self.login_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/login.html')
