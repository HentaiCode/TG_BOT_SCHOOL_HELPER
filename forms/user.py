import wtforms
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField, IntegerField, FieldList
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, EqualTo
from .validators import EmailUnique, Password


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), EmailUnique(message='Такой е-мейл уже существует! ')])
    password = PasswordField('Пароль',
                             validators=[DataRequired(), EqualTo('password_again', message='Пароли не совпадают!')])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст пользователя', validators=[DataRequired()])
    position = wtforms.SelectField(label='Должность пользователя', choices=['Учитель', 'Ученик'])
    about = TextAreaField("Немного о себе")
    address = TextAreaField("Адрес")
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Password('Неправильный логин или пароль')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
