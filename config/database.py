from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def crie_conexao_mongo(colecao):
  client = MongoClient(os.getenv('MONGO_URL'))
  db = client[os.getenv('BANCO_MONGO')]
  return db[colecao]
