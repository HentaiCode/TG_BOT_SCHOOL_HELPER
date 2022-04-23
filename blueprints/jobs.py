from flask import Blueprint, render_template
from werkzeug.utils import redirect

from forms.addjob import AddJobForm
from database.models.jobs import Jobs as Job
from database.repositories import jobs_rep

bp = Blueprint('jobs', __name__)


@bp.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = AddJobForm()
    if form.validate_on_submit():
        job = Job()
        form.populate_obj(job)
        jobs_rep.save_job(job)

        return redirect('/')
    return render_template('addjob.html', title='Добавление работы', form=form)
