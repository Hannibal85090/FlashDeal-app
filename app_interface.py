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
