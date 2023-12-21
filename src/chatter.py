import os
from llama_index import StorageContext, load_index_from_storage


class Chatter():
    def __init__(self, openai_api_key):
        self._openai_api_key = openai_api_key
        os.environ["OPENAI_API_KEY"] = self._openai_api_key

    def create_engine(self, index):
        self._query_engine = index.as_query_engine()

    def answer(self, prompt="What is the main focus on this web site especially about gmapping? describe in Japanese."):
        return self._query_engine.query(prompt)
