from twilio.request_validator import RequestValidator
from flask import request
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class ValidationService:
    @staticmethod
    def validate_twilio_request() -> bool:
        if not settings.VALIDATE_TWILIO_REQUESTS:
            return True  # Skip if validation is disabled
        
        auth_token = settings.TWILIO_AUTH_TOKEN
        if not auth_token:
            logger.error("Twilio Auth Token missing!")
            return False

        validator = RequestValidator(auth_token)
        signature = request.headers.get('X-Twilio-Signature', '')
        url = request.url  # Get the full URL (including query params if any)
        form_data = request.form.to_dict()  # Get all form data

        # Debug logs (remove in production)
        logger.debug(f"Validating Twilio request | URL: {url} | Signature: {signature}")
        
        return validator.validate(url, form_data, signature)