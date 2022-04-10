from flask import Flask, render_template, redirect, request, abort, Blueprint, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

from database.models.jobs import Jobs
from database.models.users import User
from forms.news import JobsForm
from database.manage import db_session
from forms.user import RegisterForm, LoginForm
from database.repositories import users_rep

# from app import login_manager


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        users_rep.save_user(user, form.password.data)

        return redirect('/auth/login')
    return render_template('register.html', title='Регистрация', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users_rep.get_user_by_email(form.email.data)
        login_user(user, remember=form.remember_me.data)
        return redirect("/")
    return render_template('login.html', title='Авторизация', form=form)
