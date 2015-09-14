from django.conf import settings

import requests
import hashlib
import hmac
import json
import base64

API_KEY = settings.API_KEY
API_SECRET =settings.API_SECRET
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


def weebly_patch(my_url, my_data):
    # get url
    full_url = base_url + my_url

    # get hash
    my_content = 'PATCH' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hash = weebly_hash(my_content)

    # get headers
    post_header = {
        'Content-Type': 'application/json',
        'X-Public-Key': API_KEY,
        'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.put(full_url, data=json.dumps(my_data), headers=post_header)

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

