# load_pdf.py
from langchain_community.document_loaders import UnstructuredPDFLoader

def load_pdf(file_path):
    """
    Load the content of a PDF file using the UnstructuredPDFLoader.
    
    Args:
        file_path (str): The path to the PDF file to be loaded.
        
    Returns:
        list: A list of document pages loaded from the PDF file.
        
    Raises:
        FileNotFoundError: If the PDF file cannot be found at the specified path.
        Exception: For other issues that may occur during the loading process.
    """
    try:
        # Initialize the PDF loader with the specified file path
        loader = UnstructuredPDFLoader(file_path=file_path)
        # Load the document content and return the loaded data
        return loader.load()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while loading the PDF: {e}")
        raise
