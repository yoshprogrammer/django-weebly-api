# django-weebly-api
## The core python functions have been moved into the python distribution "weebly".
https://pypi.python.org/pypi/weebly/
## Use "pip install weebly" to install.
 
This codebase will demonstrate a simple project using all features of Weebly's cloud platform.

To configure you must put your Weebly API keys in a settings file such as "local.py" and include the base.py. It's also
good to create a "user" account on Weebly Cloud first using their admin panel. Put the user_id in the local.py also.

        from .base import *
        
        WEEBLY_API_KEY = 'your api key here'
        WEEBLY_API_SECRET = 'your secret key here'
        WEEBLY_TEST_ACCOUNT_ID = 'your test account here'

New accounts can be created using the 'signup/' url. But __accounts cannot be deleted!__ Do not create too many accounts!
