# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu',
        url='https://2captcha.com/demo/recaptcha-v3',
        version='v3',
        action='test')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))