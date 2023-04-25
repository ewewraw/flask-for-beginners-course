from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student/<name>')
def main_page(name=None, characteristics=['cool', 'nice'], photo="/static/harold.webp", gender="(s)he"):
    # Here you should complete your code
    if name == "natalia":
        gender = 'she'
        characteristics = ['god damn awsome', 'a programming tutor', 'thinking if she should do a master at TUM', "smart"]
        photo ="/static/natalia.png"
    elif name == "alex":
         gender = 'she'
         characteristics = ['happy (when she has free time)', 'bad at programming', 'mbti - infj']
         photo ="/static/alex.jpg"
    else:
        print('student 1')
        print('student 2')
        print('Ive changed smth')

    return render_template('student.html', name=name, gender=gender, characteristics=characteristics, photo=photo)

if __name__ == '__main__':
   app.run(port=5000, debug=True)
