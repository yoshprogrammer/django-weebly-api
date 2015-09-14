from django.conf import settings

import requests
import hashlib
import hmac
import json
import base64

API_KEY         = settings.WEEBLY_API_KEY
API_SECRET      = settings.WEEBLY_API_SECRET
USER_ID         = settings.WEEBLY_TEST_ACCOUNT_ID

base_url = 'https://api.weeblycloud.com/'


def weebly_hash(my_content):
    my_hmac = hmac.new(API_SECRET, my_content, digestmod=hashlib.sha256).hexdigest()
    my_hash = base64.b64encode(my_hmac)

    return my_hash


def weebly_post(my_url, my_data=None):

    # get url
    full_url = base_url + my_url

    # get hash
    if (my_data == None):
        my_content = 'POST' + '\n' + my_url + '\n'
    else:
        my_content = 'POST' + '\n' + my_url + '\n' + json.dumps(my_data)

    my_hash = weebly_hash(my_content)

    # get headers
    if (my_data == None):
        post_header = {
            'X-Public-Key': API_KEY,
            'X-Signed-Request-Hash': my_hash,
        }
    else:
        post_header = {
            'Content-Type': 'application/json',
            'X-Public-Key': API_KEY,
            'X-Signed-Request-Hash': my_hash,
        }

    # send request
    if (my_data == None):
        resp = requests.post(full_url, headers=post_header)
    else:
        resp = requests.post(full_url, data=json.dumps(my_data), headers=post_header)

    return resp


def weebly_get(my_url):

    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'GET' + '\n' + my_url + '\n'
    my_hash = weebly_hash(my_content)

    # get headers
    get_header = {
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.get(full_url, headers=get_header)

    return resp


def weebly_put(my_url, my_data):
    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'PUT' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hash = weebly_hash(my_content)

    # get headers
    put_header = {
        'Content-Type': 'application/json',
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.put(full_url, data=json.dumps(my_data), headers=put_header)

    return resp


def weebly_patch(my_url, my_data):
    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'PATCH' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hash = weebly_hash(my_content)

    # get headers
    patch_header = {
        'Content-Type': 'application/json',
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.patch(full_url, data=json.dumps(my_data), headers=patch_header)

    return resp


def weebly_delete(my_url):
    full_url = base_url + my_url

    #get hash
    my_content = 'DELETE' + '\n' + my_url + '\n'
    my_hash = weebly_hash(my_content)

    # get headers
    post_header = {
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.delete(full_url, headers=post_header)

    return resp


def weebly_loginlink(user_id):
    my_url = 'user/' + user_id + '/loginlink'
    full_url = base_url + my_url

    #get hash
    my_content = 'POST' + '\n' + my_url + '\n'
    my_hash = weebly_hash(my_content)

    # get headers
    post_header = {
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    resp = requests.post(full_url)

    return resp


def create_user():
    # create test account
    my_url = 'user/'
    my_data = {'email': 'tester223423@fake.com'}
    resp = weebly_post(my_url, my_data)

    if (resp.status_code == 200):
        user_id = resp.json()['user']['user_id']
        print('Successfully created testacct@weebly_api_test.com')
        print('Please put this in the settings.py: WEEBLY_TEST_ACCOUNT_ID = ' + user_id)
    else:
        print('Couldn\'t create testacct@weebly_api_test.com. Does it already exist?')


def create_site():
    # create test site
    my_url = 'user/' + USER_ID + '/site'
    my_domain = USER_ID + '.com'
    my_data = {'domain': my_domain, 'site_title': 'My Test Website'}
    resp = weebly_post(my_url, my_data)
    if (resp.status_code == 200):
        print('Successfully created weeblytest.com')
    else:
        print('Couldn\'t create weeblytest.com. Does it already exist?')