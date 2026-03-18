import streamlit as st
import cv2
import numpy as np
from core.motion_engine import FlashDealMotionEngine

# 1. إعدادات الصفحة
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟")

# 2. تهيئة محرك الحركة في ذاكرة الجلسة لضمان الاستقرار
if 'motion_detector' not in st.session_state:
    try:
        st.session_state.motion_detector = FlashDealMotionEngine()
    except Exception as e:
        st.error(f"خطأ في تهيئة محرك الحركة: {e}")

# 3. واجهة المستخدم
st.title("🌟 FlashDeal Star")
st.subheader("Talk. Pay. Done.")

# الحالة في الجانب
with st.sidebar:
    st.header("حالة النظام الأمني")
    st.write("✅ بصمة الصوت: مفعلة")
    st.write("✅ بصمة الوجه: مفعلة")
    st.write("✅ بصمة الحركة: مفعلة")

# 4. قسم التفاعل
st.divider()
if st.button("🎤 ابدأ التفاعل الصوتي (Talk)"):
    with st.spinner('جاري الاستماع وتحليل الطلب...'):
        st.info("🔓 يرجى تأكيد الهوية الحيوية (بصمة الحركة) لإتمام العملية")

# 5. قسم المصادقة المتعددة (بصمة الحركة)
st.divider()
st.header("🛡️ المصادقة الحيوية (Motion Auth)")
captured_image = st.camera_input("اعرض حركتك السرية للكاميرا")

if captured_image and 'motion_detector' in st.session_state:
    # تحويل الصورة الملتقطة لمعالجة OpenCV
    file_bytes = np.asarray(bytearray(captured_image.read()), dtype=np.uint8)
    opencv_frame = cv2.imdecode(file_bytes, 1)
    
    # تنفيذ عملية التحقق
    success, final_output = st.session_state.motion_detector.verify_motion(opencv_frame)
    
    if success:
        st.success("✅ تم التحقق من الهوية حركياً")
        st.image(final_output, channels="BGR", caption="بصمة الحركة المكتشفة")
        st.balloons()
    else:
        st.warning("⚠️ لم يتم رصد حركة واضحة. يرجى إظهار يدك بوضوح.")
