from __future__ import unicode_literals, absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Celery.settings')

app = Celery('Django_Celery')#name project
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind =True)
def debug_task(self):
    print(self.request)

app.conf.beat_schedule = {
    #Task's Name
    'Generate Report for minutes': {
        #path Task or Method
        'task': 'apps.uploadfile.task.generate_report_n',
        #Put Time
        'schedule': crontab(minute='*/1'),
    },
}


