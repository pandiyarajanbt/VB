import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from app.config import settings
import os

def configure_logging(app: Flask):
    """Configure application logging"""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Set log level
    log_level = getattr(logging, settings.LOG_LEVEL.upper())
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        'logs/twilio_voice_bot.log',
        maxBytes=1024 * 1024 * 10,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(log_level)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Configure app logger
    app.logger.setLevel(log_level)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    
    # Remove default Flask handler
    app.logger.removeHandler(app.logger.handlers[0])
    
    # Set logger for other modules
    logging.basicConfig(
        level=log_level,
        handlers=[file_handler, console_handler]
    )
    
    app.logger.info('Logging configured')