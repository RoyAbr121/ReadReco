import os

from flask import Flask, jsonify, request
from flask_smorest import Api
from dotenv import load_dotenv
import requests

from recommender import rag_chain

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

GATEWAY_ADDRESS = os.getenv('GATEWAY_ADDRESS')
GATEWAY_PORT = os.getenv('GATEWAY_PORT')
rag_chain = rag_chain
chat_history = []


class Config:
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Recommender Service REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/recommend', methods=['POST'])
    def recommend():
        query = request.json.get("query")
        output = rag_chain.invoke({"input": query, "chat_history": chat_history})
        answer = output.get("answer", [])

        return jsonify({"answer": answer}), 200

    return app


if __name__ == '__main__':
    host = os.getenv('RECOMMENDER_ADDRESS')
    port = os.getenv('RECOMMENDER_PORT')
    debug = os.getenv('DEBUG')

    app = create_app()
    app.run(host=host, port=port, debug=debug)
