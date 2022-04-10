from database.manage import db_session
from database.models import User


class UsersRepository:
    def get_user_by_id(self, user_id):
        return db_session.query(User).get(user_id)
        # users = self.session.query(User).all()

    def get_user_by_email(self, user_email):
        return db_session.query(User).filter(User.email == user_email).first()

    def save_user(self, user_obj, password):
        user_obj.set_password(password)
        db_session.add(user_obj)
        db_session.commit()


users_rep = UsersRepository()
