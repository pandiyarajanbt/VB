from twilio.request_validator import RequestValidator
from flask import request
from app.config import settings
from typing import Dict

class ValidationService:
    @staticmethod
    def validate_twilio_request() -> bool:
        """
        Validates incoming Twilio request using X-Twilio-Signature
        """
        if not settings.VALIDATE_TWILIO_REQUESTS:
            return True
            
        validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)
        
        # Get request URL without query parameters if present
        url = request.url
        if '?' in url:
            url = url.split('?')[0]
        
        # Get POST parameters
        post_params = {}
        for key in request.form.keys():
            post_params[key] = request.form.get(key)
        
        # Get X-Twilio-Signature header
        signature = request.headers.get('X-Twilio-Signature', '')
        
        return validator.validate(url, post_params, signature)