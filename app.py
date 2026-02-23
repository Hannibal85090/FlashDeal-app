import streamlit as st

# FlashDeal - My Star: High-Quality Parallel Project Implementation
st.set_page_config(page_title="FlashDeal - My Star", page_icon="💫", layout="centered")

# Custom CSS to match the Cyber-Tech visual identity
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Neon Title & Slogan */
    h1 {
        color: #00FBFF !important;
        text-shadow: 0 0 15px #00FBFF;
        text-align: center;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
    }
    .slogan {
        text-align: center;
        color: #7000FF;
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 30px;
        text-transform: uppercase;
    }
    
    /* Icon Dashboard for Seniors & Accessibility */
    .dashboard-container {
        display: flex;
        justify-content: space-around;
        margin-bottom: 35px;
    }
    .icon-card {
        background: rgba(30, 33, 41, 0.8);
        padding: 15px;
        border-radius: 20px;
        border: 1px solid #7000FF;
        width: 100px;
        text-align: center;
        transition: 0.3s;
    }
    .icon-card:hover {
        border-color: #00FBFF;
        box-shadow: 0 0 20px rgba(0, 251, 255, 0.3);
        transform: translateY(-5px);
    }
    .icon-text {
        font-size: 0.7em;
        margin-top: 8px;
        color: #00FBFF;
        font-weight: bold;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #1E2129;
        border-radius: 10px;
        color: white;
    }
    
    /* Buttons with Gradient */
    .stButton>button {
        background: linear-gradient(90deg, #00FBFF 0%, #7000FF 100%);
        color: white;
        border: none;
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>⚡ FLASHDEAL</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

# --- ICON DASHBOARD (Shield, Clock, Crown) ---
st.markdown("""
    <div class="dashboard-container">
        <div class="icon-card">
            <div style="font-size: 2em;">🛡️</div>
            <div class="icon-text">SECURITY</div>
        </div>
        <div class="icon-card">
            <div style="font-size: 2em;">🕒</div>
            <div class="icon-text">SPEED</div>
        </div>
        <div class="icon-card">
            <div style="font-size: 2em;">👑</div>
            <div class="icon-text">QUALITY</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN NAVIGATION TABS ---
tab1, tab2, tab3 = st.tabs(["🎙️ Voice Control", "💰 Token Wallet", "🔒 Security Star"])

with tab1:
    st.markdown("### Smart Transaction")
    st.info("Ready for your voice command.")
    if st.button("ACTIVATE VOICE RECORDING"):
        st.success("Voice recognition active: 'Send 50 Tokens to My Star'...")

with tab2:
    st.markdown("### My FlashDeal Wallet")
    c1, c2 = st.columns(2)
    # Handling the 'token' aspect as requested
    c1.metric("Current Balance", "1,250 FTK", delta="Synced")
    c2.metric("Last Move", "-50 FTK", delta_color="inverse")
    st.divider()
    st.caption("All transactions are secured via Mutual Token encryption.")

with tab3:
    st.markdown("### Protection Layers")
    # Security options for customers
    st.checkbox("Face ID Biometrics", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Body Movement Matching", value=False)
    st.checkbox("Simple/Complex Secret Code", value=True)

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color: #7000FF;'>My FlashDeal Star</h2>", unsafe_allow_html=True)
st.sidebar.write("User: Hannibal85090")
st.sidebar.write("Device: Active 🟢")
st.sidebar.divider()
st.sidebar.info("Quality Level: High Premium")
