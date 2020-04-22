from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("form.html")

@app.route("/receiver", methods=["POST"])
def receiver():
    url = request.form.get("url")
    print(url)
    return render_template("index.html")   