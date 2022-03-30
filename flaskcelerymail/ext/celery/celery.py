from celery import Celery

celery = Celery("flaskcelerymail", include=[])
celery.autodiscover_tasks(["flaskcelerymail.ext.celery.tasks"], force=True)


@celery.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
