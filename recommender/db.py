import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_milvus import Milvus

load_dotenv()
milvus_embedding = os.getenv('MILVUS_EMBEDDING')
milvus_host = os.getenv('MILVUS_HOST')
milvus_port = os.getenv('MILVUS_PORT')
milvus_collection = os.getenv('MILVUS_COLLECTION')

embeddings = OpenAIEmbeddings(model=milvus_embedding)
db = Milvus(embedding_function=embeddings, collection_name=milvus_collection,
            connection_args={"host": milvus_host, "port": milvus_port})
