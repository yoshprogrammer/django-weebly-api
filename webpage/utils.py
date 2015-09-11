import requests
import hashlib
import hmac
import json
import base64

API_KEY = '0513rf6d0om4y1vmbm2gazxqrcwaye38'
API_SECRET = '8mzamuu3vpk9laud7a9e5uw0yobaywxozkhpdtgh6iscd15puk11jkwb8h714duy'


def weebly_api(my_method, my_data, my_url):

    # get url
    post_url = 'https://api.weeblycloud.com/' + my_url

    # get hash
    post_content = my_method + '\n' + post_url + '\n' + json.dumps(my_data)
    post_content = bytes(post_content).encode('utf-8')
    post_secret = bytes(API_SECRET).encode('utf-8')
    post_hmac = hmac.new(post_secret, post_content, digestmod=hashlib.sha256).digest()
    post_hash = base64.b64encode(post_hmac)

    # get headers
    post_header = {
    'Content-Type': 'application/json',
    'X-Public-Key': API_KEY,
    'X-Signed-Request-Hash': post_hash,
    }

    # send request
    #resp = requests.post(post_url, data=json.dumps(my_data), headers=post_header)

    resp = requests

    resp.json = {"user": {
        "user_id": "39793399",
        "email": "test231@yahoo.com",
        "test_mode": True,
        "language": "en"
    }}
    return resp


# get url
my_url = 'user/'

# define method
my_method = 'POST'

# get data
my_data = {
    'email': 'test231@yahoo.com',
    'test_mode': True,
    'language': 'en',
}

r = weebly_api(my_method, my_data, my_url)

print(r.json)


r.json['user']['email']