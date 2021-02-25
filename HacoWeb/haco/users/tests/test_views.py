from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
from users.forms import RegistrationForm, LoginForm
from users.views import user_register, user_login
import pdb


# Tests for Views
class BaseViewsTest(TestCase):

    # Setup on init
    def setUp(self):
        # Init
        self.c = Client()
        self.factory = RequestFactory()
        self.home_url = reverse('home')
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        # Test Fields
        self.user_all_non_py_fields = {  # "_non_py_" here means all those fields which are
            'username': 'johndoe',  # unique to the custom user model and not required
            'password1': 'johndoespassword1234',  # from 'super' class
            'password2': 'johndoespassword1234',
            'email': 'johndoe@gmail.com',
            'first_name': 'John',
            'last_name': 'Doe;'
        }

        return super().setUp()

    # User Registration form is displayed is if the method does not equal to POST
    def test_create_user(self):
        # Create a user model and basic user
        um = get_user_model()
        user = um.objects.create_user(
            'johndoe@hotmail.com', 'johndoe', 'johndoespassword1234'
        )
        self.assertEqual(user.email, 'johndoe@hotmail.com')
        self.assertEqual(user.username, 'johndoe')
        self.assertTrue(user.is_active)
        self.assertEqual(str(user), "johndoe")

        # Exception raised without 1). email, 2). username or 3). password
        # 1).
        with self.assertRaises(ValueError):
            um.objects.create_user(
                email='', username='johndoe', password='johndoespassword1234'
            )

        # 2).
        with self.assertRaises(ValueError):
            um.objects.create_user(
                email='john@email.com', username='', password='johndoespassword1234'
            )
        # 3).
        with self.assertRaises(ValueError):
            um.objects.create_user(
                email='john@email.com', username='johnsdoe', password=''
            )

    def test_create_staffuser(self):
        # Create a user model
        staff_um = get_user_model()
        staff_user = staff_um.objects.create_staffuser(
            'johndoe@mail.com', 'johndoe', 'johndoespassword1234'
        )
        self.assertEqual(staff_user.email, 'johndoe@mail.com')
        self.assertEqual(staff_user.username, 'johndoe')
        self.assertEqual(str(staff_user), "johndoe")
        self.assertTrue(staff_user.is_staff)
        self.assertFalse(staff_user.is_superuser)
        self.assertTrue(staff_user.is_active)

        # User permissions
        with self.assertRaises(ValueError):
            staff_um.objects.create_staffuser(
                email='johndoe@email.com', username='johndoe123', password='johndoespass1234', is_staff=False
            )
        with self.assertRaises(ValueError):
            staff_um.objects.create_staffuser(
                email='johndoe@email.com', username='johndoe123', password='johndoespass1234', is_superuser=True
            )
        with self.assertRaises(ValueError):
            staff_um.objects.create_staffuser(
                email='johndoe@email.com', username='johndoe123', password='johndoespass1234', is_active=False
            )


# Test User Registration View
class RegisterViewsTest(BaseViewsTest):
    def test_register_form_save_POST(self):
        form_data = {
            'username': 'johndoe',
            'email': 'dean@mail.com',
            'password1': 'testuserpassword123',
            'password2': 'testuserpassword123'
        }
        form = RegistrationForm(data=form_data)

        # Form is Valid
        form = form.is_valid()
        # Create POST request
        request = self.c.post(self.register_url, form_data, format="text/html")
        # Redirects to home onece User is created
        self.assertRedirects(request, self.home_url)

    def test_register_form_GET(self):
        # Invalid form data
        form_data = {
            'username': '',
            'email': 'test@mail.com',
            'password1': 'testuserpassword123',
            'password2': 'testuserpassword123'
        }

        # Create GET request
        request = self.c.get(self.register_url, form_data, format="text/html")
        # Form is set to RegistrationForm()
        self.assertEqual(request.status_code, 200)


class LoginViewTest(BaseViewsTest):
    def test_returns_redirect(self):
        request = self.c.post(self.login_url, {'username': 'johndoe', 'password': 'johndoe1234'}, format="text/html")
        self.assertEqual(request.status_code, 200)

    def test_user_is_authenticated(self):
        um = get_user_model()
        user = um.objects.create_user(username='johndoe', password='johndoe1234', email='john@mail.com')
        auth = authenticate(username='johndoe', password='johndoe1234')
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(auth, self.home_url)


class LogoutViewTest(BaseViewsTest):
    # Test Logout method works
    def test_logout_user(self):
        request = self.c.post(self.logout_url)
        self.assertEqual(request.status_code, 302)
