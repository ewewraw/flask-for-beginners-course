from flask import Flask, render_template # include the flask library

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('portfolio.html')

if __name__ == '__main__':
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000