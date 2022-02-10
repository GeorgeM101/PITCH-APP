from flask import render_template,request,redirect, url_for, flash
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from email import mail_message
from flask_login import login_user,logout_user,login_required


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Pitch-App Login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/register',methods = ["GET","POST"])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        user = User(email =register_form.email.data, username =register_form.username.data,password =register_form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)

    title = "New account"
    return render_template('auth/register.html',register_form =register_form, title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.html"))