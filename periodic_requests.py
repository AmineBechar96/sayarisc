import requests
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from twisted.internet import reactor


def send_request():
    
    requests.post("https://scrapya.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })
    
 def send_request2():
    
    requests.post("https://scrapya.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })

if __name__ == '__main__':
        scheduler = BlockingScheduler(timezone="Africa/Lagos")
        scheduler2 = BlockingScheduler(timezone="Africa/Lagos")
        scheduler.add_job(send_request,'cron', hour = '18', minute = '03')
        scheduler2.add_job(send_request2,'cron', hour = '18', minute = '04')
        scheduler.start()
        scheduler2.start()
        reactor.run()
