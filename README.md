# LOCAL_RAG: PDF Content Analyzer

Welcome to the PDF Content Analyzer, a Python application that utilizes natural language processing to analyze and answer questions from a PDF document. This project leverages the LangChain library to facilitate document loading, text processing, embedding generation, and querying capabilities.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation

Follow these steps to get your environment set up:

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/JYF19/COMP401_Spr2024.git
cd COMP401_Spr2024/main
```

### 2. Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to manage dependencies. Here's how you can set it up:

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install unstructured langchain langchain-community chromadb langchain-text-splitters
```

## Usage

Once you've installed all the required software and libraries, you're ready to run the application.

### Running the Application

1. **Start the Application**:
   Execute the `main.py` script from your terminal. Make sure your virtual environment is activated if you are using one.

   ```bash
   python main.py
   ```

2. **Input the PDF File Path**:
   When prompted, enter the full path to the PDF file you wish to analyze.

3. **Ask a Question**:
   After the PDF is processed, the system will prompt you to enter a question. Type your question and press Enter.

4. **Receive Your Answer**:
   The system will process your question and return an answer based on the content of the PDF.

### Example Interaction

```plaintext
Please enter the path to the PDF file you want to analyze: C:\Users\JohnDoe\Documents\example.pdf
Enter your question: What are the main topics discussed in the document?
Processing... please wait.
The main topics discussed are...
```

## Architecture Overview

This application is structured into several modules, each handling a specific part of the process:

- `load_pdf.py`: Manages the loading of PDF files.
- `text_processing.py`: Handles the splitting and cleaning of text data.
- `embeddings.py`: Responsible for generating embeddings from text.
- `query_processing.py`: Manages the creation and processing of queries.
- `response_handling.py`: Formats and displays responses.

## Contributing

We welcome contributions to this project! If you have suggestions or improvements, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses several open-source packages:
- [LangChain](https://github.com/hwchase17/langchain)
- [Unstructured](https://github.com/Unstructured-IO/unstructured)
- [ChromaDB](https://github.com/chroma-core/chroma)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

Thank you to all the contributors of these projects!
```
