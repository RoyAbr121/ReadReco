import os
from recommender import app
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

RECOMMENDER_ADDRESS = os.getenv('RECOMMENDER_ADDRESS')
RECOMMENDER_PORT = os.getenv('RECOMMENDER_PORT')
DEBUG = os.getenv('DEBUG')

if not RECOMMENDER_ADDRESS or not RECOMMENDER_PORT or not DEBUG:
    raise ValueError("RECOMMENDER_ADDRESS, RECOMMENDER_PORT and DEBUG must be set.")

if __name__ == '__main__':
    app.run(host=RECOMMENDER_ADDRESS, port=RECOMMENDER_PORT, debug=DEBUG)