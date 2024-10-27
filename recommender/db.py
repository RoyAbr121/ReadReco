import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_milvus import Milvus

current_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

openai_api_embedding = os.getenv('OPENAI_API_EMBEDDING')
milvus_host = os.getenv('MILVUS_HOST')
milvus_port = os.getenv('MILVUS_PORT')
milvus_collection = os.getenv('MILVUS_COLLECTION')

embeddings = OpenAIEmbeddings(model=openai_api_embedding)
db = Milvus(embedding_function=embeddings, collection_name=milvus_collection,
            connection_args={"host": milvus_host, "port": milvus_port})
