# config file for Celery Daemon
from __future__ import absolute_import
from celery.schedules import crontab
# from proj import tasks
import proj
CELERY_IMPORTS = ('proj.tasks', )
# default RabbitMQ broker
BROKER_URL = 'amqp://'

# default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'

# TimeZone, this should be changed
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERY_TASK_RESULT_EXPIRES = 300 #time in seconds.

CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'proj.tasks.add',
        'schedule': crontab(minute='*'),
        'args': (1,2),
    },
}
