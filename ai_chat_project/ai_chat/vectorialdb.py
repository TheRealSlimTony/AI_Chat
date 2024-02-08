from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


class VectorialDatabase:
    def __init__(self, persist_directory="docs/chroma"):
        self.persist_directory = persist_directory
        self.embedding = OpenAIEmbeddings()
        self.vectordb = self.load_vector_db()

    def load_vector_db(self):
        try:
            # Replace 'load' with the appropriate method to load your Chroma vector DB from the disk.
            persist_directory = "docs/chroma"
            embedding = OpenAIEmbeddings()
            vectordb = Chroma(
                persist_directory=persist_directory, embedding_function=embedding
            )
            return vectordb
        except Exception as e:
            print(f"An error occurred while loading the vector DB: {e}")
            return None

    def initialize_with_data(self, file_paths):
        loaders = [PyPDFLoader(path) for path in file_paths]

        docs = []
        for loader in loaders:
            docs.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=150
        )
        splits = text_splitter.split_documents(docs)

        self.vectordb = Chroma.from_documents(
            documents=splits,
            embedding=self.embedding,
            persist_directory=self.persist_directory,
        )
        self.vectordb.persist()

    def similarity_search(self, question, k=5):
        if self.vectordb is None:
            raise ValueError(
                "Vectorial database is not initialized. Please load data first."
            )
        docs = self.vectordb.similarity_search(question, k=k)
        all_pages_content = " ".join([doc.page_content for doc in docs])
        source = docs[0].metadata["source"]
        if docs:
            return (
                all_pages_content,
                source,
            )  # or however you want to process the results
        else:
            return "No matching documents found."

    def load_and_embbed_txt(self, file_paths):
        loaders = [TextLoader(path) for path in file_paths]

        docs = []
        for loader in loaders:
            docs.extend(loader.load())

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500, chunk_overlap=150
        )
        splits = text_splitter.split_documents(docs)

        self.vectordb = Chroma.from_documents(
            documents=splits,
            embedding=self.embedding,
            persist_directory=self.persist_directory,
        )
        self.vectordb.persist()
