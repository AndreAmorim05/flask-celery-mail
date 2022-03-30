from flaskcelerymail.app import create_app
from flaskcelerymail.ext.celery import init_celery

celery = init_celery(create_app())
