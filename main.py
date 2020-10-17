from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home, Page!</h1>"


@app.route("/<page>/")
def user(page):
    return f"This is {page}!"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", page='Not Admin!'))


if __name__ == '__main__':
    app.run()
