from flask import Flask

app = Flask(__name__)

@app.route('/') # http://www.google.com/ homepage of the appliation what is after the "/" in this case
def home():
    return "Hello, world!"

app.run(port=5000)
