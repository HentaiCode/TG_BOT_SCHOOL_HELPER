from flask import Blueprint, render_template

from database.manage import db_session
from database.models import Jobs, User

bp = Blueprint('pages', __name__)


@bp.route('/')
def index():
    jobs = db_session.query(Jobs).all()
    users = db_session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    # print(names)
    return render_template("index.html", jobs=jobs, names=names, title='Work Log')
