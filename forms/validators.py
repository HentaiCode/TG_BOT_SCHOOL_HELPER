from wtforms import ValidationError

from database.manage import db_session
from database.models import User
from database.repositories import users_rep


class EmailUnique:
    """
    Check email unique.

    :param message:
        Error message to raise in case of a validation error. Can be
        interpolated with `%(other_label)s` and `%(other_name)s` to provide a
        more helpful error.
    """

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if users_rep.get_user_by_email(field.data):
            raise ValidationError(self.message)


class Password:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        user = users_rep.get_user_by_email(form.email.data)
        if user is None or not user.check_password(field.data):
            raise ValidationError(self.message)

        # if db_session.query(User).filter(User.email == field.data).first():
        #     raise ValidationError(self.message)
        #
        #     user = users_rep.get_user_by_email(form.email.data)
        # if user and user.check_password(form.password.data):
        #     login_user(user, remember=form.remember_me.data)
        #     return redirect("/")