# Simple RAG LangChain Bot

A simple Retrieval-Augmented Generation (RAG) chatbot that allows you to ask questions about PDF documents and receive answers with source citations.

## 🚀 Features

- **Document-based Q&A**: Ask questions about PDF document content
- **Source Citations**: Each answer includes citations to specific pages in the source document
- **Structured Output**: Answers formatted as JSON with sentence-by-sentence citations
- **Interactive Chat Interface**: Command-line interface for asking questions

## 🛠️ Technologies Used

- [LangChain](https://python.langchain.com/) - Framework for developing applications powered by language models
- [OpenAI](https://openai.com/) - Provides the LLM (GPT-4o-mini) and embedding services
- [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search and clustering of dense vectors
- [PyPDFLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf) - For loading and parsing PDF documents

## 📋 Prerequisites

- Python 3.8+
- An OpenAI API key

## 🛠️ Setup

### 1. Clone or download the repository

```bash
git clone <repository-url>
cd simple-rag-langchain-bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install langchain-community langchain-openai faiss-cpu python-dotenv pypdf
```

### 4. Set up your environment

Create a `.env` file in the project root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Add your PDF document

Place your PDF document in the project directory. By default, the application looks for `ai-in-the-enterprise.pdf`. If you're using a different file, update the filename in `main.py`:

```python
loader = PyPDFLoader("your-document.pdf")
```

## 🚀 Usage

Run the application:

```bash
python main.py
```

The application will:
1. Load the PDF document
2. Split it into chunks
3. Create embeddings and store them in FAISS
4. Start an interactive chat session

Ask questions about your document content. Type "exit", "quit", or "q" to quit the chat.

### Example Interaction

```
📖 RAG chat ready! Type 'exit' to quit.

Ask: What is the main topic of this document?
...
```

## 🏗️ How It Works

1. **Document Loading**: Loads a PDF document using PyPDFLoader
2. **Text Splitting**: Splits the document into chunks of 800 characters with 100-character overlap
3. **Embedding Generation**: Creates embeddings for each chunk using OpenAI's embedding model
4. **Vector Storage**: Stores embeddings in a FAISS vector store for efficient retrieval
5. **Query Processing**: Uses a RetrievalQA chain to answer questions based on the document content
6. **Output Formatting**: Returns answers in JSON format with citations to source pages

## ⚙️ Configuration

The application currently uses these default settings which can be modified in the code:
- Chunk size: 800 characters
- Chunk overlap: 100 characters
- Retrieved documents: 5 most relevant chunks
- Model: GPT-4o-mini
- Temperature: 0 (for more deterministic output)

## 🐛 Known Issues

- The LLM might not always produce perfectly formatted JSON output, in which case the raw output will be shown
- No input validation for empty queries
- Hardcoded file paths (these should be made configurable)

## 🔒 Security Note

- Keep your OpenAI API key secure and never commit it to version control
- The `.env` file should be added to `.gitignore` (if not already there)

## 🤝 Contributing

Contributions are welcome! Some potential improvements include:
- Adding input validation and sanitization
- Making all parameters configurable through environment variables
- Adding support for more document formats
- Implementing structured output parsing for more reliable JSON results
- Adding a web interface

## 📄 License

[MIT License](LICENSE)