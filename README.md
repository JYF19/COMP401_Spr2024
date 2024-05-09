# LOCAL_RAG: Q&A from a pdf file

This project aims to analyze the content of a pdf document using natural language processing techniques. It leverages the power of large language models (LLMs) and vector databases to enable efficient retrieval and generation of relevant information from the document.

## Installation

To set up the project, follow these steps:

1. Install the required libraries:
   ```
   !pip install unstructured langchain
   !pip install "unstructured[all-docs]"
   !pip install chromadb
   !pip install langchain-text-splitters
   ```

2. Clone the project repository:
   ```
   git clone https://github.com/JYF19/COMP401_Spr2024.git
   ```

3. Navigate to the project directory:
   ```
   cd global-cooperation-barometer-analysis
   ```

## Usage

1. Place the "WEF_The_Global_Cooperation_Barometer_2024.pdf" file in the project directory.

2. Open the main script file and update the `local_path` variable with the path to your PDF file:
   ```python
   local_path = "WEF_The_Global_Cooperation_Barometer_2024.pdf"
   ```

3. Run the script to process the PDF, generate embeddings, and set up the retrieval system:
   ```
   python main.py
   ```

4. Once the setup is complete, you can enter your question when prompted:
   ```
   Enter your question:
   ```

5. The script will generate multiple variations of your question, retrieve relevant context from the document, and provide an answer based on the retrieved information.

## Project Structure

The project consists of the following main components:

- **Document Loading**: The script uses the `UnstructuredPDFLoader` from the `langchain_community` library to load the content of the PDF document.

- **Text Splitting**: The loaded document is split into manageable text chunks using the `RecursiveCharacterTextSplitter` from the `langchain_text_splitters` library.

- **Embedding and Vector Database**: The text chunks are embedded using the `OllamaEmbeddings` model and stored in a vector database using the `Chroma` vector store from the `langchain_community` library.

- **Query Generation**: The script defines a prompt template for generating multiple variations of the user's question to improve retrieval effectiveness.

- **Retrieval and Answer Generation**: The `MultiQueryRetriever` is used to retrieve relevant context from the vector database based on the generated query variations. The retrieved context is then used to generate an answer using the specified LLM.

- **Cleanup**: After processing the user's question, the script cleans up by deleting all collections in the vector database to avoid data clutter.

## Dependencies

The project relies on the following libraries:

- `unstructured`: For handling unstructured data like PDFs.
- `langchain`: For building the language model pipeline and retrieval system.
- `chromadb`: For storing and querying embeddings in a vector database.
- `langchain-text-splitters`: For splitting text into manageable chunks.
- `langchain_community`: For accessing community-contributed modules and extensions.

## Acknowledgements

This project utilizes various open-source libraries and models, including:

- Langchain: [https://github.com/hwchase17/langchain](https://github.com/hwchase17/langchain)
- Unstructured: [https://github.com/Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)
- ChromaDB: [https://github.com/chroma-core/chroma](https://github.com/chroma-core/chroma)
- Ollama: [https://github.com/huggingface/ollamaflower](https://github.com/huggingface/ollamaflower)

## License

This project is licensed under the [MIT License](LICENSE).
