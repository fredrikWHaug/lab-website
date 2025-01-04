from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    CORS(app)
    Talisman(app)  # Enforce secure headers

    from .routes import api
    app.register_blueprint(api)

    return app
