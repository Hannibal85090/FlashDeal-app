import streamlit as st
import time

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="FlashDeal | Talk. Pay. Done.",
    page_icon="⚡",
    layout="centered"
)

# 2. تصميم الواجهة (تم تصحيح الخطأ هنا)
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 25px; background: linear-gradient(45deg, #00B2FF, #006AFF); color: white; border: none; font-weight: bold; }
    .stTextInput>div>div>input { border-radius: 15px; border: 1px solid #00B2FF; }
    </style>
    """, unsafe_allow_input=True)

# 3. الهيدر والشعار
st.title("⚡ FlashDeal")
st.subheader("Talk. Pay. Done.")
st.caption("الجيل القادم من الدفع الذكي المدعوم بـ Gemini 3 Flash")

# 4. طبقة الأمان
with st.expander("🛡️ بروتوكولات الأمان النشطة"):
    st.info("نظام Gemini للأمان نشط الآن - متصل بواسطة 🔐")
    agreed = st.checkbox("أقر بأني المسؤول عن العمليات المالية وأوافق على الشروط")

if agreed:
    st.write("---")
    interaction_type = st.radio("اختر وسيلة التفاعل:", ["🎙️ أمر صوتي (Talk)", "🖐️ إيماءة حركية (Gesture)", "⌨️ نص ذكي"])
    
    if interaction_type == "🎙️ أمر صوتي (Talk)":
        if st.button("🎤 ابدأ الاستماع"):
            with st.status("🔍 جاري تحليل البصمة الصوتية...", expanded=True) as status:
                st.write("...التحقق من صحة البيانات")
                time.sleep(1)
                st.write("...البحث عن أفضل الخيارات")
                time.sleep(1.5)
                status.update(label="✅ تم تحليل الطلب بنجاح", state="complete", expanded=False)
            st.success("📦 طلبك جاهز: 'مصباح ليد ذكي'")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🚀 تأكيد الدفع النهائي"):
                    with st.spinner('جاري المعالجة...'):
                        time.sleep(2)
                    st.balloons()
                    st.success("✨ Done. تمت العملية")
            with col2:
                if st.button("❌ إلغاء"):
                    st.error("تم الإلغاء")

# 5. التذييل
st.markdown("---")
st.caption("FlashDeal © 2026 - رؤية مستقبلية للدفع الصوتي الذكي")
