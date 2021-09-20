import requests
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from twisted.internet import reactor


def send_request():
    requests.get("https://sayarti3.herokuapp.com/")
    requests.post("https://scrapya.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })

if __name__ == '__main__':
        scheduler = BlockingScheduler(timezone="Africa/Lagos")
        scheduler.add_job(send_request,'cron', hour = '01', minute = '11')
        scheduler.start()
        reactor.run()
