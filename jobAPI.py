import sqlite3
from job import Job

class JobAPI:
    conn = sqlite3.connect('job.db')
    c = conn.cursor()

    def __init__(self) -> None:
        self.conn
        # self.c.execute("""create table Job(
        #     job_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        #     description text)""")
        self.conn.commit()    
    def create_job(self,job:Job):
        self.c.execute("insert into Job(description) values(?)",(job.get_description(),))
        self.conn.commit()

    def read_job(self):
        with self.conn:
             return (self.c.execute("""select * from Job """))
    
    def update_job(self,job:Job):
        with self.conn:
            self.c.execute("""update Job set job_id = :job_id , description = :description
                           where job_id = :job_id""",{'job_id':job.get_Job_id() , 'description': job.get_description()}) 

    def delete_jop(self,job_id):
        with self.conn:
            self.c.execute("""delete from Job 
            where job_id = :job_id""",{'job_id': job_id})

job = JobAPI()