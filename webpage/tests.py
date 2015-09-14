from django.test import TestCase

import random
import string

from .utils import *

# Create your tests here.
class WeeblyApiTests(TestCase):

    def setUp(self):
        #self.email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6)) + '@test.com'
        self.email   = 'test23@yahoo.com'
        self.user_id = '60525257'
        self.site_id = ''
        self.domain = ''

    def test_new_user_account_creation(self):
        my_url = 'user/'
        my_data = "{'email': " + "'" + self.email + "'}"
        resp = weebly_post(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.user_id =  resp.json()['user']['user_id']


    def test_user_site_creation(self):
        my_url = 'user/' + self.user_id + '/site'
        self.domain = 'www.' + self.user_id + '.com'
        my_data = {'domain': self.domain}
        resp = weebly_post(my_url, my_data)


    def test_fetch_user_info(self):
        my_url = 'user/' + self.user_id

        resp = weebly_get(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['user']['email'], self.email)
        self.assertEqual(resp.json()['user']['test_mode'], True)
        self.assertEqual(resp.json()['user']['language'], 'en')


    def test_change_user_email_test_mode(self):
        my_url = 'user/' + self.user_id
        my_data = {'email': 'me_updated@test.com', 'test_mode': True, 'language': 'it'}

        resp = weebly_patch(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['user']['email'], self.email)
        self.assertEqual(resp.json()['user']['test_mode'], True)
        self.assertEqual(resp.json()['user']['language'], 'it')


    def test_disable_user(self):
        my_url = 'user/' + self.user_id + '/disable'

        resp = weebly_post(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)


    def test_enable_user(self):
        my_url = 'user/' + self.user_id + '/enable'

        resp = weebly_post(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], True)


    def test_create_site(self):
        my_url = 'user/' + self.user_id + '/site'
        my_data = "{'domain': '" + self.user_id +  \
                  ".com', 'site_title': 'My Test Website'}"

        resp = weebly_post(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['site']['domain'], self.user_id + '.com')
        self.assertEqual(resp.json()['site']['site_title'], 'My Test Website')
        self.site_id = resp.json()['site']['site_id']


    def test_delete_site(self):
        my_url = 'user/' + self.user_id + '/site/' + self.site_id
        resp = weebly_delete(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], 'True')


    def test_restore_site(self):
        my_url = 'user/' + self.user_id + '/site/' + self.site_id + '/restore'
        my_data = "{'domain': '" + self.domain + "'}"

        resp = weebly_post(my_url, my_data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['success'], 'True')


    def test_fetch_user_sites(self):
        my_url = 'user/' + self.user_id + '/site'

        resp = weebly_get(my_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['sites'][0]['domain'], self.domain)
        self.assertEqual(resp.json()['sites'][0]['site_id'], self.site_id)


