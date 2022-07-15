# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import register_events, DjangoJobStore
# from api.views import GetSavantName


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
#     register_events(scheduler)

#     @scheduler.scheduled_job('interval', minutes=5, name='auto_hello')
#     def auto_hello():
#         GetSavantName.get()

#     scheduler.start()
