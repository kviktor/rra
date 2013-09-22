# RRA (Random Reddit Account)

Create a random reddit user. Username is generated from animal names, adjectives and cities.

## Usage
First install the requirements

```
$ pip install -r requirements.txt
```

then use the app either from command line or via the nice little web page.

### Command line


```
$ python register.py
```

Just copy the link into your browser / download the captcha, solve it and you are ready to go!

### Web

```
$ cd web/
```

```
$ python server.py
```

This starts the Flask development server. Obviously in production you should not use this (especially because DEBUG is set to True) instead try something like uWSGI + nginx.
