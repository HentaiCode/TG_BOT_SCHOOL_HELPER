from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    title = StringField('Job title', validators=[DataRequired()])
    scope_of_work = StringField('Scope of work', validators=[DataRequired()])
    content = StringField('Project Description', validators=[DataRequired()])
    team_leader_name = StringField('Team Leader_name', validators=[DataRequired()])
    accomplices = StringField('Accomplices', validators=[DataRequired()])
    work_size = StringField('Work Size', validators=[DataRequired()])
    is_finished = BooleanField('is job finished?')

    submit = SubmitField('Submit')
