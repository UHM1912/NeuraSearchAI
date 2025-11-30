import streamlit as st
from notebook.document import rag_retriever, llm, rag_advanced


# ---------------------------
# Page config
# ---------------------------
st.set_page_config(
    page_title="Utkarsh RAG Assistant",
    page_icon="📚",
    layout="wide"
)



# ---------------------------
# Custom Premium CSS
# ---------------------------
import streamlit as st

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="NeuraSearch AI",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------
# FULL FUTURISTIC CSS
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
        rgba(15,23,42,0.9),
        rgba(2,6,23,0.9)
    );
    border-radius: 26px;
    padding: 3rem 2.5rem;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 0 35px rgba(0,245,160,0.08),
        inset 0 0 10px rgba(0,0,0,0.5);
    margin-bottom: 2rem;

    animation: fadeInUp 1s ease forwards;
}

/* ---------- HERO TITLE ---------- */
.hero-title {
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(90deg,
        #22d3ee,
        #22c55e,
        #38bdf8
    );

    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 18px rgba(56,189,248,0.35);

    animation: glowPulse 4s infinite ease-in-out;
}

/* ---------- HERO SUBTITLE (TYPEWRITER) ---------- */
.hero-sub {
    margin-top: 0.6rem;
    font-size: 1.15rem;
    color: #e5e7eb;

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
    background: rgba(255,255,255,0.9) !important;
    border-radius: 18px !important;
    padding: 0.75rem 1.2rem !important;
    font-size: 1.05rem !important;
    box-shadow: 0 0 15px rgba(56,189,248,0.2);
}

/* ---------- BUTTON ---------- */
button {
    background: linear-gradient(
        90deg,
        #22c55e,
        #38bdf8
    ) !important;

    color: #020617 !important;
    border-radius: 18px !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;

    box-shadow:
        0 0 16px rgba(56,189,248,0.45) !important;

    transition: 0.3s ease all;
}

button:hover {
    transform: scale(1.05);
    filter: brightness(1.2);
    box-shadow:
        0 0 30px rgba(34,197,94,0.75) !important;
}

/* ---------- ANSWER CARD ---------- */

.answer-card {
    background:
        linear-gradient(
            145deg,
            rgba(2,6,23,0.95),
            rgba(15,23,42,0.95)
        );

    border-radius: 22px;
    padding: 1.8rem;
    border: 1px solid rgba(255,255,255,0.1);

    box-shadow:
        0 0 40px rgba(0,0,0,0.5);

    animation: fadeInUp 0.6s ease backwards;
}

.confidence-badge {
    padding: 6px 18px;
    border-radius: 999px;
    background: linear-gradient(90deg,#38bdf8,#22c55e);
    color: black;
    font-weight: 600;
}

/* ---------- SOURCES ---------- */

.source-box{
    background: rgba(15,23,42,0.9);

    border-radius: 18px;
    padding: 1rem 1.4rem;
    margin-bottom: 10px;

    border-left: 4px solid #38bdf8;

    animation: fadeInUp 0.5s ease backwards;
}

.source-file {
    color: #60a5fa;
    font-weight: 600;
}


/* ---------- ANIMATIONS ---------- */

@keyframes glowPulse {
    0%   { text-shadow: 0 0 6px #22d3ee; }
    50%  { text-shadow: 0 0 25px #22c55e; }
    100% { text-shadow: 0 0 6px #38bdf8; }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
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


/* ---------- CLEANUP ---------- */
footer { visibility: hidden; }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* ----------------------------
   FORCE HIGH CONTRAST TEXT
-----------------------------*/

.answer-text,
.answer-box p,
.source-box p,
.source-box small,
.source-box div,
.source-file,
label,
p,
span {
    color: #F1F5F9 !important;   /* ✅ Bright readable white */
}

/* Make answer body really legible */
.answer-text {
    font-size: 1.15rem !important;
    line-height: 1.8 !important;
    opacity: 1 !important;
}

/* Source filename = accent blue */
.source-file {
    color: #38BDF8 !important;
    font-weight: 700 !important;
}

/* Preview text softer but readable */
.source-box p {
    color: #E5E7EB !important;
    opacity: 0.95 !important;
}

/* Page labels brighter */
.source-box small {
    color: #94A3B8 !important;
}

/* Section titles like "Answer", "Sources" */
h2, h3 {
    color: #E5E7EB !important;
}

/* Expanders text */
.streamlit-expanderHeader {
    color: #F1F5F9 !important;
}

/* Default Streamlit text */
[data-testid="stMarkdownContainer"] > p {
    color: #F8FAFC !important;
}

/* Fix button text */
button span {
    color: #020617 !important;
}

/* ✅ Make entire glass cards slightly lighter to avoid washout */
.hero-card,
.answer-card,
.source-box {
    background: linear-gradient(
        145deg,
        rgba(8,14,35,0.96),
        rgba(16,30,60,0.96)
    ) !important;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="hero-card">
    <div class="hero-title">🤖 NeuraSearch AI</div>
    <div class="hero-sub">
        Futuristic document intelligence powered by Retrieval-Augmented Generation
    </div>
</div>
""", unsafe_allow_html=True)





# ---------------------------
# INPUT AREA
# ---------------------------
query = st.text_input(
    "",
    placeholder="Ask anything about your PDFs — for example: 'Who is Utkarsh Misra?'",
    key="query_input"
)


# ---------------------------
# ASK BUTTON
# ---------------------------
ask = st.button("🔍 Search Knowledge Base", use_container_width=True)


# ---------------------------
# RUN RAG
# ---------------------------
if ask and query.strip():

   with st.spinner(""):
    st.markdown("""
    <div class="loading-wrapper">
        <div class="loading-card">
            <span class="loading-text">
                🧠 Scanning knowledge base<span class="loading-dots"></span>
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)


    result = rag_advanced(
        query=query,
        retriever=rag_retriever,
        llm=llm,
        top_k=6,
        min_score=0.1,
        return_context=True
    )

    result = rag_advanced(
            query=query,
            retriever=rag_retriever,
            llm=llm,
            top_k=6,
            min_score=0.1,
            return_context=True
        )

    # ---------------------------
    # ANSWER CARD
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


   
