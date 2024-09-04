import datetime
import logging
import os

from flask import Flask
from flask_cors import CORS
# from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from .config import config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

# database related
app.config['DB_NAME'] = os.environ.get('DB_NAME')
# app.config.from_object(config[os.environ.get('CONFIG_MODE')])
app.config.from_object(config['development'])
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "postgresql+psycopg2://" + os.environ['DB_USER'] + ":"
    + os.environ['DB_PASSWORD'] + "@"
    + os.environ['DB_HOST']
    + ":"
    + os.environ['DB_PORT'] + "/"
    + os.environ['DB_NAME']
    )

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

# JWT_ACCESS_TOKEN_TIMEDELTA = datetime.timedelta(minutes=20)
# JWT_REFRESH_TOKEN_TIMEDELTA = datetime.timedelta(hours=6)

# app_jwt = JWTManager(app)

api = Api(app)

CORS(app)

# BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME')
#
# bucket_client = boto3.client('s3', aws_access_key_id=os.environ['S3_BUCKET_KEY'],
#                              aws_secret_access_key=os.environ['S3_BUCKET_SECRET_ACCESS_KEY'])
