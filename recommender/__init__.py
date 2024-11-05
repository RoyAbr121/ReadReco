from flask import Flask
from routes import blueprint_recommender


class Config:
    PROPAGATE_EXCEPTIONS = True
    API_TITLE = "Recommender Service REST API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint_recommender)
