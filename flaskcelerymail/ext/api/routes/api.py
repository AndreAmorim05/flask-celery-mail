from flaskcelerymail.ext.api.views.api import send_mail


def init_api_routes(api):
    api.add_url_rule(
        "/send-mail", "mail", view_func=send_mail, methods=["POST"]
    )
