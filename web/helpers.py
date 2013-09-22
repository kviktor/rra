# - * - encoding: utf-8 - * -
import random
import requests
from settings import USER_AGENT as ua
import os


def name_gen(number=False):
    files = ['adjectives', 'animals', 'cities']  # adverbs
    name = ''

    # we need this for command line usage from another directory
    path = os.path.dirname(__file__)

    for f in files:
        with open(os.path.join(path, 'static', f), 'r') as words:
            # maximum username length is 20, so we don't want to exceed
            # that
            chosen = random.choice(list(words)).strip()
            if len(name + chosen) <= 20:
                name += chosen.strip().replace(" ", "")
            else:
                # we insert a random number
                # this way the username gonna be a bit more random
                number = True

    rand = random.randint(0, len(name))
    return "%s%d%s" % (name[:rand], rand, name[rand:20]) if number else name


def password_gen():
    return '%x' % random.randrange(pow(2, 30), pow(2, 40))


def get_captcha():
    data = {
        'api_type': 'json'
    }

    headers = {
        'User-Agent': ua
    }

    re = requests.post("http://www.reddit.com/api/new_captcha",
                       data=data,
                       headers=headers)
    return re.json()['json']['data']['iden']


def register_reddit(username, passwd, captcha, iden):
    data = {
        'api_type': 'json',
        'user': username,
        'passwd': passwd,
        'passwd2': passwd,
        'captcha': captcha,
        'iden': iden,
        'rem': False,
    }

    headers = {
        'User-Agent': ua
    }

    r = requests.post("http://www.reddit.com/api/register",
                      headers=headers,
                      data=data)
    return r.json()['json'].get('errors')
