import requests
import hashlib
import hmac
import json
import base64

API_KEY = '0513rf6d0om4y1vmbm2gazxqrcwaye38'
API_SECRET = '8mzamuu3vpk9laud7a9e5uw0yobaywxozkhpdtgh6iscd15puk11jkwb8h714duy'


def weebly_post(my_url, my_data):

    # get url
    full_url = 'https://api.weeblycloud.com/' + my_url

    # get hash
    my_content = 'POST' + '\n' + my_url + '\n' + json.dumps(my_data)
    my_hmac = hmac.new(API_SECRET, my_content, digestmod=hashlib.sha256).hexdigest()
    my_hash = base64.b64encode(my_hmac)

    # get headers
    post_header = {
    'Content-Type': 'application/json',
    'X-Public-Key': API_KEY,
    'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.post(full_url, data=json.dumps(my_data), headers=post_header)

    return resp


def weebly_get(my_url):

    # get url
    full_url = 'https://api.weeblycloud.com/' + my_url

    # get hash
    my_content = 'GET' + '\n' + my_url
    my_hmac = hmac.new(API_SECRET, my_content, digestmod=hashlib.sha256).hexdigest()
    my_hash = base64.b64encode(my_hmac)

    # get headers
    get_header = {
    'X-Public-Key': API_KEY,
    'X-Signed-Request-Hash': my_hash,
    }

    # send request
    resp = requests.get(full_url, headers=get_header)

    return resp

if 0:
    # test post to create user
    my_url = 'user/'
    my_data = {'email':'t9@you.com'}
    resp = weebly_post(my_url, my_data)

if 0:
    # test post to create site for user
    my_url = 'user/60598425/site'
    my_data = {'domain': 'testsite231.com'}

    resp = weebly_post(my_url, my_data)

if 1:
    # test to fetch user info
    my_url = 'user/60598425'

    resp = weebly_get(my_url)

if 0:
    # test to fetch sites for user. fail
    my_url = 'user/60598425/site'

    resp = weebly_get(my_url)

if 1:
    # print results
    print(resp.status_code)
    print(resp.text)

