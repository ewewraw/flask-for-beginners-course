from flask import Flask, render_template, redirect, url_for, request  # include the flask library
import locale
import json
import os
from os import listdir
from os.path import isfile, join
# to install this package run pip (or pip3) install Flask-Mail
from flask_mail import Mail, Message
import locale
import json
from os import listdir
from os.path import isfile, join
from flask_mail import Mail, Message
import os

app = Flask(__name__)

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

app_language = 'ru_RU'

@app.route('/portfolio')
def main_page():
    #app_language
    # TODO
    # Look at the translations argument. How does it look like?
    # What kind of object is that? What is inside?
    # Maybe you can print it and have a look?
    # TODO: Main task: 1) make everything translatable 2) add another language (any)
    return render_template('portfolio.html', translations=languages.get(app_language))

@app.route('/dummy_function', methods = ['POST'])
def dummy_function():
    global app_language
    # TODO
    # what is this weird function?
    lang = request.form['lang']
    print('Oh myyyy')
    print(lang)
    print("button clicked")
    if lang == 'en':
        app_language = 'en_EN'
        return render_template('portfolio.html', translations=languages.get(app_language))
    elif lang == 'ru':
        app_language = 'ru_RU'
        return render_template('portfolio.html', translations=languages.get(app_language))
    else:
        app_language = 'ch_CH'
        return render_template('portfolio.html', translations=languages.get(app_language))
@app.route('/volunteering_activity')
def volunteering_activity():
    return render_template('volunteering_activity.html', translations=languages.get(app_language))
@app.route('/education')
def education():
    return render_template('education.html', translations=languages.get(app_language))

@app.route('/information')
def information():
    return render_template('information.html', translations=languages.get(app_language))

@app.route('/working_experience')
def working_experience():
    return render_template('working_experience.html', translations=languages.get(app_language))

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', translations=languages.get(app_language))

@app.route("/send-test-email", methods = ['POST'])
def index():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    message = request.form['message']
    email = request.form['email']
    msg = Message('New email from' + ' ' + firstname + ' ' + lastname, sender=request.form['email'], recipients=['0708anastasiya99@gmail.com'])
    msg.body = request.form['message']
    mail.send(msg)
    msg1 = Message('Dear,' + ' ' + firstname + ' ' + ', ' + 'your message is sent!', sender='0708anastasiya99@gmail.com', recipients=[request.form['email']])
    mail.send(msg1)
    return "Your message is sent!"

def get_stats(input):
    return locale.format_string('%d', input)


def get_currencies(input):
    return locale.currency(input, international=True)

if __name__ == '__main__':
    app_language = 'ru_RU'
    locale.setlocale(locale.LC_ALL, app_language)
    languages = {}
    # TODO: so we just took all the files that are in the language directory? Hmm..
    language_list = [f for f in listdir(os.path.join(".", 'language')) if isfile(join(os.path.join(".", 'language'), f))]
    # ["en_EN.json", "ru_RU.json"]
    # TODO: And for each file... ?
    for lang in language_list:
        # TODO: we extract the language code from the file name...
        lang_code = lang.split('.')[0]
        # TODO: and look inside the file
        with open(os.path.join(".", 'language', lang), 'r', encoding='utf8') as file:
            # TODO: and for our languages array we add the content of each file under the language code. Hmm...
            languages[lang_code] = json.loads(file.read())
    # TODO: So, how will the languages array look like in the end? Let's try to print it and see the console logs...

    app.run(host="0.0.0.0", port=8080, debug=True)  # application will start listening for web request on port 5000

