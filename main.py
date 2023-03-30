from flask import Flask # include the flask library

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello, jkdsjfs fdgkljdfklsgj ljflkgj!"

@app.route("/kpfu")
def hello_kpfu():
   return "Hello, students from KPFU"

@app.route("/kpfu-top")
def hello_kpfu_2():
   return "Hello, students from KPFU fjdksfgjksdj"

if __name__ == '__main__':
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000