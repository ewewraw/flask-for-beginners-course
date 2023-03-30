from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student/<name>')
def main_page(name=None, characteristics=['cool', 'nice'], photo="/static/harold.webp", gender="(s)he"):
    # Here you should complete your code
    if name == "natalia":
        gender = 'she'
        characteristics = ['god damn awsome', 'a programming tutor', 'thinking if she should do a master at TUM']
        photo ="/static/natalia.png"
    else:
        print('here you should add info about you')

    return render_template('student.html', name=name, gender=gender, characteristics=characteristics, photo=photo)

if __name__ == '__main__':
   app.run(port=5000, debug=True)