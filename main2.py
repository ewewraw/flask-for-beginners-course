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

app.config['MAIL_SERVER'] = '08gulnazik08@gmail.com'
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



@app.route('/portfolio')
def main_page():
    # TODO
    # Look at the translations argument. How does it look like?
    # What kind of object is that? What is inside?
    # Maybe you can print it and have a look?
    # TODO: Main task: 1) make everything translatable 2) add another language (any)
    return render_template('portfolio.html', translations=languages.get('en_EN'))
@app.route('/ecucation_categories')
def education_categories():
    render_template('education.html')

@app.route('/languages_categoties')
def languages_categories():
    render_template('languages.html')
@app.route('/workingexperience_categories')
def workingexperience_categories():
    render_template('workingexperience.html')
@app.route('/interests_categories')
def interest_categories():
    render_template('interest.html')
@app.route('/send-test-email')
def index():
    msg = Message('Damn it really works!, sender \'08gulnazik08@gmail.com\'', recipients = ['08gulnazik08@gmail.com'])
    msg.body = "Hey dude, sending you this email from my Flask app, lmk if it works"
    print(msg)
    mail.send (msg)
    return "Message sent"

@app.route('/')
def index():
    lang = session.get('lang', 'en')
    with open('translations.json', 'r') as f:
        translations = json.load(f)[lang]
    return render_template('index.html', translations=translations)

@app.route('/change_language', methods=['POST'])
def change_language():
    lang = request.form['lang']
    session['lang'] = lang
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/dummy_function')
def dummy_function():
    # TODO
    # what is this weird function?
    print('Oh myyyy')
    return redirect(url_for('main_page'))

@app.route('/random')
def random_page():
    return render_template('index.html')

def get_stats(input):
    return locale.format_string('%d', input)

def get_currencies(input):
    return locale.currency(input, international=True)

if __name__ == '__main__':
    app_language = 'ru_RU'
    locale.setlocale(locale.LC_ALL, app_language)
    languages = {}
    # TODO: so we just took all the files that are in the language directory? Hmm..
    language_list = glob.glob("./language/*.json")
    # TODO: And for each file... ?
    for lang in language_list:
        filename = lang.split('/')
        # TODO: we extract the language code from the file name...
        lang_code = filename[2].split('.')[0]
        # TODO: and look inside the file
        with open(lang, 'r', encoding='utf8') as file:
            # TODO: and for our languages array we add the content of each file under the language code. Hmm...
            languages[lang_code] = json.loads(file.read())
    # TODO: So, how will the languages array look like in the end? Let's try to print it and see the console logs...

    app.run(host="0.0.0.0", port=8080, debug=True)  # application will start listening for web request on port 5000