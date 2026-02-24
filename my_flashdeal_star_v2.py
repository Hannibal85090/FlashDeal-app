import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="My FlashDeal Star V2", layout="wide")

# تصميم الواجهة الاحترافي
st.markdown("""
    <style>
    .main-header { font-size: 2.5rem; color: #FFD700; text-align: center; background: #1e1e1e; padding: 20px; border-radius: 10px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #FF4B4B; color: white; height: 3em; }
    .feature-card { background-color: #f0f2f6; padding: 20px; border-radius: 15px; border: 1px solid #ddd; height: 250px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-header">⭐ MY FLASHDEAL STAR <br> <small>Talk. Pay. Done.</small></div>', unsafe_allow_html=True)
st.write("##")

# قسم الأمان والتوكن
with st.expander("🔐 نظام التوكن المتبادل (Security Token)"):
    st.info("هذا المربع مخصص لتأمين العمليات بين المستخدم والجهاز.")
    token = st.text_input("أدخل كود التوكن:", type="password")

# نظام المربعات المفتوح للإضافات
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("🎤 Talk (صوتي)")
    st.write("التحكم عبر الأوامر الصوتية المباشرة.")
    if st.button("تفعيل الميكروفون"):
        st.write("جاري الاستماع لطلبك...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("💳 Pay (دفع)")
    st.write("تنفيذ عمليات الدفع الفوري.")
    amount = st.number_input("المبلغ", min_value=0.0)
    if st.button("تأكيد الدفع"):
        st.success("تمت العملية بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("🛡️ Bio (بصمة)")
    st.write("إضافات الأمان الحيوي.")
    st.selectbox("نوع التحقق:", ["بصمة وجه", "بصمة إصبع", "حركة جسم"])
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة للمستقبل
st.divider()
st.sidebar.title("إعدادات V2")
st.sidebar.success("الواجهة مفتوحة للإضافات")
st.sidebar.info("هذا الملف يعمل بالتوازي مع النسخة القديمة.")

