import datetime
import logging
import traceback

from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource

from wiz_server import app, api
from wiz_server.common.constants import (
    API_STATUS_SUCCESS, API_STATUS_FAILURE, API_STATUS_ERROR, DEFAULT_PAGE, DEFAULT_PER_PAGE
)
from wiz_server.core.controller import create_user_controller

core_blueprint = Blueprint('core', __name__)

logger = logging.getLogger(__name__)


class Ping(Resource):
    def get(self):
        return jsonify({"message": "pong"})
    

class Users(Resource):
    def post(self):
        try:
            name = request.json.get('name')
            username = request.json.get('username')
            email = request.json.get('email')
            password = request.json.get('password')
            result = create_user_controller(email=email, username=username, name=name, password=password)
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'user': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))


api.add_resource(Ping, '/ping')
api.add_resource(Users, '/users')
