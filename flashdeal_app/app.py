import streamlit as st
from streamlit_option_menu import option_menu
# التعديل هنا: استدعاء مباشر بدون اسم المجلد لتجنب خطأ ModuleNotFoundError
try:
    from security_engine import FlashDealSecurity
except ImportError:
    st.error("لم يتم العثور على ملف security_engine.py في المجلد الرئيسي.")

st.set_page_config(page_title="FlashDeal Star Portal", page_icon="⭐", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title="FlashDeal Star", 
        options=["الرئيسية", "المحرك الأمني", "المشروع الموازي", "سجل الأعتبار"],
        icons=["house", "shield-lock", "rocket-takeoff", "journal-text"],
        menu_icon="stars",
        default_index=0,
    )

security = FlashDealSecurity()

if selected == "الرئيسية":
    st.title("⭐ My FlashDeal Star")
    st.subheader("Talk. Pay. Done.")
    st.write("مرحباً بك في بوابة التحكم الذكية.")

elif selected == "المحرك الأمني":
    st.header("🛡️ نظام التحقق")
    token = st.text_input("أدخل التوكن (مثال: FLASH_2026)", type="password")
    if st.button("تحقق الآن"):
        if security.verify_token(token):
            st.success("✅ تم التوثيق بنجاح.")
        else:
            st.error("❌ التوكن غير صحيح.")

elif selected == "المشروع الموازي":
    st.header("🚀 High-Quality Track")
    st.info("هذا القسم مخصص للميزات المتقدمة مثل بصمة الحركة.")

elif selected == "سجل الأعتبار":
    st.header("📝 سجل الدروس المستفادة")
    st.warning("درس تقني: تم تبسيط المسارات (Path simplification) لحل مشكلة ModuleNotFoundError.")
