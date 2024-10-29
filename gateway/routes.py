import os
import json
import requests

from flask import Flask, jsonify, request
from flask_smorest import Blueprint
from dotenv import load_dotenv


current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

RECOMMENDER_ADDRESS = os.getenv('RECOMMENDER_ADDRESS')
RECOMMENDER_PORT = os.getenv('RECOMMENDER_PORT')

gateway_bp = Blueprint('gateway', __name__)


@gateway_bp.route('/recommendations', methods=['GET'])
def recommendations():
    query = request.json.get("query")

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    url = f"http://{RECOMMENDER_ADDRESS}:{RECOMMENDER_PORT}/recommend"
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"query": query})

    try:
        response = requests.post(url=url, headers=headers, data=data)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"error": "Failed to retrieve recommendations"}), 500

    return jsonify({"recommendations": response.json().get("answer", [])}), 200
