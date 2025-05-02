from flask import Flask
from app.config import settings
from app.routes import bp
from app.utils.logging import configure_logging

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Configure logging
    configure_logging(app)
    
    # Register blueprints
    app.register_blueprint(bp)
    
    return app