st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* ---------- MAIN BACKGROUND ---------- */
.stApp {
    background:
        linear-gradient(rgba(2,6,23,0.85), rgba(2,6,23,0.85)),
        url("https://images.unsplash.com/photo-1614064642638-95b84efb7738?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
}

/* ---------- HERO ---------- */
.hero-card {
    background: linear-gradient(145deg, rgba(15,23,42,0.9), rgba(2,6,23,0.9));
    border-radius: 26px;
    padding: 3rem 2.5rem;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 35px rgba(0,245,160,0.08);
}

/* ---------- TITLE ---------- */
.hero-title {
    font-size: 3.3rem;
    font-weight: 800;
    background: linear-gradient(90deg,#22d3ee,#22c55e,#38bdf8);
    -webkit-background-clip: text;
    color: transparent;
}

.hero-sub {
    font-size:1.15rem;
    color:#e5e7eb;
}

/* ---------- INPUT ---------- */
input {
    background: rgba(255,255,255,0.9) !important;
    border-radius: 18px !important;
    padding: 0.75rem 1.2rem !important;
}

/* ---------- BUTTON ---------- */
button {
    background: linear-gradient(90deg,#22c55e,#38bdf8) !important;
    border-radius: 18px !important;
    font-weight:600 !important;
}

/* ---------- ANSWER ---------- */
.answer-box{
    background: rgba(10,16,32,0.88);
    color: white !important;
    padding: 20px;
    border-radius: 16px;
    font-size: 16px;
    line-height: 1.6;
    box-shadow: 0 0 15px rgba(0,255,255,0.15);
}

.answer-box ul,
.answer-box li,
.answer-box p,
.answer-box span{
    color:#ffffff !important;
    opacity:1 !important;
}

/* ---------- ANSWER CARD ---------- */
.answer-card{
    background: linear-gradient(145deg, rgba(8,14,35,0.96), rgba(16,30,60,0.96));
    border-radius: 22px;
    padding: 1.8rem;
}

/* ---------- SOURCES ---------- */
.source-box{
    background: rgba(15,23,42,0.9);
    border-radius: 18px;
    padding: 1rem 1.4rem;
    border-left:4px solid #38bdf8;
}

.source-file{
    color:#38BDF8;
    font-weight:700;
}

/* ---------- HIGH CONTRAST ---------- */
.answer-text,
.source-box p,
label,p,span{
    color:#F1F5F9 !important;
}

/* ---------- CLEANUP ---------- */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)
