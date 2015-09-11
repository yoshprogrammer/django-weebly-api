import requests
import hashlib
import hmac
import json
import base64

API_KEY = '0513rf6d0om4y1vmbm2gazxqrcwaye38'
API_SECRET = '8mzamuu3vpk9laud7a9e5uw0yobaywxozkhpdtgh6iscd15puk11jkwb8h714duy'

# get url
base_url = 'https://api.weeblycloud.com/'
my_url = 'user/'
post_url = base_url + my_url

# get data
post_data = {
    'email': 'test231@yahoo.com',
    'test_mode': True,
    'language': 'en',
}

# get hash
post_content = 'POST' + '\n' + post_url + '\n' + json.dumps(post_data)
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
r = requests.post(post_url, data=json.dumps(post_data), headers=post_header)

print(r.status_code)
print(r.text)
print(r.json)


