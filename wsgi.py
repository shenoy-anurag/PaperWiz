from dotenv import load_dotenv

load_dotenv('config/secrets.env')

from wiz_server.server import app


if __name__ == "__main__":
    app.run(port=5005, debug=True)
