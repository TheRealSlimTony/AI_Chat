# ai_chat/embedding_process.py

from vectorialdb import VectorialDatabase


class EmbeddingProcess:
    def __init__(self, persist_directory="docs/chroma"):
        self.vectordb = VectorialDatabase(persist_directory=persist_directory)

    def process_txt_documents(self, file_paths):
        # Llama al método para procesar y agregar archivos TXT
        self.vectordb.load_and_embbed_txt(file_paths)

    def process_pdf_documents(self, file_paths):
        # Método similar para procesar PDFs si es necesario
        self.vectordb.initialize_with_data(file_paths)

    # Aquí podrías añadir más métodos según sea necesario,
    # por ejemplo, para actualizar documentos, eliminar, etc.


print("hey! I'm the embedding process module!")


def run_example():

    # Instancia tu clase EmbeddingProcess
    embedding_process = EmbeddingProcess()

    embedding_process.process_pdf_documents(
        [r"C:\Users\Its Tony Again PC\Downloads\Naruto.pdf"]
    )
    print("Embedding process finished!")
    db = VectorialDatabase(persist_directory="docs/chroma")
    context = db.similarity_search("who is narturo")
    print(context)


if __name__ == "__main__":
    run_example()
