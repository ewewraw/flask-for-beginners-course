from flask import Flask, render_template # include the flask library

app = Flask(__name__)

@app.route('/portfolio')
def main_page():
    return render_template('portfolio.html')


@app.route('/random')
def random_page():
    return render_template('index.html')

@app.route("/education")
def education():
    return render_template('education.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True) # application will start listening for web request on port 5000