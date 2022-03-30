from collections import namedtuple

from flask import render_template
from flask_mail import Message

from . import mail


def email_formater(subject, recipients, body=None, html=None, charset="utf-8"):
    Email = namedtuple("Email", "subject recipients body html charset")
    email = Email(subject, recipients, body, html, charset)
    return email._asdict()


def send_email(
    company: str,
    address: str,
    emails: list,
    subject: str = "AVISO - Preditivo",
    preheader: str = "Alerta de mal funcionamento",
):
    html = render_template(
        "emails/warning.html",
        preheader=preheader,
        company=company,
        address=address,
    )

    for contact in emails:
        msg = email_formater(subject, [contact], html=html)
        email = Message(**msg)
        mail.send(email)
