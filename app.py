import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="FlashDeal - Talk. Pay. Done.", page_icon="⚡")

# تنسيق مخصص (CSS) لتحسين المظهر
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #007bff; color: white; }
    .title-text { text-align: center; color: #1E3A8A; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>⚡ FlashDeal</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Talk. Pay. Done.</h3>", unsafe_allow_html=True)

# --- تصنيف الأجزاء حسب الاتفاق ---
# 1. قسم الواجهة الصوتية (Voice Interface)
st.subheader("🎙️ تحدث لإتمام الصفقة")
audio_input = st.button("اضغط للتحدث (Voice Command)")

if audio_input:
    with st.spinner("جاري تحليل صوتك..."):
        time.sleep(2) # محاكاة المعالجة
        st.success("تم التعرف على الطلب: 'شراء منتج X ودفع 50 ريال'")

# 2. قسم الدفع السريع (Practical Steps)
st.divider()
st.subheader("💳 الدفع الفوري")
col1, col2 = st.columns(2)
with col1:
    st.text_input("المبلغ", placeholder="0.00")
with col2:
    st.selectbox("وسيلة الدفع", ["Apple Pay", "STC Pay", "Credit Card"])

if st.button("إتمام العملية"):
    st.balloons()
    st.info("تمت العملية بنجاح! Done.")

# --- التوثيق والحفظ (للأرشفة الخاصة بك) ---
st.sidebar.title("🗂️ تصنيفات المشروع")
st.sidebar.info("""
- **التصنيف:** البرمجة / الخطوات العملية
- **المشروع:** FlashDeal
- **الحالة:** تطوير الواجهة (Streamlit)
""")
