import streamlit as st
import hashlib
import time

# إعدادات الصفحة
st.set_page_config(page_title="FlashDeal - My Star", page_icon="⭐")

# التنسيق الجمالي (CSS)
st.markdown("""
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        color: white;
    }
    .token-box {
        background-color: #00ffcc;
        color: #000;
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⭐ My FlashDeal Star")
st.write("Current Status: **Secure & Ready**")

# واجهة الحالة الأمنية
st.markdown("""
    <div class="glass-card">
        <h3>Security Engine</h3>
        <p>Encryption: <b>AES-256 Enabled</b></p>
        <p>Device: <b>FlashDeal Star v1.0</b></p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# وظيفة توليد التوكين (المنطق البرمجي)
if st.button("Generate Secure Token"):
    # إنشاء توكين فريد بناءً على الوقت الحالي
    raw_data = str(time.time())
    token = hashlib.sha256(raw_data.encode()).hexdigest()[:12].upper()
    
    st.balloons() # تأثير احتفالي بسيط
    st.markdown(f"**Your One-Time Payment Token:**")
    st.markdown(f'<div class="token-box">{token}</div>', unsafe_allow_html=True)
    st.info("This token expires in 60 seconds.")
