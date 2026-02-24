import streamlit as st

# إعدادات الصفحة الاحترافية
st.set_page_config(page_title="FlashDeal Star - Pro", layout="wide", initial_sidebar_state="collapsed")

# هندسة التصميم (CSS) لإصلاح "المهزلة" البصرية
st.markdown("""
    <style>
    /* تصميم الخلفية الداكنة العميقة */
    .stApp { background-color: #05070a; color: #e0e0e0; }
    
    /* بطاقات الأقسام (Glassmorphism) */
    .section-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    /* شعار فلاش ديل المضيء */
    .brand-title {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px; font-weight: 900; letter-spacing: -1px;
    }
    
    .slogan { color: #888; font-size: 18px; margin-top: -15px; margin-bottom: 40px; }
    
    /* الموجة الصوتية والتوكن */
    .voice-glow { color: #00f2fe; text-shadow: 0 0 15px #00f2fe; font-size: 40px; text-align: center; }
    .token-value { color: #00f2fe; font-size: 35px; font-weight: bold; }
    
    /* الأزرار الاحترافية */
    .stButton>button {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        color: white; border: none; border-radius: 12px;
        padding: 10px 25px; transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر الرئيسي
st.markdown('<div class="brand-title">FlashDeal</div>', unsafe_allow_html=True)
st.markdown('<div class="slogan">Talk. Pay. Done.</div>', unsafe_allow_html=True)

# توزيع المحتوى بنظام الشبكة الاحترافي
col_main, col_side = st.columns([2, 1])

with col_main:
    # قسم الأوامر الصوتية (من الصورة 1 و 2)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🎙️ Smart Voice Command System (#42)")
    st.markdown('<div class="voice-glow">〰️〰️〰️ 🎙️ 〰️〰️〰️</div>', unsafe_allow_html=True)
    st.info("Listening for: 'Send 50 Tokens to Star Device'")
    st.markdown('</div>', unsafe_allow_html=True)

    # قسم المحفظة (معالجة الـ Token)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 💰 FlashDeal Token Wallet (#43)")
    c1, c2, c3 = st.columns(3)
    c1.markdown("**Current Balance**")
    c1.markdown('<div class="token-value">1,250 FTK</div>', unsafe_allow_html=True)
    c2.markdown("**Recent Deal**")
    c2.markdown('<div style="color:#ff4b4b; font-size:25px;">-50 FTK</div>', unsafe_allow_html=True)
    c3.button("Activate Wallet")
    st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    # نظام الحماية (المواصفات المطلوبة لـ My FlashDeal Star)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("### 🛡️ Security Star (#2)")
    st.checkbox("Face ID Verification", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Fingerprint Scanner", value=True)
    st.checkbox("Body Movement Compatibility")
    st.divider()
    st.write("🔐 **Security Code:** Dual Layer (Simple + Complex)")
    st.markdown('</div>', unsafe_allow_html=True)

    # رؤية المستثمر (من الصورة 1)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("📈 **Investor Vision 2027**")
    st.progress(65)
    st.caption("Targeting 320% Market Growth")
    st.markdown('</div>', unsafe_allow_html=True)

# التذييل الاحترافي
st.markdown("---")
footer_l, footer_r = st.columns(2)
footer_l.caption("Device: My FlashDeal Star (Connected) | Version 3.0")
if footer_r.button("Commit All Changes"):
    st.balloons()
