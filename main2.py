from flask import Flask, render_template, redirect, url_for, request  # include the flask library
import locale
import json
import os
from os import listdir
from os.path import isfile, join

# pip install Flask-Mail
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("FROM_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app_language = 'en_EN'


@app.route('/portfolio')
def main_page():
    global app_language
    return render_template('portfolio.html', translations=languages.get(app_language))


@app.route('/work')
def work():
    return render_template('work.html', translations=languages.get(app_language))


@app.route('/education')
def education():
    return render_template('education.html', translations=languages.get(app_language))


@app.route('/dog')
def dog():
    return render_template('dog.html', translations=languages.get(app_language))


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', translations=languages.get(app_language))


@app.route('/dummy_function', methods=['POST'])
def dummy_function():
    global app_language
    lang = request.form['lang']
    if lang == 'en':
        app_language = "en_EN"
        return render_template('portfolio.html', translations=languages.get(app_language))
    elif lang == 'de':
        app_language = "de_DE"
        return render_template('portfolio.html', translations=languages.get(app_language))
    else:
        app_language = "ru_RU"
        return render_template('portfolio.html', translations=languages.get(app_language))

@app.route("/send-test-email", methods=['POST'])
def index():
    name = request.form['name']
    fname = request.form['fname']
    message = request.form['message']
    email = request.form['email']
    msg = Message('New email from ' + name + ' ' + fname + ' ', sender=request.form['email'], recipients=['23angel18@gmail.com'])
    msg.body = request.form['message']
    mail.send(msg)
    msg1 = Message(name + ' ' + fname + ',' + ' ' + 'your email is sent! Thank you.', sender='23angel18@gmail.com', recipients = [request.form['email']])
    mail.send(msg1)
    return "Message sent!"


def get_stats(input):
    return locale.format_string('%d', input)


def get_currencies(input):
    return locale.currency(input, international=True)


if __name__ == '__main__':
    app_language = 'ru_RU'
    locale.setlocale(locale.LC_ALL, app_language)
    languages = {}
    language_list = [f for f in listdir(os.path.join(".", 'language')) if
                     isfile(join(os.path.join(".", 'language'), f))]
    for lang in language_list:
        lang_code = lang.split('.')[0]
        with open(os.path.join(".", 'language', lang), 'r', encoding='utf8') as file:
            languages[lang_code] = json.loads(file.read())

    app.run(host="0.0.0.0", port=8080, debug=True)  # application will start listening for web request on port 5000
