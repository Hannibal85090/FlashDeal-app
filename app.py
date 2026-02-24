import streamlit as st

st.set_page_config(page_title="FlashDeal - High Quality", layout="wide")

# تصحيح الخطأ: يجب وضع كود CSS داخل st.markdown مع تفعيل unsafe_allow_html
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;900&display=swap');
    
    .main { background-color: #020617; color: white; font-family: 'Inter', sans-serif; }
    .glass-card { 
        background: rgba(30, 41, 59, 0.7); 
        backdrop-filter: blur(10px); 
        border: 1px solid rgba(34, 211, 238, 0.2); 
        border-radius: 1rem; 
        padding: 2rem;
        margin-bottom: 1rem;
    }
    .neon-text { color: #22d3ee; text-shadow: 0 0 10px rgba(34, 211, 238, 0.5); font-weight: 900; }
    .stButton>button {
        background: linear-gradient(90deg, #22d3ee, #3b82f6);
        color: black;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيكل التنظيمي للمشروع الموازي
st.markdown('<h1 class="neon-text">FlashDeal</h1>', unsafe_allow_html=True)
st.caption("Talk. Pay. Done. | Parallel High-Quality Project")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Security Star Protection")
    st.checkbox("Face ID Verification", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Body Movement Compatibility")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.metric("Token Wallet", "1,250 FTK", "-50 FTK")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Investor Pitch: Future Vision")
    st.write("Targeting 320% growth by 2027 through 'My FlashDeal Star' hardware integration.")
    st.progress(75, text="User Adoption Growth")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Request Demo"):
        st.balloons()
        st.success("Demo request sent securely via Mutual Token.")

st.sidebar.info("User: Hanniball85090\n\nDevice: FlashDeal Star Connected")
