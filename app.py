import streamlit as st

# إعداد الصفحة لتكون عريضة واحترافية (Dark Theme)
st.set_page_config(page_title="FlashDeal Star - Pro", layout="wide")

# تخصيص التصميم (CSS) ليعكس طابع الصور (Neon Blue & Dark Grey)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background-color: #0e1117; }
    .card {
        background-color: #1a1c24;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .token-val { color: #00d4ff; font-size: 32px; font-weight: bold; }
    .voice-wave { color: #00d4ff; text-align: center; font-size: 50px; margin: 20px 0; }
    .sidebar .sidebar-content { background-color: #161b22; }
    h1, h2, h3 { color: #ffffff !important; }
    .stButton>button {
        background-image: linear-gradient(to right, #00d4ff, #0055ff);
        color: white; border: none; border-radius: 8px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# الشريط الجانبي - القائمة والتحكم
with st.sidebar:
    st.image("https://via.placeholder.com/150x50/0e1117/00d4ff?text=FlashDeal", width=150)
    st.markdown("### 🛠️ Settings")
    st.caption("User: Hannibal85090")
    st.info("FlashDeal Star Device: Connected")
    st.divider()
    st.button("FlashDeal-app")
    st.button("App.py")
    st.button("Settings")

# الواجهة الرئيسية - الهوية
col_logo, col_empty = st.columns([1, 2])
with col_logo:
    st.title("⚡ FlashDeal")
    st.markdown("#### *Talk. Pay. Done.*")

# توزيع الأقسام كما في الصورة الثانية (الدمج الأفضل)
tab1, tab2, tab3 = st.tabs(["🎙️ Voice Command", "💰 Token Wallet", "🔒 Security Star"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### #42 Smart Voice Command System")
    st.markdown('<div class="voice-wave">〰️〰️〰️🎙️〰️〰️〰️</div>', unsafe_allow_html=True)
    st.write("Listening for your command...")
    st.code('"Send 50 Tokens"', language="text")
    st.markdown('</div>', unsafe_allow_html=True)

col_mid_left, col_mid_right = st.columns(2)

with col_mid_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### #43 FlashDeal Token Wallet")
    c1, c2 = st.columns(2)
    c1.metric("Current Balance", "1,250 FTK", "Synced")
    c2.metric("Last Transaction", "-50 FTK", "Inverse", delta_color="normal")
    st.markdown("**Recent Activity:** Safe & Encrypted")
    if st.button("Activate Button"):
        st.toast("System Activated")
    st.markdown('</div>', unsafe_allow_html=True)

with col_mid_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### #2 My FlashDeal Star Protection")
    st.checkbox("Face ID Verification", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Control Protocol")
    st.checkbox("Body Movement Compatibility")
    st.markdown('<p style="color:gray;">نظام الكود السري: مفعل (بسيط + معقد)</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# القسم السفلي - التحديثات
st.markdown('<div class="card">', unsafe_allow_html=True)
if st.button("Commit changes"):
    st.success("Configuration Updated for FlashDeal Star")
st.caption("Transform: 3.00.1.20 | Parallel High-Quality Version")
st.markdown('</div>', unsafe_allow_html=True)
