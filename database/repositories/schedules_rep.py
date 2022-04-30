from database.manage import db_session
from database.models import Schedule


class ScheduleRepository:
    def get_schedule_by_id(self, schedule_id):
        return db_session.query(Schedule).get(schedule_id)

    def save_schedule(self, schedule_obj):
        db_session.add(schedule_obj)
        db_session.commit()


schedule_rep = ScheduleRepository()