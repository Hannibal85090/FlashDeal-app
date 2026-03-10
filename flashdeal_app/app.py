import streamlit as st
from star_security_core import MyFlashDealStarSecurity

st.title("⭐ My FlashDeal Star")
st.markdown("### High-Quality Parallel Track")

security = MyFlashDealStarSecurity()

# واجهة تفاعلية لاستعراض القوة الأمنية
with st.expander("🛡️ بوابة التحقق الأمنية"):
    token = st.text_input("أدخل رمز النجمة:", type="password")
    if st.button("تفعيل النجمة"):
        if security.verify_transaction(token):
            st.success("✅ تم الاتصال بنجاح. Talk. Pay. Done.")
        else:
            st.error("❌ الرمز غير متوافق مع معايير النجمة.")
