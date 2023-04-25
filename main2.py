from flask import Flask, render_template, redirect, url_for  # include the flask library
import locale
import glob
import json
import os
from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route('/portfolio')
def main_page():
    # TODO
    # Look at the translations argument. How does it look like?
    # What kind of object is that? What is inside?
    # Maybe you can print it and have a look?
    # TODO: Main task: 1) make everything translatable 2) add another language (any)
    return render_template('portfolio.html', translations=languages.get('en_EN'))

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
    language_list = [f for f in listdir('./language/') if isfile(join('./language/', f))]
    # TODO: And for each file... ?
    for lang in language_list:
        # TODO: we extract the language code from the file name...
        lang_code = lang.split('.')[0]
        # TODO: and look inside the file
        with open('./language/' + lang, 'r', encoding='utf8') as file:
            # TODO: and for our languages array we add the content of each file under the language code. Hmm...
            languages[lang_code] = json.loads(file.read())
    # TODO: So, how will the languages array look like in the end? Let's try to print it and see the console logs...

    app.run(host="0.0.0.0", port=8080, debug=True)  # application will start listening for web request on port 5000

