from celery import Celery
from .config_essentials import request_url

def make_celery(app_name = __name__):
    backend = request_url
    broker = backend.replace("0", "1")
    return Celery(app_name, backend=backend, broker=broker)

celery = make_celery()