from flask import Blueprint, request, Response
from app.services.twilio_service import TwilioService
from app.services.validation_service import ValidationService
import logging

logger = logging.getLogger(__name__)


bp = Blueprint('routes', __name__)

@bp.route('/voice-webhook', methods=['POST'])
def voice_webhook():
    """
    Handles incoming Twilio voice calls and streams to WebSocket
    """
    try:
        # Validate request if enabled
        if not ValidationService.validate_twilio_request():
            logger.warning("Invalid Twilio request signature")
            return Response("Invalid request signature", status=403)
        
        # Get call details
        call_sid = request.form.get('CallSid')
        logger.info(f"Incoming call from {request.form.get('From')}, CallSid: {call_sid}")
        
        # Generate TwiML response
        twiml = TwilioService.generate_twiml_response(call_sid)
        
        logger.debug(f"Generated TwiML: {twiml}")
        return Response(twiml, mimetype='application/xml')
        
    except Exception as e:
        logger.error(f"Error processing voice webhook: {str(e)}", exc_info=True)
        return Response("Server error", status=500)