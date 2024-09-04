import os

from wiz_server.server import app

if __name__ == "__main__":
    app.run(port=5005, debug=True if os.environ.get('FLASK_DEBUG') == 1 else False)
