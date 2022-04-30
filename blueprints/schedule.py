from flask import Blueprint, render_template
from werkzeug.utils import redirect

from forms.addschedule import AddScheduleForm
from database.models.schedule import Schedule
from database.repositories import schedule_rep
from flask_login import current_user

bp = Blueprint('schedule', __name__)


@bp.route('/addschedule', methods=['GET', 'POST'])
def addschedule():
    form = AddScheduleForm()
    if current_user.__dict__:

        if current_user.position == 'Учитель':

            if form.validate_on_submit():
                schedule = Schedule()
                form.populate_obj(schedule)
                schedule_rep.save_schedule(schedule)
                return redirect('/')

            return render_template('addshedule.html', title='Добавление расписания', form=form)

    return {"error": "Access denied"}
