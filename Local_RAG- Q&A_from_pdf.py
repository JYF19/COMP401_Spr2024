# Import necessary libraries for handling PDFs
!pip install unstructured langchain
!pip install "unstructured[all-docs]"

# Import necessary modules for document loading and handling
from langchain_community.document_loaders import UnstructuredPDFLoader #PDFMiner Loader for more structured data
from langchain_community.document_loaders import OnlinePDFLoader

# Specify the path to the local PDF file to be processed
local_path = ""

# Load data from the specified local PDF file
if local_path:
    # Initialize the PDF loader with the path to the PDF file
    loader = UnstructuredPDFLoader(file_path=local_path)
    # Load the document content into the data variable
    data = loader.load()
else:
    # Prompt to upload a PDF if no local path is provided
    print("Upload a PDF file")

# Display the first page of the PDF to verify content loading
print(data[0].page_content)

# Install additional libraries for handling embeddings and vector databases
!pip install chromadb
!pip install langchain-text-splitters

# Import modules for embeddings and vector stores
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Define parameters for splitting the document into manageable text chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=100)
chunks = text_splitter.split_documents(data)

# Initialize a vector database using the split text chunks and specified embedding model
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    collection_name="local-rag"  # Specify a unique collection name for the project
)

# Set up the local model and import modules for retrieval
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

local_model = "mistral"  # Model name for the LLM, can be swapped with other open-source models that can be run on your system
llm = ChatOllama(model=local_model)

# Define a prompt template for generating multiple query variations
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate three
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}"""
)

# Initialize the retriever with the query prompt and LLM
retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), 
    llm,
    prompt=QUERY_PROMPT
)

# Define a prompt template for generating answers based on retrieved context
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Combine all components into a single runnable chain for processing user queries
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Example usage of the chain with a user input
response = chain.invoke(input("Enter your question: "))
print(response)

# Clean up by deleting all collections in the vector database to avoid data clutter
vector_db.delete_collection()
