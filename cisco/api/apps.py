from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    name = 'api'

    # def ready(self):
    #     print("Starting Scheduler ............")
    #     from .nav_Schedule import nav_update_time
    #     nav_update_time.start()

    # def ready(self):
    #     if settings.SCHEDULER_DEFAULT:
    #         from cisco_name import operator
    #         operator.start()


