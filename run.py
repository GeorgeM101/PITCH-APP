from flask import Flask, render_template

from app.models import loginForm

app= Flask(__name__)


@app.route('/login')
def login():
    form = loginForm

    return render_template('login.html', form=form)

if __name__== '__main__':
    app.run(debug=True)