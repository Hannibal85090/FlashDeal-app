import streamlit as st
from star_security_core import FlashDealStarSecurity # هذا السطر يستدعي "المخ" الأمني

# إعدادات واجهة نجمتي فلاش ديل
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="centered")

# تشغيل النظام الأمني
security = FlashDealStarSecurity()

# تصميم الواجهة الرئيسية
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🌟 My FlashDeal Star</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

st.divider()

# منطقة فحص الأمان (الدرع الذكي)
st.subheader("🛡️ درع الأمان الذكي (Security Shield)")
st.info("قم بلصق أي رسالة مشبوهة أو رابط لفحصه قبل إتمام العملية.")

user_input = st.text_area("رسالة الدفع أو المحتوى:", placeholder="ضع النص هنا...")

if st.button("تفعيل فحص FlashDeal"):
    if user_input:
        is_safe, message = security.validate_content(user_input)
        
        if is_safe:
            st.success(f"✅ محتوى آمن: {message}")
            # توليد التوكن كإجراء أمني إضافي
            token = security.generate_secure_token(user_input[:5])
            st.code(f"Generated Security Token: {token}", language="bash")
        else:
            st.error(f"⚠️ تحذير أمني: {message}")
            st.warning("تم حظر العملية تلقائياً لحمايتك.")
    else:
        st.write("الرجاء إدخال بيانات لتحليلها.")

st.divider()
st.caption("FlashDeal High-Quality Project | 2026 Security Core")
