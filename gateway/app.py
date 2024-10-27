import os

from flask import Flask, jsonify, request
from flask_smorest import Api
from dotenv import load_dotenv
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    @app.route('/recommend', methods=['GET'])
    def recommend():
        data = request.json
        query = data.get("query")
        url = f'http://127.0.0.1:5001/recommend'
        response = requests.get(url, params=query)

        return response

    return app


if __name__ == '__main__':
    host = os.getenv('GATEWAY_ADDRESS')
    port = os.getenv('GATEWAY_PORT')
    debug = os.getenv('DEBUG')
    app = create_app()
    app.run(host=host, port=port, debug=debug)
