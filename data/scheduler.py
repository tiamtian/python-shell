import time
from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5, id='123')
sched.add_job(my_job, 'cron', day_of_week='1-5', hour=6, minute=30)
print(sched.get_jobs())
sched.start()