import streamlit as st
from notebook.document import rag_retriever, llm, rag_advanced

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="NeuraSearch AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# FULL FUTURISTIC UI CSS
# ---------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* ---------- MAIN BACKGROUND ---------- */
.stApp {
    background:
        linear-gradient(
            rgba(2,6,23,0.85),
            rgba(2,6,23,0.85)
        ),
        url("https://images.unsplash.com/photo-1614064642638-95b84efb7738?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
}

/* ---------- HERO CARD ---------- */
.hero-card {
    background: linear-gradient(
        145deg,
        rgba(8,14,35,0.96),
        rgba(16,30,60,0.96)
    );
    border-radius: 26px;
    padding: 3rem 2.5rem;
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow:
        0 0 35px rgba(0,245,160,0.08),
        inset 0 0 10px rgba(0,0,0,0.5);
    margin-bottom: 2rem;

    animation: slideIn 0.8s ease forwards;
}

/* ---------- HERO TITLE ---------- */
.hero-title {
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(90deg,#22d3ee,#22c55e,#38bdf8);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 18px rgba(56,189,248,0.35);
}

/* ---------- HERO SUBTITLE ---------- */
.hero-sub {
    margin-top: 0.6rem;
    font-size: 1.15rem;
    color: #E5E7EB;

    white-space: nowrap;
    overflow: hidden;
    border-right: 3px solid rgba(255,255,255,.6);
    width: 0;

    animation:
        typing 4s steps(60,end) forwards,
        blink 0.7s infinite;
}

/* ---------- INPUT ---------- */
input {
    background: rgba(255,255,255,0.95) !important;
    border-radius: 18px !important;
    padding: 0.75rem 1.2rem !important;
    font-size: 1.05rem !important;
    box-shadow: 0 0 15px rgba(56,189,248,0.2);
}

/* ---------- BUTTON ---------- */
button {
    background: linear-gradient(90deg,#22c55e,#38bdf8) !important;
    color: #020617 !important;
    border-radius: 18px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;

    box-shadow:
        0 0 16px rgba(56,189,248,0.45) !important;
}

button:hover {
    transform: scale(1.05);
    filter: brightness(1.2);
}

/* ---------- ANSWER CARD ---------- */
.answer-card {
    background: linear-gradient(
        145deg,
        rgba(8,14,35,0.98),
        rgba(16,30,60,0.98)
    );

    border-radius: 22px;
    padding: 1.8rem;
    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 0 35px rgba(0,0,0,0.5);

    animation: slideIn 0.5s ease forwards;
}

/* ---------- BADGE ---------- */
.confidence-badge {
    padding: 6px 18px;
    border-radius: 999px;
    background: linear-gradient(90deg,#38bdf8,#22c55e);
    color: #020617;
    font-weight: 700;
}

/* ---------- SOURCES ---------- */
.source-box{
    background: linear-gradient(
        145deg,
        rgba(8,14,35,0.98),
        rgba(16,30,60,0.98)
    );

    border-radius: 18px;
    padding: 1rem 1.4rem;
    margin-bottom: 10px;

    border-left: 4px solid #38bdf8;
}

/* ---------- TEXT OVERRIDES ---------- */

h1, h2, h3, h4, h5 {
    color: #F8FAFC !important;
}

p,
span,
label,
small,
li,
.answer-text,
[data-testid="stMarkdownContainer"] > p {
    color: #F1F5F9 !important;
    font-size: 1.1rem;
    line-height: 1.8;
    opacity: 1 !important;
}

/* Source filename */
.source-file {
    color: #38BDF8 !important;
    font-weight: 700;
}

/* ---------- ANIMATIONS ---------- */

@keyframes slideIn {
    from {
        transform: translateY(30px);
    }
    to {
        transform: translateY(0);
    }
}

@keyframes typing {
    from { width: 0; }
    to   { width: 100%; }
}

@keyframes blink {
    from,to { border-color: transparent; }
    50% { border-color: white; }
}

/* ---------- FOOTER ---------- */
footer { visibility: hidden; }

</style>
""", unsafe_allow_html=True)

# ---------------------------
# HERO SECTION
# ---------------------------
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🤖 NeuraSearch AI</div>
    <div class="hero-sub">
        Futuristic document intelligence powered by Retrieval-Augmented Generation
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# INPUT
# ---------------------------
query = st.text_input(
    "",
    placeholder="Ask anything about your documents… e.g. 'Who is Utkarsh Misra?'",
    key="query_input"
)

ask = st.button("🔍 Search Knowledge Base", use_container_width=True)

# ---------------------------
# RUN RAG
# ---------------------------
if ask and query.strip():

    with st.spinner("🧠 Scanning knowledge base..."):

        result = rag_advanced(
            query=query,
            retriever=rag_retriever,
            llm=llm,
            top_k=6,
            min_score=0.1,
            return_context=True
        )

    # ---------------------------
    # OUTPUT
    # ---------------------------
    st.markdown("""
        <div class="answer-card">
            <h2>✅ Answer</h2>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="answer-box">
            <p class="answer-text">{result['answer']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="margin-top:12px">
            <span class="confidence-badge">
                Confidence: {result["confidence"]*100:.1f}%
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)
