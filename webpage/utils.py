import requests
import hashlib
import hmac
import json
import base64

API_KEY = '0513rf6d0om4y1vmbm2gazxqrcwaye38'
API_SECRET = '8mzamuu3vpk9laud7a9e5uw0yobaywxozkhpdtgh6iscd15puk11jkwb8h714duy'

# get url
base_url = "https://api.weeblycloud.com/"
my_url = "user/"
post_url = base_url + my_url

# get data
post_data = {
    'email': 'test@yahoo.com'
}

# get hash
post_hash = "POST" + "\n" + post_url + "\n" + json.dumps(post_data)
my_hash = base64.b64encode(hmac.new(API_SECRET, post_hash, digestmod=hashlib.sha256).digest())

# get headers
post_header = {
'Content-Type': 'application/json',
'X-Public-Key': 'API_KEY',
'X-Signed-Request-Hash': my_hash
}

# create request
r = requests.post(post_url, data=json.dumps(post_data), headers=post_header)


print(r)
