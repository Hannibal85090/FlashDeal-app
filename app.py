import streamlit as st

# FlashDeal - High Quality Parallel Project (Visual Update)
st.set_page_config(page_title="FlashDeal - My Star", page_icon="💫", layout="centered")

# CSS لتطابق الألوان والمؤثرات مع الصورة التي أرسلتها
st.markdown("""
    <style>
    /* الخلفية الداكنة العميقة */
    .stApp {
        background-color: #0B0E14;
        color: #FFFFFF;
    }
    
    /* العنوان الرئيسي بشعاع النيون */
    .main-title {
        color: #00FBFF;
        text-shadow: 0 0 20px #00FBFF, 0 0 30px #00FBFF;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 3em;
        margin-bottom: 0px;
    }
    
    .slogan {
        text-align: center;
        color: #B0B0B0;
        font-size: 1.2em;
        margin-bottom: 40px;
        letter-spacing: 3px;
    }

    /* لوحة أيقونات كبار السن وسهولة الاستخدام */
    .icon-bar {
        display: flex;
        justify-content: space-around;
        margin-bottom: 50px;
    }
    .card {
        background: rgba(20, 25, 35, 0.9);
        border: 2px solid #7000FF;
        border-radius: 20px;
        padding: 20px;
        width: 110px;
        text-align: center;
        transition: 0.4s;
    }
    .card:hover {
        border-color: #00FBFF;
        box-shadow: 0 0 25px rgba(0, 251, 255, 0.4);
        transform: scale(1.1);
    }
    .card-label {
        font-size: 0.7em;
        color: #00FBFF;
        margin-top: 10px;
        font-weight: bold;
    }

    /* أزرار النيون التفاعلية */
    .stButton>button {
        background: linear-gradient(135deg, #7000FF 0%, #00FBFF 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 15px;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(112, 0, 255, 0.3);
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px #00FBFF;
        color: #000;
    }

    /* تنسيق التبويبات */
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] {
        color: #B0B0B0;
        background-color: #1A1F2B;
        border-radius: 10px 10px 0 0;
        margin-right: 5px;
    }
    .stTabs [aria-selected="true"] {
        color: #00FBFF !important;
        border-bottom: 2px solid #00FBFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الواجهة العلوية ---
st.markdown("<h1 class='main-title'>⚡ FLASHDEAL</h1>", unsafe_allow_html=True)
st.markdown("<p class='slogan'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

# --- لوحة القيادة (Dashboard) كما في الصورة ---
st.markdown("""
    <div class="icon-bar">
        <div class="card">
            <div style="font-size: 2.5em;">🛡️</div>
            <div class="card-label">SECURITY</div>
        </div>
        <div class="card">
            <div style="font-size: 2.5em;">🕒</div>
            <div class="card-label">SPEED</div>
        </div>
        <div class="card">
            <div style="font-size: 2.5em;">👑</div>
            <div class="card-label">QUALITY</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- الأقسام الوظيفية ---
tab1, tab2, tab3 = st.tabs(["🎙️ Voice Control", "💰 Token Wallet", "🔒 Security Star"])

with tab1:
    st.markdown("### Smart Voice Command")
    st.info("System is listening... 'Talk' to start your deal.")
    if st.button("ACTIVATE MICROPHONE"):
        st.success("Listening... 'Transfer 100 Tokens' recognized.")

with tab2:
    st.markdown("### My FlashDeal Wallet")
    col1, col2 = st.columns(2)
    # معالجة جانب الـ Token كما طلبت
    col1.metric("Current Balance", "1,250 FTK", delta="Synced")
    col2.metric("Last Action", "-50 FTK", delta_color="inverse")
    st.divider()
    st.write("Recent Transactions: Secured via Mutual Token Protocol.")

with tab3:
    st.markdown("### Advanced Security Layers")
    # خيارات الحماية التي خططنا لها
    st.checkbox("Face ID Biometrics", value=True)
    st.checkbox("Mutual Token Verification", value=True)
    st.checkbox("Body Movement Matching", value=False)
    st.checkbox("Complex Secret Code", value=True)

# --- الشريط الجانبي (Sidebar) ---
st.sidebar.markdown("<h2 style='color: #00FBFF;'>My FlashDeal Star</h2>", unsafe_allow_html=True)
st.sidebar.write(f"User ID: Hannibal85090")
st.sidebar.write("Device Status: **Connected 🟢**")
st.sidebar.divider()
st.sidebar.info("Quality Mode: High Premium / Investor Ready")

if st.sidebar.button("System Reboot"):
    st.rerun()
