from database.manage import db_session
from database.models import Jobs


class JobsRepository:
    def get_job_by_id(self, job_id):
        return db_session.query(Jobs).get(job_id)

    def save_job(self, job_obj):
        db_session.add(job_obj)
        db_session.commit()


jobs_rep = JobsRepository()
