import streamlit as st

# 1. إعدادات الهوية البصرية (Talk. Pay. Done.)
st.set_page_config(page_title="My FlashDeal Star V2", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 15px; height: 3.5em; background: #000; color: #fff; }
    .module-card { padding: 20px; border-radius: 15px; background-color: #f8f9fa; border: 1px solid #ddd; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⭐ My FlashDeal Star (النسخة الموازية)")
st.caption("الشعار: Talk. Pay. Done.")

# 2. مربع التوكن المتبادل (Mutual Token) - الخطوة الأولى للأمان
with st.container():
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🔐 نظام التوكن المتبادل")
    t_col1, t_col2 = st.columns([3, 1])
    with t_col1:
        st.text_input("أدخل التوكن السري للمزامنة:", type="password", key="sync_token")
    with t_col2:
        st.write("##")
        if st.button("تفعيل المزامنة"):
            st.success("تم الربط بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. نظام المربعات المفتوحة (الميزات الرئيسية)
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.subheader("🎤 مربع Talk")
        if st.button("تسجيل أمر صوتي الجديد"):
            st.write("جاري المعالجة بنظام عالي الجودة...")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.subheader("💳 مربع Pay")
        st.number_input("تحديد المبلغ المستحق", min_value=0.0)
        if st.button("تنفيذ الدفع"):
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

# 4. المربعات الجديدة (بصمة الوجه وجهاز النجمة)
st.divider()
st.subheader("🚀 الإضافات الذكية (New Add-ons)")

with st.expander("📸 تفعيل مربع بصمة الوجه (Biometrics)"):
    st.camera_input("التقط صورة للتحقق الحيوي")

with st.container():
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🔑 جهاز My FlashDeal Star")
    st.write("حالة الجهاز: متصل بالقرب من السيارة/المستخدم")
    st.slider("نطاق العمل (Range M)", 1, 10, 3)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. جانب الإدارة (Sidebar)
st.sidebar.title("إدارة الجودة")
st.sidebar.info("هذا المشروع يطبق معايير الجودة العالية Parallel Project")
