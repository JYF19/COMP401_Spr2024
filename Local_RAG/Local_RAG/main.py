# main.py
from load_pdf import load_pdf
from text_processing import split_text, clean_text
from embeddings import create_embeddings
from query_processing import process_user_query
from response_handling import format_response

def main():
    """
    Main function to run the entire processing chain from loading a PDF to answering queries.
    Asks the user to input the path to the PDF file they wish to process.
    """
    file_path = input("Please enter the path to the PDF file you want to analyze: ")
    try:
        # Load PDF and process text
        raw_data = load_pdf(file_path)
        chunks = split_text(raw_data)
        cleaned_chunks = [clean_text(chunk) for chunk in chunks]
        
        # Create embeddings and setup retriever
        vector_db = create_embeddings(cleaned_chunks)
        model = "your_lang_model"  # Placeholder for actual model initialization
        
        # Prompt user to enter a question
        user_question = input("Enter your question: ")
        
        # Process user query
        response = process_user_query(user_question, model, vector_db)
        
        # Format and output the response
        print(format_response(response, user_question))
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
