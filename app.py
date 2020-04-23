from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    f = open("urls.txt", "r", encoding="utf-8")
    urls = [row for row in f]
    f.close()
    return render_template("index.html", urls=urls)


@app.route("/add")
def add():
    return render_template("form.html")


@app.route("/receiver", methods=["POST"])
def receiver():
    url = request.form.get("url")
    f = open("urls.txt", "a+", encoding="utf-8")
    f.write("\n" + url )
    sources = [row for row in f if row]
    f.close()
    return render_template("index.html", url=sources)      