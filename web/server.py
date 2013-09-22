# - * - encoding: utf-8 - * -
from __future__ import unicode_literals

from flask import Flask, render_template, request, session, redirect
from helpers import name_gen, password_gen, register_reddit, get_captcha

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    response = None
    if request.method == 'POST':
        passwd = password_gen()
        response = register_reddit(username=request.form['user'],
                                   passwd=passwd,
                                   captcha=request.form['captcha'],
                                   iden=request.form['iden'])
        if len(response) < 1:
            session['username'] = request.form['user']
            session['passwd'] = passwd
            return redirect('/success')
    number = False if request.args.get('number') is None else True
    return render_template('register.html', name=name_gen(number),
                           iden=get_captcha(), errors=response)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    app.run()
