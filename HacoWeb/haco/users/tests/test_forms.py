from django.test import TestCase, RequestFactory, client
from http import HTTPStatus
from django.urls import reverse
from users.views import user_register, user_login, user_logout
from users.forms import RegistrationForm, LoginForm
from users.models import User


# Create your tests here.
class BaseUserFormsTest(TestCase):
    def setUp(self):

        # Init
        self.factory = RequestFactory()
        self.client = client.Client()

        # URLs
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        # Test Fields
        self.user_all_non_py_fields = {             # "_non_py_" here means all those fields which are
            'username': 'johndoe',                  # unique to the custom user model and not required
            'password1': 'johndoespassword1234',     # from 'super' class
            'password2': 'johndoespassword1234',
            'email': 'johndoe@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe;'
        }
        self.user_missing_email = {
            'username': 'johndoe1',
            'password': 'johndoe1234',
            'email': '',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        self.user_missing_password = {
            'username': 'johndoe1',
            'password': '',
            'email': 'johndoe@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        # User objects
        self.user_all_non_py_fields_form = User.objects.create(
            username='johndoe',
            password='johndoepassword1234',
            email='johndoe@gmail.com',
            first_name='John',
            last_name='Doe',
            country='Ireland'
        )

        return super().setUp()


class UserRegisterFormsTest(BaseUserFormsTest):
    # POST method accepted and form is created
    def test_register_POST(self):
        request = self.factory.post('register')
        response = user_register(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # User can't register without email
    def test_user_cannot_register_without_email(self):
        request = self.client.post(self.register_url, self.user_missing_email, format='text/html')
        self.assertFormError(request, 'form', 'email', 'This field is required.')

    # User can't register without passwords one and two filled
    def test_user_cannot_register_without_password(self):
        request = self.client.post(self.register_url, self.user_missing_password, format='text/html')
        self.assertFormError(request, 'form', 'password1', 'This field is required.')
        self.assertFormError(request, 'form', 'password2', 'This field is required.')

    # User form isn't saved when invalid
    def test_user_registration_form_not_save_invalid(self):
        form_data = self.user_all_non_py_fields
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    # User form is saved when valid


# class UserLoginTest(BaseUserFormsTest):
#     def test_view_page_ok(self):
#         response = self.client.get(self.login_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/login.html')
