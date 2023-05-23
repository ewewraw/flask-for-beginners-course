from flask import Flask # include the flask library

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello, jkdsjfs fdgkljdfklsgj ljflkgj!"

@app.route("/kpfu")
def hello_kpfu():
   return "Hello, ppl from KPFU"

@app.route("/kpfu-top")
def hello_kpfu_2():
   return "Hello everyone, students from KPFU fjdksfgjksdj"

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080, debug=True) # application will start listening for web request on port 5000