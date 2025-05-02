import os
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, AnyUrl
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    # Twilio Configuration
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER: str = os.getenv("TWILIO_PHONE_NUMBER")
    
    # WebSocket Configuration
    WEBSOCKET_URL: AnyUrl = os.getenv("WEBSOCKET_URL", "wss://devapi.ivoz.ai/llm-campaigns/ws/groq/?bot=ivoz")
    STREAM_TRACK: str = os.getenv("STREAM_TRACK", "inbound_track")
    
    # Security
    VALIDATE_TWILIO_REQUESTS: bool = os.getenv("VALIDATE_TWILIO_REQUESTS", "true").lower() == "true"
    
    # Application
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()