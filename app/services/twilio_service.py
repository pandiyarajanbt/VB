from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from app.config import settings
from typing import Dict, Optional

class TwilioService:
    @staticmethod
    def generate_twiml_response(call_sid: Optional[str] = None) -> str:
        """
        Generates TwiML response to connect call to WebSocket
        """
        response = VoiceResponse()
        connect = Connect()
        
        # Configure stream with WebSocket URL
        stream = Stream(
            url=str(settings.WEBSOCKET_URL),
            track=settings.STREAM_TRACK
        )
        
        # Add optional parameters if needed
        if call_sid:
            stream.parameter(name="callSid", value=call_sid)
        
        connect.append(stream)
        response.append(connect)
        
        # Fallback instructions if stream fails
        response.say("We're connecting you to our voice assistant.")
        
        return str(response)