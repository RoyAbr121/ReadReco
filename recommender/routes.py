import os

from flask import jsonify, request
from flask_smorest import Blueprint
from recommender import rag_chain
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

GATEWAY_ADDRESS = os.getenv('GATEWAY_ADDRESS')
GATEWAY_PORT = os.getenv('GATEWAY_PORT')

if not GATEWAY_ADDRESS or not GATEWAY_PORT:
    raise ValueError("GATEWAY_ADDRESS and GATEWAY_PORT must be set.")

chat_history = []
recommender_bp = Blueprint('recommender', __name__)


@recommender_bp.route('/recommend', methods=['POST'])
def recommend():
    query = request.json.get("query")
    output = rag_chain.invoke({"input": query, "chat_history": chat_history})
    answer = output.get("answer", [])

    return jsonify({"answer": answer}), 200
