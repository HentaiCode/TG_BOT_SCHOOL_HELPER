from flask import Blueprint, render_template
from werkzeug.utils import redirect

from forms.addjob import AddJobForm
from database.models.jobs import Jobs as Job
from database.repositories import jobs_rep
from flask_login import current_user

bp = Blueprint('jobs', __name__)


@bp.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = AddJobForm()
    if current_user.__dict__:
        if current_user.position == 'Учитель':
            if form.validate_on_submit():
                job = Job()
                form.populate_obj(job)
                jobs_rep.save_job(job)

                return redirect('/')
            return render_template('addjob.html', title='Добавление работы', form=form)
    return {"error": "Access denied"}
