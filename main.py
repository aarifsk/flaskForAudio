from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", number=5, message="Hola!")


@app.route("/<page>/")
def user(page):
    return f"This is {page}!"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", page='Not Admin!'))


if __name__ == '__main__':
    app.run(debug=True)  # rerun on every change
