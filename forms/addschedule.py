from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddScheduleForm(FlaskForm):
    grade = StringField('grade', validators=[DataRequired()])
    week_number = IntegerField('week_number', validators=[DataRequired()])
    monday = StringField('monday', validators=[DataRequired()])
    tuesday = StringField('tuesday', validators=[DataRequired()])
    wednesday = StringField('wednesday', validators=[DataRequired()])
    thursday = StringField('thursday', validators=[DataRequired()])
    friday = StringField('friday', validators=[DataRequired()])
    saturday = StringField('saturday', validators=[DataRequired()])
    sunday = StringField('sunday', validators=[DataRequired()])

    submit = SubmitField('Submit')