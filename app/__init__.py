from flask import Flask
from app.routes import main_bp
import os


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    config_path = os.path.join(app.instance_path, "config.py")
    app.config.from_pyfile(config_path, silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
