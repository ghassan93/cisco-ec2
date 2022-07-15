from apscheduler.schedulers.background import BackgroundScheduler
from api.views import GetSavantName

def start():
    scheduler = BackgroundScheduler()
    nav = GetSavantName()
    scheduler.add_job(nav.get, "interval", minutes=2,replace_existing=True)
    scheduler.start()