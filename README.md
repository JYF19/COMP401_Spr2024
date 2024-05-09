# COMP401_Spr2024
Senior Seminar Project based on passion project (Foundational)
# Local RAG PDF Q&A Tool

## Project Overview
This project provides a tool for analyzing PDF documents related to global cooperation, specifically focusing on the "Global Cooperation Barometer 2024" report by the World Economic Forum. The script extracts text from specified PDF documents, processes the text to create vector embeddings, and sets up a queryable vector database. This enables users to ask questions and retrieve relevant information from the loaded documents, leveraging state-of-the-art natural language processing techniques.

## Built With
- Python
- LangChain - for document loading and handling
- Unstructured - for PDF processing
- ChromaDB - for vector storage and retrieval
- PyPi libraries (Ollama, ChromaDB) for embeddings and text splitting

## Getting Started

### Prerequisites
- Python 3.6 or later
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/global-cooperation-barometer-tool.git
   cd global-cooperation-barometer-tool
