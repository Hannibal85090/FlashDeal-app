import streamlit as st
from core.main_orchestrator import FlashDealOrchestrator

# إعدادات الصفحة
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟")

st.title("🌟 FlashDeal Star")
st.subheader("Talk. Pay. Done.")

# إنشاء نسخة من المنسق العام
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = FlashDealOrchestrator()

# واجهة التفاعل
st.write("---")
st.info("اضغط على الزر لمحاكاة الأمر الصوتي والدفع الآمن")

if st.button("🎤 ابدأ التفاعل الصوتي (Talk)"):
    with st.spinner('جاري الاستماع وتحليل الطلب...'):
        # استدعاء دورة العمل الكاملة
        # ملحوظة: في التطبيق الحقيقي سنقسم الخطوات لعرضها تدريجياً
        st.success("✅ تم استقبال الأمر: Pay 50 DT to Store A")
        
        st.warning("🔒 يرجى تأكيد الهوية الحيوية (صوت + وجه + حركة)")
        
        # محاكاة النجاح
        result = st.session_state.orchestrator.run_transaction_flow()
        
        if result:
            st.balloons()
            st.success("✨ العملية اكتملت بنجاح! Pay. Done.")
        else:
            st.error("❌ فشلت عملية التحقق.")

# عرض حالة الأمان في الجانب
st.sidebar.header("حالة النظام الأمني")
st.sidebar.write("✅ بصمة الصوت: مفعلة")
st.sidebar.write("✅ بصمة الوجه: مفعلة")
st.sidebar.write("✅ بصمة الحركة: مفعلة")
import streamlit as st
import numpy as np
import cv2
from core.motion_engine import FlashDealMotionEngine

# استدعاء المحرك الذكي
motion_detector = FlashDealMotionEngine()

st.divider()
st.header("🛂 Multi-Modal Authentication")
st.info("قم بتأكيد هويتك الآن عبر 'بصمة الحركة' (Sign Auth)")

# تشغيل الكاميرا داخل المتصفح
captured_image = st.camera_input("اعرض حركتك السرية للكاميرا")

if captured_image:
    # تحويل الصورة الملتقطة لصيغة معالجة OpenCV
    file_bytes = np.asarray(bytearray(captured_image.read()), dtype=np.uint8)
    opencv_frame = cv2.imdecode(file_bytes, 1)
    
    # التحقق من بصمة الحركة ورسم النقاط
    success, final_output = motion_detector.verify_motion(opencv_frame)
    
    if success:
        st.success("✅ تم التحقق من الهوية حركياً! Identity Secured.")
        st.image(final_output, channels="BGR", caption="FlashDeal Motion Signature Detected")
    else:
        st.warning("⚠️ لم يتم رصد حركة واضحة. يرجى إظهار يدك بوضوح أمام الكاميرا.")
