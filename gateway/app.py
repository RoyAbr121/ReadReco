import json
import os

from flask import Flask, jsonify, request
from flask_smorest import Api
from dotenv import load_dotenv
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

RECOMMENDER_ADDRESS = os.getenv('RECOMMENDER_ADDRESS')
RECOMMENDER_PORT = os.getenv('RECOMMENDER_PORT')

if not RECOMMENDER_ADDRESS or not RECOMMENDER_PORT:
    raise ValueError('RECOMMENDER_ADDRESS and RECOMMENDER_PORT must be set')


class Config:
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Gateway Service REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    return app


if __name__ == '__main__':
    host = os.getenv('GATEWAY_ADDRESS')
    port = os.getenv('GATEWAY_PORT')
    debug = os.getenv('DEBUG')
    app = create_app()
    app.run(host=host, port=port, debug=debug)
