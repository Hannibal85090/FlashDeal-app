import streamlit as st
from streamlit_option_menu import option_menu
import cv2
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="FlashDeal - FinTech", layout="wide")

# القائمة الجانبية
with st.sidebar:
    selected = option_menu(
        menu_title="FlashDeal Navigation",
        options=["الرئيسية", "التحليل الحركي", "الإعدادات"],
        icons=["house", "activity", "gear"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "الرئيسية":
    st.title("🚀 FlashDeal: مستقبلك في التمويل التفاعلي")
    st.write("مرحباً بك في منصة FlashDeal المطورة.")

elif selected == "التحليل الحركي":
    st.title("📊 نظام التحليل الحركي")
    st.info("نظام الكشف عن الإيماءات يعمل الآن عبر OpenCV.")
    # كود تجريبي للكاميرا
    img_file_buffer = st.camera_input("قم بالتقاط صورة لاختبار النظام")
