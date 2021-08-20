import requests
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from twisted.internet import reactor


def send_request():
    requests.post("https://guarded-temple-96501.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })
 def send_request2():
    requests.post("http://sayarti.herokuapp.com/")

if __name__ == '__main__':
        scheduler = BlockingScheduler(timezone="Africa/Lagos")
        scheduler.add_job(send_request,'cron', hour = '01', minute = '16')
        scheduler.add_job(send_request2,'cron', hour = '21', minute = '00')
        scheduler.start()
        reactor.run()
