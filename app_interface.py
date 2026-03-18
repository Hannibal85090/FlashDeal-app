import streamlit as st
import cv2
import numpy as np
from core.main_orchestrator import FlashDealOrchestrator
from core.motion_engine import FlashDealMotionEngine

# إعدادات الصفحة
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟")

st.title("🌟 FlashDeal Star")
st.subheader("Talk. Pay. Done.")

# تهيئة المحركات في حالة الجلسة (Session State)
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = FlashDealOrchestrator()
if 'motion_detector' not in st.session_state:
    st.session_state.motion_detector = FlashDealMotionEngine()

# واجهة التفاعل الصوتي (محاكاة)
st.divider()
if st.button("🎤 ابدأ التفاعل الصوتي (Talk)"):
    with st.spinner('جاري الاستماع وتحليل الطلب...'):
        st.success("✅ تم استقبال الأمر: Pay 50 DT to Store A")
        st.warning("🔒 يرجى تأكيد الهوية الحيوية (صوت + وجه + حركة)")
        
        result = st.session_state.orchestrator.run_transaction_flow()
        if result:
            st.balloons()
            st.success("✨ العملية اكتملت بنجاح! Pay. Done.")
        else:
            st.error("❌ فشلت عملية التحقق")

# حالة النظام في الجانب
st.sidebar.header("حالة النظام الأمني")
st.sidebar.write("✅ بصمة الصوت: مفعلة")
st.sidebar.write("✅ بصمة الوجه: مفعلة")
st.sidebar.write("✅ بصمة الحركة: مفعلة")

# قسم المصادقة المتعددة (بصمة الحركة)
st.divider()
st.header("🛡️ Multi-Modal Authentication")
st.info("(Sign Auth) قم بتأكيد هويتك الآن عبر بصمة الحركة")

captured_image = st.camera_input("اعرض حركتك السرية للكاميرا")

if captured_image:
    # معالجة الصورة الملتقطة
    file_bytes = np.asarray(bytearray(captured_image.read()), dtype=np.uint8)
    opencv_frame = cv2.imdecode(file_bytes, 1)
    
    # التحقق عبر المحرك
    success, final_output = st.session_state.motion_detector.verify_motion(opencv_frame)
    
    if success:
        st.success("✅ Identity Secured: تم التحقق من الهوية حركياً")
        st.image(final_output, channels="BGR", caption="FlashDeal Motion Signature Detected")
    else:
        st.warning("⚠️ لم يتم رصد حركة واضحة. يرجى إظهار يدك بوضوح أمام الكاميرا.")
