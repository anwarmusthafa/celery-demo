from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab,timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryapp.settings')

app = Celery('celeryapp')

# Use a string here to avoid importing the Django settings file directly.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat settings
app.conf.beat_schedule = {
    # Task to run at 2:49 AM daily
    'send-mail-every-day-2-49-am': {
        'task': 'send_mail.tasks.send_mail_function',
        'schedule': crontab(hour=1, minute=35),
    },
     # Task to run every 15 minutes
    'send-mail-every-15-minutes': {
        'task': 'send_mail.tasks.send_mail_function',
        'schedule': timedelta(minutes=15),  # Runs every 15 minutes
    },
}

# Discover tasks in installed apps automatically.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
