# query_processing.py
from langchain.prompts import ChatPromptTemplate, PromptTemplate

def generate_query_template():
    """
    Generates a prompt template to facilitate the creation of multiple query versions for improved retrieval.
    
    Returns:
        PromptTemplate: A template that instructs the language model on how to generate alternative queries.
    """
    template_text = """
    You are an AI language model assistant. Your task is to generate five different versions of the given user question
    to retrieve relevant documents from a vector database. By generating multiple perspectives on the user question,
    your goal is to help the user overcome some of the limitations of the distance-based similarity search. Provide
    these alternative questions separated by newlines. Original question: {question}
    """
    # Return a prompt template with the defined text
    return PromptTemplate(
        input_variables=["question"],
        template=template_text
    )

def process_user_query(question, model, retriever):
    """
    Processes a user's question to generate multiple queries and retrieve relevant responses.
    
    Args:
        question (str): The user's input question.
        model (object): The language model used for generating queries.
        retriever (object): The retrieval system to fetch answers based on queries.
    
    Returns:
        str: The retrieved answer based on the processed queries.
    """
    # Generate alternative queries using the model and the template
    query_template = generate_query_template()
    alternative_queries = model.generate(query_template.fill(question=question))
    
    # Use the retriever to get the most relevant responses based on the alternative queries
    responses = retriever.retrieve(alternative_queries)
    
    # Combine responses into a single answer string
    combined_response = " ".join(responses)
    return combined_response
