import streamlit as st
from streamlit_option_menu import option_menu
from flashdeal_app.security_engine import FlashDealSecurity

st.set_page_config(page_title="FlashDeal Star Portal", page_icon="⭐", layout="wide")

# 1. قائمة جانبية احترافية
with st.sidebar:
    selected = option_menu(
        menu_title="FlashDeal Star", 
        options=["الرئيسية", "المحرك الأمني", "المشروع الموازي", "سجل الأعتبار"],
        icons=["house", "shield-lock", "rocket-takeoff", "journal-text"],
        menu_icon="stars",
        default_index=0,
    )

security = FlashDealSecurity()

# 2. محتوى الصفحات
if selected == "الرئيسية":
    st.title("⭐ My FlashDeal Star")
    st.subheader("Talk. Pay. Done.")
    st.write("مرحباً بك في بوابة التحكم الذكية الخاصة بـ FlashDeal.")

elif selected == "المحرك الأمني":
    st.header("🛡️ نظام التحقق من التوكن")
    token = st.text_input("أدخل التوكن النشط", type="password")
    if st.button("تحقق الآن"):
        if security.verify_token(token):
            st.success("✅ تم التوثيق بنجاح.")
        else:
            st.error("❌ التوكن غير صحيح.")

elif selected == "المشروع الموازي":
    st.header("🚀 High-Quality Parallel Project")
    st.info("هذا القسم مخصص للميزات المتقدمة: بصمة الحركة، التعرف على الوجه، وشريحة SIM الخاصة.")
    st.button("طلب تمويل للمشروع الموازي", disabled=True)

elif selected == "سجل الأعتبار":
    st.header("📝 سجل الدروس المستفادة")
    st.warning("درس تقني: تم حل مشكلة Indentation Error وضبط مسارات GitHub بنجاح.")
