from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello_world_str():
    return "hello world"


@app.route("/hello2")
def hello_world_str2():
    return "hello world2"
