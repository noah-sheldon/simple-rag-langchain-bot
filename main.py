from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import json

load_dotenv()

# 1. Load PDF
loader = PyPDFLoader("ai-in-the-enterprise.pdf")
docs = loader.load()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 3. Embeddings + FAISS
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# --- Prompt for JSON per sentence ---
PROMPT_TMPL = """
You are a helpful assistant. Use ONLY the context below to answer the question.  

Break the answer into multiple short sentences.  
For each sentence, return a JSON object with two keys:
- "sentence": the sentence text  
- "citation": the source in the format "<filename>, page <n>"  

The final output MUST be a valid JSON array.  
If the answer is not in the context, return: []  

Question: {question}  

Context:
{context}  

Answer as JSON:
"""

PROMPT = PromptTemplate(
    template=PROMPT_TMPL,
    input_variables=["question", "context"]
)

# --- Retrieval QA ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True,
)

# --- Chat loop ---
print("📖 RAG chat ready! Type 'exit' to quit.\n")
while True:
    query = input("Ask: ")
    if query.lower() in ["exit", "quit", "q"]:
        break

    result = qa.invoke({"query": query})
    raw_answer = result["result"]

    try:
        parsed = json.loads(raw_answer)
        print("\n=== Parsed JSON Output ===")
        print(json.dumps(parsed, indent=2))
    except Exception:
        print("\n[WARN] Could not parse JSON. Raw output below:\n")
        print(raw_answer)

    # show retrieved sources for transparency
    print("\n=== Retrieved Sources ===")
    for doc in result.get("source_documents", []):
        print(f"- {doc.metadata.get('source')} p.{doc.metadata.get('page')}")
    print("\n---\n")
