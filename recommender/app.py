import os

from flask import Flask
from flask_smorest import Api
from dotenv import load_dotenv


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)

    return app


if __name__ == '__main__':
    app = create_app()

    host = os.getenv('GATEWAY_ADDRESS')
    port = os.getenv('GATEWAY_PORT')
    debug = os.getenv('DEBUG')

    app.run(host=host, port=port, debug=debug)
