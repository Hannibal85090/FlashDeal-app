import streamlit as st

# FlashDeal - My Star: Advanced Visual Identity
st.set_page_config(page_title="FlashDeal - My Star", page_icon="💫", layout="centered")

# Custom CSS for Cyber-Tech UI
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    h1 { color: #00FBFF !important; text-shadow: 0 0 15px #00FBFF; text-align: center; font-family: 'Inter', sans-serif; }
    .slogan { text-align: center; color: #7000FF; font-weight: bold; font-size: 1.2em; margin-bottom: 30px; }
    
    /* Icon Box Style */
    .icon-container { display: flex; justify-content: space-around; text-align: center; margin-bottom: 40px; }
    .icon-box { background: #1E2129; padding: 20px; border-radius: 15px; border: 1px solid #7000FF; width: 100px; }
    .icon-box:hover { box-shadow: 0 0 20px #7000FF; transform: translateY(-5px); transition: 0.3s; }
    .icon-label { font-size: 0.8em; margin-top: 10px; color: #00FBFF; }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00FBFF 0%, #7000FF 100%);
        color: white; border: none; border-radius: 12px; padding: 10px 25px; font-weight: bold; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("<h1>⚡ FLASHDEAL</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

# Visual Icons Section (As per your request for Seniors & Clarity)
st.markdown(f"""
    <div class="icon-container">
        <div class="icon-box">
            <div style="font-size: 2em;">🛡️</div>
            <div class="icon-label">SECURITY</div>
        </div>
        <div class="icon-box">
            <div style="font-size: 2em;">🕒</div>
            <div class="icon-label">SPEED</div>
        </div>
        <div class="icon-box">
            <div style="font-size: 2em;">👑</div>
            <div class="icon-label">QUALITY</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Tabs for Functions
tab1, tab2, tab3 = st.tabs(["🎙️ Voice Control", "💰 Token Wallet", "🔒 Security Star"])

with tab1:
    st.markdown("### Smart Voice Command")
    st.info("System is ready. Speak your intent.")
    if st.button("START VOICE RECORDING"):
        st.success("Analyzing Voice... 'Send 50 Tokens' recognized.")

with tab2:
    st.markdown("### FlashDeal Token Wallet")
    c1, c2 = st.columns(2)
    c1.metric("Balance", "1,250 FTK", "Synced")
    c2.metric("Last Action", "-50 FTK", delta_color="inverse")
    st.divider()
    st.write("Transaction History: Encrypted & Secure")

with tab3:
    st.markdown("### Security Settings")
    st.checkbox("Face ID Verification", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Biometric Compatibility", value=False)

# Sidebar
st.sidebar.markdown("<h2 style='color: #7000FF;'>FlashDeal Star</h2>", unsafe_allow_html=True)
st.sidebar.write("User: Hannibal85090")
st.sidebar.write("Status: Connected 🟢")
