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
    top_k=6,
    min_score=0.1,
    return_context=True,
):

    results = retriever.invoke(query)

    # 🔎 Safety fallback for name searches
    q = query.lower()
    if "utkarsh misra" in q:
        keyword_hits = [
            d for d in chunks
            if "utkarsh misra" in d.page_content.lower()
        ]
        if keyword_hits:
            results = keyword_hits[:6]

    if not results:
        return {
            "answer": "⚠️ No relevant content was found in the loaded PDFs or text files.",
            "confidence": 0,
            "sources": [],
            "context": ""
        }


    context = "\n\n".join(doc.page_content for doc in results)

    prompt = f"""
You are answering questions only using the provided CONTEXT.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = llm.invoke(prompt)
    answer = response.content if hasattr(response, "content") else response


    sources = [
        {
            "source": doc.metadata.get("source", "unknown"),
            "page": doc.metadata.get("page", "-"),
            "preview": doc.page_content[:200] + "..."
        }
        for doc in results
    ]

    return {
        "answer": answer,
        "confidence": 0.90,
        "sources": sources,
        "context": context if return_context else None,
    }



