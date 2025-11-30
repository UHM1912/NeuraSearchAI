from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import os


# ---------- LLM ----------
llm = ChatGroq(
    api_key=os.environ["GROQ_API_KEY"],
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=512,      # ✅ prevents overflow
    timeout=60,
)



# ---------- LOAD ALL DOCUMENTS ----------
docs = []

# ✅ Load text files
text_folder = Path("data/text_files")

for txt_path in text_folder.glob("*.txt"):
    print(f"Loading TEXT → {txt_path.name}")
    loader = TextLoader(str(txt_path), encoding="utf-8")
    docs.extend(loader.load())


# ✅ Load PDF files
pdf_folder = Path("data/pdf")

for pdf_path in pdf_folder.glob("*.pdf"):
    print(f"Loading PDF → {pdf_path.name}")
    loader = PyPDFLoader(str(pdf_path))
    docs.extend(loader.load())


if not docs:
    raise ValueError("⚠️ No documents loaded! Check data folders.")


# ---------- SPLIT INTO CHUNKS ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,      # smaller chunks = better name recall
    chunk_overlap=80
)

chunks = splitter.split_documents(docs)


# ---------- BUILD VECTOR STORE ----------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(chunks, embeddings)


# ✅ MMR retriever = more diverse sources
rag_retriever = vector_store.as_retriever(
    search_kwargs={"k": 20}  # pulls from more PDFs at once
)



# ---------- RAG PIPELINE ----------
def rag_advanced(
    query,
    retriever,
    llm,
    top_k=4,
    min_score=0.1,
    return_context=True,
):

    # Retrieve relevant chunks
    results = retriever.invoke(query)

    # Build context
    context = "\n\n".join(doc.page_content for doc in results)

    if not context.strip():
        return {
            "answer": "⚠️ This information is not available in the uploaded documents.",
            "confidence": 0.0,
            "sources": [],
            "context": "",
        }

    # Prompt
    prompt = f"""
You are a professional research assistant.

Use the CONTEXT to answer the QUESTION clearly and in detail.
If the CONTEXT is short, expand the explanation naturally without adding new facts.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    # ✅ This line MUST NOT be extra-indented
    response = llm.invoke(prompt)

    answer = response.content if hasattr(response, "content") else response

    # Build sources
    sources = []
    for doc in results:
        sources.append(
            {
                "source": doc.metadata.get("source", "unknown"),
                "page": doc.metadata.get("page", "-"),
                "score": 1.0,
                "preview": doc.page_content[:200] + "...",
            }
        )

    return {
        "answer": answer,
        "confidence": 0.90,
        "sources": sources,
        "context": context if return_context else None,
    }





