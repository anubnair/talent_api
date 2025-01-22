from flask import Flask

def create_app():
    app = Flask(__name__)
    # Do not initialize db here anymore
    from app import views
    app.register_blueprint(views.bp)

    return app