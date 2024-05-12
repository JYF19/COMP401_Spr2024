# text_processing.py
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(data, chunk_size=7500, chunk_overlap=100):
    """
    Split the text data into manageable chunks using RecursiveCharacterTextSplitter.
    
    Args:
        data (list): A list of text data extracted from the PDF document.
        chunk_size (int): The maximum size of each text chunk.
        chunk_overlap (int): The overlap size between chunks to maintain context.
    
    Returns:
        list: A list of text chunks.
    """
    # Create a text splitter instance with specified chunk size and overlap
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # Split the document into chunks and return the chunks
    return splitter.split_documents(data)

def clean_text(text):
    """
    Perform basic text cleaning, removing unwanted characters and whitespace.
    
    Args:
        text (str): The text to be cleaned.
    
    Returns:
        str: The cleaned text.
    """
    # Remove non-printable characters and excessive whitespace
    cleaned_text = re.sub(r'\s+', ' ', text)
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', cleaned_text)
    return cleaned_text.strip()
