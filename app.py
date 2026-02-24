import streamlit as st

# الإعدادات العامة للواجهة
st.set_page_config(page_title="My FlashDeal Star", layout="centered")

# التنسيق البصري (CSS)
st.markdown("""
    <style>
    .main-title { color: #FFD700; text-align: center; font-size: 40px; font-weight: bold; }
    .slogan { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
    .token-box { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# الهوية البصرية والشعار
st.markdown('<div class="main-title">✨ My FlashDeal Star</div>', unsafe_allow_html=True)
st.markdown('<div class="slogan">تحدث. ادفع. تم.</div>', unsafe_allow_html=True)

# قسم الحماية (المعايير الأساسية)
with st.sidebar:
    st.header("🛡️ حماية نجم فلاش ديل")
    face_id = st.checkbox("Face ID Verification", value=True)
    fingerprint = st.checkbox("Fingerprint Scanner", value=True)
    body_mov = st.checkbox("Body Movement Compatibility")
    mutual_token = st.checkbox("Mutual Token Protocol", value=True)
    
    st.info("نظام الكود السري: مفعل (بسيط + معقد)")

# القسم الرئيسي: محفظة التوكن ورؤية المستثمر
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 رؤية المستثمر 2027")
    st.write("Targeting 320% growth through 'My FlashDeal Star' hardware.")
    st.progress(65)

with col2:
    st.markdown('<div class="token-box">', unsafe_allow_html=True)
    st.write("**Token Wallet**")
    st.subheader("1,250 FTK")
    st.caption("↓ 50 FTK (Recent Deal)")
    st.markdown('</div>', unsafe_allow_html=True)

# طلب النسخة التجريبية
if st.button("(Request Demo) طلب نسخة تجريبية", use_container_width=True):
    st.success("تم إرسال طلبك بنجاح ضمن مشروع فلاش ديل الموازي.")

# التذييل
st.markdown("---")
st.caption("FlashDeal: Parallel High-Quality Project | Version 2.0")
