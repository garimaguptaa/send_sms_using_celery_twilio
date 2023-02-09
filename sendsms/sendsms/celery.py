import os
from django.conf import settings
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendsms.settings')

app = Celery('sendsms')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind = True)
def debug_task(self):
    print("Hello from celery!")

@app.task
def print_hello():
    print("Hello")

app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'add-every-2-hour' :{
        'task' : 'send_notification',
        'schedule' : crontab(minute = '*/1')
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')