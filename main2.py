from flask import Flask, render_template, redirect, url_for, request  # include the flask library
import locale
import json
import glob
import os
from os import listdir
from os.path import isfile, join
from flask_mail import Mail, Message
import os

app = Flask(__name__)

@app.route('/portfolio')
def main_page():
    return render_template('portfolio.html', translations=language.get('en_EN'))

@app.route('/dummy_function', methods = ['POST'])
def dummy_function():
    lang = request.form['lang']
    print('Oh myyyy')
    print(lang)
    print("button clicked")
    if lang == 'en':
        return render_template('portfolio.html', translations=language.get('en_EN'))
    elif lang == 'de':
        return render_template('portfolio.html', translations=language.get('de_DE'))
    else:
        return render_template('portfolio.html', translations=language.get('ru_RU'))

@app.route("/send-test-email", methods=['POST'])
def index():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    msg = Message('You got email from ' + name + ' ', sender=request.form['email'], recipients = ['kima88445@gmail.com'])
    msg.body = request.form['message']
    mail.send(msg)
    # msgn = Message(name + ' ' + 'Thanks for your email!', sender='kima88445@gmail.com', recipients = [request.form['email']])
    # mail.send(msgn)
    return "Thanks for your email!"

def get_stats(input):
    return locale.format_string('%d', input)

def get_currencies(input):
    return locale.currency(input, international=True)

@app.route('/random')
def random_page():
    return render_template('index.html')

@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/mypets")
def mypets():
    return render_template('mypets.html')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# TODO: replace with your email
app.config['MAIL_USERNAME'] = os.getenv("FROM_EMAIL")
# TODO:
# The following line should contain a password set in app passwords ion your google account.
# The password itself should be stored in .env file. DO NOT PUSH YOUR .env FILE TO GIT!!!
# Look at the example in .dummy-env. This is how your .env should look like
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


if __name__ == '__main__':
    app_language = 'ru_RU'
    locale.setlocale(locale.LC_ALL, app_language)
    language = {}
    language_list = [f for f in listdir(os.path.join(".", 'language')) if isfile(join(os.path.join(".", 'language'), f))]
    for lang in language_list:
        lang_code = lang.split('.')[0]
        with open(os.path.join(".", 'language', lang), 'r', encoding='utf8') as file:
            language[lang_code] = json.loads(file.read())

app.run(host="0.0.0.0", port=5000, debug=True)