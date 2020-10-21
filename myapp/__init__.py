from flask import Flask
from myapp.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    from myapp.home.routes import Home


    app.register_blueprint(Home)

    return app