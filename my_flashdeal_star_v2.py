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
import streamlit as st

# 1. إعدادات الصفحة والهوية البصرية
st.set_page_config(page_title="FlashDeal Star V2", layout="wide")

# تصميم CSS للمربعات (Modules) لجعلها متناسقة وجاهزة للإضافات
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .module-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #f0f2f6;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .status-online { color: #28a745; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. الترويسة (Talk. Pay. Done.)
st.title("⭐ My FlashDeal Star")
st.info("نظام الدفع الصوتي المدمج | نسخة التطوير v2.0")

# 3. نظام التوكن المتبادل (Mutual Token System)
with st.container():
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.subheader("🔐 الأمان (Security Token)")
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        token_val = st.text_input("أدخل كود التوكن لربط الجهاز:", type="password", placeholder="Token-XXXX")
    with col_t2:
        st.write("##")
        if st.button("ربط الآن"):
            st.success("تم الربط بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. الواجهة المفتوحة (المربعات الذكية)
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.subheader("🎤 Talk (الأوامر الصوتية)")
        st.write("حالة الميكروفون: <span class='status-online'>جاهز</span>", unsafe_allow_html=True)
        if st.button("ابدأ التحدث 🎙️"):
            st.warning("جاري الاستماع... (هذا الجزء سيرتبط بالـ API لاحقاً)")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.subheader("💳 Pay (محفظة الفلاش)")
        balance = 1250.50  # قيمة افتراضية
        st.write(f"الرصيد الحالي: **{balance} USD**")
        if st.button("دفع سريع بنقرة واحدة"):
            st.balloons()
            st.success("تم الدفع! Done.")
        st.markdown('</div>', unsafe_allow_html=True)

# 5. مربع الإضافات (بصمة الوجه وحركة الجسم)
st.markdown("### 🛠️ الإضافات المتطورة (Biometrics)")
expander = st.expander("فتح خيارات التحقق الحيوي")
with expander:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.checkbox("تفعيل بصمة الوجه")
    with c2:
        st.checkbox("تفعيل بصمة الإصبع")
    with c3:
        st.checkbox("تفعيل مستشعر حركة الجسم")

# 6. قسم التذييل والربط مع GitHub
st.sidebar.title("إدارة المشروع")
st.sidebar.write("✅ الملف مرتب وواضح")
st.sidebar.write("🔗 مرتبط بالمستودع: FlashDeal-app")

if st.sidebar.button("تحديث البيانات"):
    st.sidebar.snow()


