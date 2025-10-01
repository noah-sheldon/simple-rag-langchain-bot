# Simple RAG LangChain Bot

## Project Overview

This is a simple Retrieval-Augmented Generation (RAG) chatbot built using LangChain, OpenAI, and FAISS. The project enables users to ask questions about the content of a PDF document ("ai-in-the-enterprise.pdf") and receive answers with citations to specific pages in the document.

### Key Technologies

- **LangChain**: Framework for developing applications powered by language models
- **OpenAI**: Provides the LLM (GPT-4o-mini) and embedding services
- **FAISS**: Facebook AI Similarity Search for efficient similarity search and clustering of dense vectors
- **PyPDFLoader**: For loading and parsing PDF documents
- **RecursiveCharacterTextSplitter**: For splitting documents into manageable chunks
- **dotenv**: For loading environment variables from a .env file

### Project Architecture

The application follows a standard RAG pattern:

1. **Document Loading**: Loads a PDF document using PyPDFLoader
2. **Text Splitting**: Splits the document into chunks of 800 characters with 100-character overlap
3. **Embedding Generation**: Creates embeddings for each chunk using OpenAI's embedding model
4. **Vector Storage**: Stores embeddings in a FAISS vector store for efficient retrieval
5. **Query Processing**: Uses a RetrievalQA chain to answer questions based on the document content
6. **Output Formatting**: Returns answers in JSON format with citations to source pages

## Setup and Installation

### Prerequisites

- Python 3.8+
- OpenAI API key

### Environment Setup

1. Create a virtual environment:
   ```bash
   cd simple-rag-langchain-bot
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required dependencies:
   ```bash
   pip install langchain-community langchain-openai faiss-cpu python-dotenv PyPDF2
   ```

3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Place your PDF document in the project directory and update the filename in `main.py` if needed (currently set to "ai-in-the-enterprise.pdf").

## Running the Application

To run the RAG chatbot:

```bash
python main.py
```

The application will:
1. Load the PDF document
2. Split it into chunks
3. Create embeddings and store them in FAISS
4. Start an interactive chat session where you can ask questions about the document content

To exit the chat, type "exit", "quit", or "q".

## Project Structure

```
simple-rag-langchain-bot/
├── main.py          # Main application code
├── ai-in-the-enterprise.pdf  # Sample PDF document
├── .env             # Environment variables (not committed)
└── venv/            # Python virtual environment
```

## Dependencies

The main dependencies inferred from the code are:
- langchain-community
- langchain-openai
- langchain
- faiss-cpu
- python-dotenv
- PyPDF2 or pypdf

## Key Features

1. **Document-based Q&A**: Answers questions based on content from a PDF document
2. **Source Citations**: Each sentence in the response includes a citation to the source page
3. **JSON Output**: Responses are formatted as JSON for easy parsing
4. **Interactive Chat**: Command-line interface for asking questions
5. **Retrieval-based**: Uses FAISS for semantic search in document chunks

## How It Works

1. The PDF is loaded and split into manageable chunks
2. Each chunk is embedded using OpenAI's embedding model
3. Chunks and embeddings are stored in a FAISS vector store
4. When a question is asked, the system retrieves the most relevant chunks
5. The LLM generates an answer based on the retrieved context
6. The response is formatted as a JSON array with citations for each sentence