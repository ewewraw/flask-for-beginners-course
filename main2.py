from flask import Flask, render_template, request
import locale
import json
from os import listdir
from os.path import isfile, join
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("FROM_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
app_language = 'ru_RU'

main_path = os.getenv("PROJECT_PATH")
print(os.getenv("PROJECT_PATH"))

locale.setlocale(locale.LC_ALL, app_language)
languages = {}
language_list = [f for f in listdir(os.path.join(main_path, 'language')) if
                 isfile(join(os.path.join(main_path, 'language'), f))]
for lang in language_list:
    lang_code = lang.split('.')[0]
    with open(os.path.join(main_path, 'language', lang), 'r', encoding='utf8') as file:
        languages[lang_code] = json.loads(file.read())

@app.route('/')
def main_page():
    return render_template('portfolio.html', translations=languages.get(app_language))

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', translations=languages.get(app_language))

@app.route('/education_categories')
def education_categories():
    return render_template('education.html', translations=languages.get(app_language))

@app.route('/languages_categories')
def languages_categories():
    return render_template('languages.html', translations=languages.get(app_language))

@app.route('/workingexperience_categories')
def workingexperience_categories():
    return render_template('working_experience.html', translations=languages.get(app_language))

@app.route('/interests_categories')
def interests_categories():
    return render_template('interests.html', translations=languages.get(app_language))

@app.route('/hobbies')
def hobbies_categories():
    return render_template('hobbies.html', translations=languages.get(app_language))

@app.route('/pets')
def pets_categories():
    return render_template('pets.html', translations=languages.get(app_language))

@app.route('/certificates')
def certificates_categories():
    return render_template('certificates.html', translations=languages.get(app_language))

@app.route('/contact_form')
def contact():
    return render_template('contact_form.html', translations=languages.get(app_language))

@app.route('/send-email', methods=['POST'])
def send_email():
    success = True
    try:
        msg = Message(languages.get(app_language).get('letter_hello') + request.form['lastname'] + ' ' + request.form[
            'firstname'],
                      sender=os.getenv("FROM_EMAIL"), recipients=[request.form['email']])
        msg.body = languages.get(app_language).get('letter_subject')
        mail.send(msg)

        msg = Message('Новое сообщение с твоего сайта', sender=os.getenv("FROM_EMAIL"),
                      recipients=['shakirova.gul2015@yandex.ru'])
        msg.body = 'Вам написал ' + request.form['lastname'] + ' ' + request.form['firstname'] + ' ' \
                   + request.form['email'] + '\n' + request.form['subject']
        mail.send(msg)
    except:
        print('Неуспешная попытка отправки писем')
        success = False

    if (success):
        result = languages.get(app_language).get('email_sent')
    else:
        result = languages.get(app_language).get('failed_email_send')

    return render_template('portfolio.html', translations=languages.get(app_language), emailSentResult=result)

@app.route('/set_lang', methods=['POST'])
def dummy_function():
    global app_language
    lang = request.form['lang']
    path = request.form['path']
    if lang == 'en':
        app_language = 'en_EN'
        return render_template(path + '.html', translations=languages.get(app_language))
    elif lang == 'ru':
        app_language = 'ru_RU'
        return render_template(path + '.html', translations=languages.get(app_language))
    else:
        app_language = 'es_ES'
        return render_template(path + '.html', translations=languages.get(app_language))



if __name__ == '__main__':
    app.run(debug=True)
