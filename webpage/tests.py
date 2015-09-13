from django.test import TestCase

import random
import string

from .utils import *

# Create your tests here.
class WeeblyApiTest(TestCase):

    def setUp(self):
        self.email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6)) + '@test.com'

    def test_new_user_account_creation(self):
        print(self.email)
        self.assertEqual(True, True)

    def test_new_user_site_creation(self):
        self.assertEqual(True, False)
