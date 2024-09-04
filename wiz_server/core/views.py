import datetime
import logging
import traceback

from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource

from wiz_server import app, api
from wiz_server.common.constants import (
    API_STATUS_SUCCESS, API_STATUS_FAILURE, API_STATUS_ERROR, DEFAULT_PAGE, DEFAULT_PER_PAGE
)
from wiz_server.core.controller import (
    create_user_controller, create_category_controller, create_journal_controller, create_paper_controller,
    read_category_controller, read_journal_controller, read_paper_controller
)

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
            result = create_user_controller(
                email=email, username=username, name=name, password=password)
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'user': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))


class Papers(Resource):
    def post(self):
        try:
            title = request.json.get('title')
            abstract = request.json.get('abstract')
            publication_year = request.json.get('publication_year')
            journal = request.json.get('journal')
            category = request.json.get('category')
            doi = request.json.get('doi')
            authors = request.json.get('authors')
            citation_count = request.json.get('citation_count')
            tags = request.json.get('tags')
            result = create_paper_controller(
                title=title, abstract=abstract, publication_year=publication_year, journal=journal,
                category=category, doi=doi, authors=authors, citation_count=citation_count, tags=tags
            )
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))
        
    def get(self):
        try:
            title = request.params.get('title')
            result = read_paper_controller()
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))


class Journal(Resource):
    def post(self):
        try:
            name = request.json.get('name')
            impact_factor = request.json.get('impact_factor')
            result = create_journal_controller(
                name=name, impact_factor=impact_factor
            )
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))
        
    def get(self):
        try:
            name = request.params.get('name')
            result = read_journal_controller()
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))


class Category(Resource):
    def post(self):
        try:
            name = request.json.get('name')
            description = request.json.get('description')
            result = create_category_controller(
                name=name, description=description
            )
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))
        
    def get(self):
        try:
            name = request.params.get('name')
            result = read_category_controller()
            if result:
                return make_response(jsonify({'status': API_STATUS_SUCCESS, 'result': result}))
            else:
                return make_response(jsonify({'status': API_STATUS_FAILURE, 'result': result}))
        except Exception as e:
            app.logger.error(e)
            app.logger.debug(traceback.format_exc())
            return make_response(jsonify({'status': API_STATUS_ERROR}))


api.add_resource(Ping, '/ping')
api.add_resource(Users, '/users')
api.add_resource(Papers, '/papers')
api.add_resource(Journal, '/journal')
api.add_resource(Category, '/category')
