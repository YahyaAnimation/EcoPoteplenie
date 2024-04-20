from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main2')
def main2():
    return render_template("main2.html")


@app.route('/choice')
def choice():
    return render_template("choice.html")


@app.route('/yes')
def yes():
    return render_template("yes.html")


@app.route('/no')
def no():
    return render_template("no.html")


if __name__ == '__main__':
    app.run()