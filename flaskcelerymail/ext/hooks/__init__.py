def init_app(app):
    @app.before_first_request
    def init_everything():
        print("Isto roda sempre antes do primeiro request!!")

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        response.headers.add(
            "Access-Control-Expose-Headers",
            "Content-Type,Content-Length,Authorization,X-Pagination",
        )
        return response
