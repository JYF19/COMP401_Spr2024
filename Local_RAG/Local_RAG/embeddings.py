# embeddings.py
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def create_embeddings(chunks, model_name="nomic-embed-text"):
    """
    Create embeddings for the text chunks and store them in a vector database.
    
    Args:
        chunks (list): List of text chunks to be embedded.
        model_name (str): The model to use for generating embeddings.
    
    Returns:
        Chroma: A vector database containing the embedded text chunks.
    """
    # Create a vector database with specified embedding model and collection name
    try:
        vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=OllamaEmbeddings(model=model_name, show_progress=True),
            collection_name="local-rag"
        )
        return vector_db
    except Exception as e:
        print(f"Failed to create embeddings: {e}")
        raise
