from app import create_app
from app.config import settings
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=settings.DEBUG
    )