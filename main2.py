 # include the flask library
from flask import Flask, render_template, redirect, url_for, request, session  # include the flask library
import locale
import json
import os
from os import listdir
from os.path import isfile, join
# to install this package run pip (or pip3) install Flask-Mail
from flask_mail import Mail, Message
import os
app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("FROM_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app_language = 'ru_RU'

@app.route('/')
def main_page():
    return render_template('portfolio.html', translations=languages.get(app_language))
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', translations=languages.get(app_language))

@app.route('/ecucation_categories')
def education_categories():
    return render_template('education.html', translations=languages.get(app_language))

@app.route('/languages_categoties')
def languages_categories():
    return render_template('languages.html', translations=languages.get(app_language))

@app.route('/workingexperience_categories')
def workingexperience_categories():
    return render_template('workingexperience.html', translations=languages.get(app_language))

@app.route('/interests_categories')
def interest_categories():
    return render_template('interests.html', translations=languages.get(app_language))

@app.route('/contact_form')
def contact():
    return render_template('contact_form.html', translations=languages.get(app_language))

@app.route('/send-test-email')
def index():
    msg = Message('Hello', sender='08gulnazik08@gmail.com', recipients=['shakirova.gul2015@yandex.ru', os.getenv("FROM_EMAIL")])
    msg.body = "This is the email body"
    mail.send(msg)
    print(msg)
    return "Sent"

@app.route('/send-email', methods = ['POST'])
def send_email():

    msg = Message( languages.get(app_language).get('letter_hello') + request.form['lastname'] + ' ' + request.form['firstname'], sender=os.getenv("FROM_EMAIL"),
                  recipients=[request.form['email']])
    msg.body = languages.get(app_language).get('letter_subject')
    mail.send(msg)
    print(msg)

    msg = Message('Новое сообщение с твоего сайта', sender=os.getenv("FROM_EMAIL"),
                  recipients=['shakirova.gul2015@yandex.ru'])
    msg.body = 'Вам написал ' + request.form['email'] + '\n' + request.form['subject']
    mail.send(msg)
    print(msg)

    return render_template('portfolio.html', translations=languages.get(app_language))

@app.route('/set_lang', methods = ['POST'])
def dummy_function():
    global app_language
    lang = request.form['lang']
    path = request.form['path']
    if lang == 'en':
        app_language = 'en_EN'
        return render_template(path+'.html', translations=languages.get(app_language))
    elif lang == 'ru':
        app_language = 'ru_RU'
        return render_template(path+'.html', translations=languages.get(app_language))
    else:
        app_language = 'es_ES'
        return render_template(path+'.html', translations=languages.get(app_language))

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, app_language)
    languages = {}
    language_list = [f for f in listdir(os.path.join(".", 'language')) if
                     isfile(join(os.path.join(".", 'language'), f))]
    for lang in language_list:
        lang_code = lang.split('.')[0]
        with open(os.path.join(".", 'language', lang), 'r', encoding='utf8') as file:
            languages[lang_code] = json.loads(file.read())

    app.run(host="0.0.0.0", port=8080, debug=True)  # application will start listening for web request on port 5000