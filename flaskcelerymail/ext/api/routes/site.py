from flaskcelerymail.ext.api.views.site import home


def init_site_routes(site):
    site.add_url_rule("/", "home", view_func=home, methods=["GET"])
