from __future__ import absolute_import

from celery import Celery

# app = Celery('proj',
#              broker='amqp://',
#              backend='amqp://',
#              include=['proj.tasks'])

# instantiate Celery object
app = Celery(
                include=['proj.tasks'])

# Optional configuration, see the application user guide.

# import celery config file
app.config_from_object('proj.celeryconfig')

if __name__ == '__main__':
    app.start()

