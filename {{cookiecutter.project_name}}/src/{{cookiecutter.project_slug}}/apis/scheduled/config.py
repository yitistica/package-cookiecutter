from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

SCHEDULER_TRACKING_URI = f"sqlite:///jobs.sqlite"

job_stores = {"default": SQLAlchemyJobStore(url=SCHEDULER_TRACKING_URI)}
executors = {'default': ProcessPoolExecutor(max_workers=1)}

job_defaults = {'coalesce': True,
                'max_instances': 1,
                'misfire_grace_time': 60}


scheduler = BackgroundScheduler(jobstores=job_stores,
                                executors=executors,
                                job_defaults=job_defaults)
