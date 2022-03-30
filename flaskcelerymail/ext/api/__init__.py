from .blueprints import apibp, site
from .routes.api import init_api_routes
from .routes.site import init_site_routes


def init_app(app):
    init_site_routes(site)
    init_api_routes(apibp)

    app.register_blueprint(site)
    app.register_blueprint(apibp)
