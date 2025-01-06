from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Initialize Talisman with only basic settings
    talisman = Talisman(app)

    # Add more security headers using Flask app config
    app.config['TALISMAN_CONTENT_SECURITY_POLICY'] = {
        'default-src': "'self'",
        'script-src': "'self' 'unsafe-inline'",
        'style-src': "'self' 'unsafe-inline'"
    }
    app.config['TALISMAN_STRICT_TRANSPORT_SECURITY'] = True
    app.config['TALISMAN_X_FRAME_OPTIONS'] = 'DENY'
    app.config['TALISMAN_CONTENT_TYPE_NOSNIFF'] = True
    app.config['TALISMAN_CACHE_CONTROL'] = 'no-store'

    # Register routes
    from .routes import api
    app.register_blueprint(api)

    return app
