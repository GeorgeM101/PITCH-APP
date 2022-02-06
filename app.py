from flask import Flask,render_template , app


@app.route("/")
def index():
    return render_template('nav-bar.html')
app = Flask(__name__)
