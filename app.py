from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

from database.manage import init_db
from blueprints import auth, pages
from database.manage import db_session
from database.models import User
from database.repositories import users_rep
import os

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
print()
print(SECRET_KEY)
print()

DB_PATH = 'database/blogs.db'

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(pages)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
init_db()


@login_manager.user_loader
def load_user(user_id):
    return users_rep.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run()


# TODO
# вынос логики из main.py/app.py
# blueprints
# разделение логики и переиспользование кода
# рендер форм из форм
# репозитории? еще раз про factory и db_session
# валидаторы
# переменные окружения