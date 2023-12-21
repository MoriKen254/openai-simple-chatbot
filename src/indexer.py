import os
from llama_index import download_loader


class Indexer():
    def __init__(self, openai_api_key):
        self._openai_api_key = openai_api_key
        os.environ["OPENAI_API_KEY"] = self._openai_api_key
    
    def create(self, index_urls, store_index=True):
        BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
        loader = BeautifulSoupWebReader()
        documents = loader.load_data(urls=index_urls)

        from llama_index import GPTVectorStoreIndex
        # Create index
        self._index = GPTVectorStoreIndex.from_documents(documents)

        if store_index:
            self._index.storage_context.persist()

        return self._index       

    def load(self, index_dir="./storage"):
        from llama_index import VectorStoreIndex, SimpleDirectoryReader
        from llama_index.readers import BeautifulSoupWebReader
        from llama_index import StorageContext, load_index_from_storage
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        # load index
        self._index = load_index_from_storage(storage_context)

        return self._index

    # def answer(self, prompt="What is the main focus on this web site? describe in detail."):
    #     # Create query engine
    #     query_engine = self._index.as_query_engine()
    #     print(query_engine.query(prompt))


