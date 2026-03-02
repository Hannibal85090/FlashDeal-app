import streamlit as st
import time

# إعدادات الصفحة بجودة عالية
st.set_page_config(page_title="FlashDeal Star", page_icon="⭐", layout="centered")

# التنسيق البصري (CSS) للواجهة التفاعلية
st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .stButton>button { 
        border-radius: 50%; width: 120px; height: 120px; 
        background: radial-gradient(circle, #00d4ff 0%, #0056b3 100%);
        border: none; color: white; font-weight: bold; box-shadow: 0 0 20px #00d4ff;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 30px #00d4ff; }
    .slogan-text { font-size: 28px; font-weight: 800; color: #00d4ff; text-align: center; letter-spacing: 2px; }
    .star-status { position: absolute; top: -50px; right: 10px; color: #39ff14; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# الجزء العلوي: حالة My FlashDeal Star
col1, col2 = st.columns([4, 1])
with col2:
    st.markdown("<p class='star-status'>● My FlashDeal Star Connected</p>", unsafe_allow_html=True)

st.title("FlashDeal Project")
st.write("---")

# اختيار اللغة (للتوسع العالمي)
language = st.radio("Select Language / Choisir la langue", ("العربية", "Français"), horizontal=True)

# منطق التفاعل (Talk. Pay. Done.)
if st.button("Talk / Parler"):
    if language == "العربية":
        st.info("🎤 أهلاً بك في FlashDeal. 'Star' متصل. تحدث...")
    else:
        st.info("🎤 Bienvenue sur FlashDeal. 'Star' est connecté. Parlez...")
    
    time.sleep(1.5)
    st.success("✅ Order Captured: 1 Coffee / 1 Café")
    
    # محاكاة الأمان (Security & Token)
    st.write("### Security Check / التحقق الأمني")
    if st.checkbox("Verify with Fingerprint / بصمة الإصبع"):
        with st.spinner("Generating Mutual Token..."):
            time.sleep(1)
            token = f"TOKEN-{int(time.time()) % 10000:04d}"
            st.code(f"Mutual Token: {token}", language="bash")
            st.balloons()
            
            # الشعار النهائي
            if language == "العربية":
                st.markdown("<p class='slogan-text'>تحدث. ادفع. تم.</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p class='slogan-text'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

st.write("---")
st.caption("FlashDeal - High Quality Parallel Project 2026")
