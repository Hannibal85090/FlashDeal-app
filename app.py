import streamlit as st
import hashlib
import time

# إعدادات الصفحة والهوية البصرية
st.set_page_config(
    page_title="FlashDeal - My Star",
    page_icon="⚡",
    layout="wide"
)

# تصحيح الخطأ البرمجي السابق وإضافة تنسيق احترافي
st.markdown("""
    <style>
    /* الخلفية العامة */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #e2e8f0;
    }
    
    /* تأثير الزجاج للبطاقات */
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .status-active { color: #00ffcc; font-weight: bold; }
    .status-pending { color: #ffcc00; font-weight: bold; }
    
    /* تنسيق صندوق التوكين */
    .token-display {
        background: #00ffcc;
        color: #0f172a;
        padding: 15px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر (الشعار والسلوجان)
st.title("⚡ FlashDeal")
st.caption("Talk. Pay. Done.")

# تقسيم الشاشة إلى أعمدة كما في الصورة الثالثة
col1, col2 = st.columns([2, 1])

with col1:
    # قسم الأوامر الصوتية (Smart Voice Command)
    st.markdown("""
        <div class="glass-card">
            <h3>🎙️ Smart Voice Command System</h3>
            <p style="color: #94a3b8;">Listening for your command...</p>
            <p><i>"Send 50 Tokens"</i></p>
            <div style="height: 50px; background: url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndmZ4bmZ4bmZ4/3o7TKDkDbIDJieKbK0/giphy.gif') center/contain no-repeat;"></div>
        </div>
    """, unsafe_allow_html=True)

    # قسم المحفظة (Token Wallet)
    st.markdown("""
        <div class="glass-card">
            <h3>💰 FlashDeal Token Wallet</h3>
            <table style="width:100%; text-align: left;">
                <tr>
                    <th>Current Balance</th>
                    <th>Last Transaction</th>
                </tr>
                <tr>
                    <td style="font-size: 24px;">1,250 FTK</td>
                    <td style="font-size: 24px; color: #ff4b4b;">-50 FTK</td>
                </tr>
            </table>
            <hr style="opacity: 0.1;">
            <p>Recent Activity: <span class="status-active">Safe & Encrypted</span></p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # قسم حماية نجم فلاش ديل (Protection Settings)
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("🛡️ My FlashDeal Star")
    
    face_id = st.checkbox("Face ID Verification", value=True)
    mutual_token = st.checkbox("Mutual Token Protocol", value=False)
    body_move = st.checkbox("Body Movement Compatibility", value=False)
    
    st.markdown('<hr style="opacity: 0.1;">', unsafe_allow_html=True)
    
    # زر توليد التوكين مع المنطق البرمجي
    if st.button("Activate & Generate Token", use_container_width=True):
        token_hash = hashlib.sha256(str(time.time()).encode()).hexdigest()[:10].upper()
        st.markdown(f'<div class="token-display">{token_hash}</div>', unsafe_allow_html=True)
        st.success("Mutual Token Synced Successfully")
    
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة (Footer)
st.markdown("""
    <div style="text-align: center; margin-top: 50px; opacity: 0.5;">
        <p>FlashDeal Star Device: <b>Connected</b></p>
        <p>User ID: Hannial85090</p>
    </div>
""", unsafe_allow_html=True)
