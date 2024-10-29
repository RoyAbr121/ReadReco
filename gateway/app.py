import os

from flask import Flask
from dotenv import load_dotenv
from routes import gateway_bp

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)


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
    app.register_blueprint(gateway_bp)

    return app


if __name__ == '__main__':
    host = os.getenv('GATEWAY_ADDRESS')
    port = os.getenv('GATEWAY_PORT')
    debug = os.getenv('DEBUG')
    app = create_app()
    app.run(host=host, port=port, debug=debug)
