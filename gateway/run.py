import os
from gateway import app
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

GATEWAY_ADDRESS = os.getenv('GATEWAY_ADDRESS')
GATEWAY_PORT = os.getenv('GATEWAY_PORT')
DEBUG = os.getenv('DEBUG')

if not GATEWAY_ADDRESS or not GATEWAY_PORT or not DEBUG:
    raise ValueError("GATEWAY_ADDRESS, GATEWAY_PORT and DEBUG must be set.")

if __name__ == '__main__':
    app.run(host=GATEWAY_ADDRESS, port=GATEWAY_PORT, debug=DEBUG)
