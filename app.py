import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

# --- 1. إعدادات الهوية والعداد الحي ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# عداد الوقت والتاريخ (أعلى الشاشة)
now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")

st.markdown(f"""
    <div style='text-align: right; color: #2E8B57; font-family: sans-serif; font-weight: bold;'>
        {dt_string}
    </div>
    """, unsafe_allow_html=True)

# --- 2. محرك الجماليات (حركة البرق والنجمة) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%); }
    
    /* أنيميشن البرق والنجمة المتداخل */
    @keyframes flash-star {
        0% { opacity: 0.4; transform: scale(0.9); }
        50% { opacity: 1; transform: scale(1.1); color: #FFD700; text-shadow: 0 0 20px #FFF700; }
        100% { opacity: 0.4; transform: scale(0.9); }
    }
    .main-logo { font-size: 50px; text-align: center; animation: flash-star 2s infinite; font-weight: bold; }
    
    /* تنسيق الحاوية الأمنة */
    .secure-box {
        background: white; border-radius: 25px; padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1); border: 2px solid #2E8B57;
        max-width: 500px; margin: auto; text-align: center;
    }
    .price-tag { font-size: 30px; font-weight: bold; color: #2E8B57; margin: 15px 0; }
    </style>
    <div class='main-logo'>⚡ ⭐ ⚡</div>
    <h1 style='text-align: center; color: #1E1E1E;'>My FlashDeal Star</h1>
    <p style='text-align: center; font-style: italic;'>Talk. Pay. Done.</p>
    """, unsafe_allow_html=True)

# --- 3. القائمة المتكاملة (Navigation) ---
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "المساعدة"],
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "info-circle"],
    default_index=2,
    orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# --- 4. محتوى الشاشات (تغطية كل الجوانب) ---

if selected == "إبرام الصفقة":
    st.markdown("<div class='secure-box'>", unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x300/87CEEB/FFFFFF?text=Premium+Product", use_container_width=True)
    st.subheader("Wireless Headphones")
    st.write("⭐⭐⭐⭐⭐ (4.9)")
    st.markdown("<div class='price-tag'>$99.99 <span style='color:gray; text-decoration:line-through; font-size:18px;'>$199.99</span></div>", unsafe_allow_html=True)
    
    if st.button("BUY NOW / إتمام الصفقة"):
        with st.spinner("جاري التحقق الآمن..."):
            time.sleep(1)
            st.balloons()
            st.success("تمت الصفقة بنجاح! Talk. Pay. Done.")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "الأمان":
    st.header("🛡️ Security Center")
    st.write("ملأ الفراغ بتخطيط أمني حكيم:")
    st.checkbox("تفعيل بصمة الوجه والبيومتري", value=True)
    st.checkbox("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.info("نظام الأمان مربوط بمفتاح FlashDeal الذكي.")

elif selected == "الوكيل الذكي":
    st.header("🤖 FlashDeal AI Agent")
    st.write("التحكم عبر الصوت، النص، أو الإيماءة:")
    st.selectbox("اختر وضع التحكم", ["الصوت", "الإيماءة", "النص"])
    st.button("اختبار استجابة الوكيل")

elif selected == "سجل الصفقات":
    st.header("📜 سجل العمليات")
    st.write(f"آخر تحديث: {dt_string}")
    st.table({"التاريخ": [now.strftime("%Y-%m-%d")], "العملية": ["إطلاق MVP"], "الحالة": ["ناجح ✅"]})

elif selected == "المساعدة":
    st.header("🆘 مركز الدعم")
    st.write("نحن معك في كل خطوة لضمان صفقة آمنة.")
