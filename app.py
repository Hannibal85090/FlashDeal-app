import streamlit as st

# إعدادات لمنع التداخل وضمان سلاسة العرض على الموبايل والكمبيوتر
st.set_page_config(page_title="FlashDeal Star Premium", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: white; }
    .main-header { font-size: 35px; font-weight: bold; color: #58a6ff; text-align: center; }
    .slogan { text-align: center; color: #8b949e; margin-bottom: 30px; }
    .card {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .status-active { color: #3fb950; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# الهوية البصرية
st.markdown('<div class="main-header">⚡ FlashDeal Star</div>', unsafe_allow_html=True)
st.markdown('<div class="slogan">Talk. Pay. Done.</div>', unsafe_allow_html=True)

# تقسيم الواجهة بشكل طولي (مناسب للعرض الذي ظهر في صورك)
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎙️ نظام التحكم الصوتي الذكي")
    st.write("الحالة: <span class="status-active">متصل وجاهز</span>", unsafe_allow_html=True)
    st.text_input("الأمر الصوتي المكتشف:", value="Send 50 Tokens", disabled=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💰 محفظة التوكن (FTK)")
    col_t1, col_t2 = st.columns(2)
    col_t1.metric("الرصيد الحالي", "1,250 FTK")
    col_t2.metric("آخر عملية", "-50 FTK", delta_color="inverse")
    if st.button("تنشيط المحفظة", use_container_width=True):
        st.success("تم التزامن بنجاح")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🛡️ حماية نجم فلاش ديل")
    st.checkbox("التحقق من الوجه (Face ID)", value=True)
    st.checkbox("التحقق من بصمة الإصبع", value=True)
    st.checkbox("بروتوكول التوكن المتبادل", value=True)
    st.checkbox("توافق حركة الجسم")
    st.info("نظام الكود السري: مفعل (بسيط + معقد)")
    st.markdown('</div>', unsafe_allow_html=True)

# التذييل (Footer)
st.divider()
st.caption("FlashDeal: Parallel High-Quality Project | v3.0")
