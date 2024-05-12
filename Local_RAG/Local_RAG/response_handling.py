# response_handling.py
from langchain.prompts import ChatPromptTemplate

def get_response_prompt():
    """
    Creates a prompt template to facilitate the generation of answers based on retrieved contexts.
    
    Returns:
        ChatPromptTemplate: A template that instructs the language model on how to generate an answer.
    """
    response_template = """
    Answer the question based ONLY on the following context:
    {context}
    Question: {question}
    """
    return ChatPromptTemplate.from_template(response_template)

def format_response(context, question):
    """
    Formats the final response by integrating the context with the question to provide a detailed answer.
    
    Args:
        context (str): The retrieved context that is relevant to the user's query.
        question (str): The original user's question.
    
    Returns:
        str: The formatted response that combines context analysis and a direct answer.
    """
    prompt = get_response_prompt()
    # Fill the template with the actual context and question
    formatted_prompt = prompt.fill(context=context, question=question)
    
    # Generate the response using the filled prompt
    # Assume `llm` is a pre-initialized language model instance (not shown here for brevity)
    response = llm.generate(formatted_prompt)
    return response
