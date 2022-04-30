import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from database.manage import SqlAlchemyBase


class Schedule(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'schedule'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    grade = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    week_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    monday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tuesday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    wednesday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    thursday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    friday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    saturday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sunday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
