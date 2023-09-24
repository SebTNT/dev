from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Saying hi to another request!")
    return "<p>Hello, World!</p>"