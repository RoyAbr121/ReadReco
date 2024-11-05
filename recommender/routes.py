import os
from http import HTTPStatus

from flask import jsonify, request
from flask_smorest import Blueprint
from rag_chain import rag_chain
from dotenv import load_dotenv
from schemas import RecommendationRequestSchema

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

GATEWAY_ADDRESS = os.getenv('GATEWAY_ADDRESS')
GATEWAY_PORT = os.getenv('GATEWAY_PORT')

if not GATEWAY_ADDRESS or not GATEWAY_PORT:
    raise ValueError("GATEWAY_ADDRESS and GATEWAY_PORT must be set.")

chat_history = []
blueprint_recommender = Blueprint('Recommender', __name__)


@blueprint_recommender.route('/recommend', methods=['POST'])
@blueprint_recommender.arguments(RecommendationRequestSchema)
@blueprint_recommender.response(HTTPStatus.OK, RecommendationRequestSchema)
def recommend(user_data):
    query = user_data.get("query")
    output = rag_chain.invoke({"input": query, "chat_history": chat_history})
    answer = output.get("answer", [])

    return jsonify({"answer": answer})
