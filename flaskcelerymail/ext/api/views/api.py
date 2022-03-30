from flask import request
from flask_cors import cross_origin
from flaskcelerymail.ext.celery.tasks.tasks import send_email


@cross_origin(supports_credentials=True)
def send_mail():
    req = request.get_json(force=True)
    send_email.delay(**req)
    return "OK"
