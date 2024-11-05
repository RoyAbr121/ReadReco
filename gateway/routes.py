import os
import json
from http import HTTPStatus

import requests

from flask import jsonify, request
from flask_smorest import Blueprint
from dotenv import load_dotenv
from schemas import RecommendationRequestSchema

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

RECOMMENDER_ADDRESS = os.getenv('RECOMMENDER_ADDRESS')
RECOMMENDER_PORT = os.getenv('RECOMMENDER_PORT')

if not RECOMMENDER_ADDRESS or not RECOMMENDER_PORT:
    raise ValueError("GATEWAY_ADDRESS and GATEWAY_PORT must be set.")

blueprint_gateway = Blueprint('Gateway', __name__)


@blueprint_gateway.route('/recommendations', methods=['POST'])
@blueprint_gateway.arguments(RecommendationRequestSchema)
@blueprint_gateway.response(HTTPStatus.OK, RecommendationRequestSchema)
def recommendations(user_data):
    query = user_data.get("query")
    url = f"http://{RECOMMENDER_ADDRESS}:{RECOMMENDER_PORT}/recommend"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"query": query})

    try:
        response = requests.post(url=url, headers=headers, data=data)
        response.raise_for_status()
        answer = response.json().get("answer", [])
    except requests.RequestException as e:
        return jsonify({"error": "Failed to retrieve recommendations"}), 500

    return jsonify({"answer": answer})
