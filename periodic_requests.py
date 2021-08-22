import requests
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
from twisted.internet import reactor
import schedule

def send_request():
    requests.post("https://guarded-temple-96501.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'ouedkniss'
    })
 def send_request2():
    requests.get("https://sayarti.herokuapp.com/")

if __name__ == '__main__':
        schedule.every().day.at("18:05").do(send_request)
        schedule.every().day.at("20:00").do(send_request)
        reactor.run()
        while (true):
            schedule.run_pending()
            time.sleep(1)
