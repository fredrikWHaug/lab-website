import logging
from flask import Flask, request
from flask_cors import CORS
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Setup CORS configuration (adjust based on environment)
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:5000", "http://localhost:5000"],  # Allow local testing
            "methods": ["GET", "POST", "PUT", "DELETE"],  # Allowed HTTP methods
            "allow_headers": ["Content-Type", "Authorization"],  # Allowed headers
            "supports_credentials": True  # Allow credentials
        }
    })

    # Initialize Talisman with security settings
    talisman = Talisman(
        app,
        content_security_policy={
            'default-src': "'self'",
            'script-src': "'self' 'unsafe-inline'",
            'style-src': "'self' 'unsafe-inline'"
        },
        strict_transport_security=True,  # Enforce HTTPS
        frame_options="DENY"  # Prevent clickjacking
    )

    # Add additional headers for enhanced security
    @app.after_request
    def set_additional_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevent MIME sniffing
        response.headers['Cache-Control'] = 'no-store'  # Prevent caching
        return response

    # Setup logging
    logging.basicConfig(
        filename='app.log',  # Log file
        level=logging.INFO,  # Log level
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Log request information before processing
    @app.before_request
    def log_request_info():
        logging.info(f'Request: {request.method} {request.url}')
        logging.info(f'Headers: {request.headers}')
        logging.info(f'Body: {request.get_data()}')

    # Register routes
    from .routes import api
    app.register_blueprint(api)

    return app
