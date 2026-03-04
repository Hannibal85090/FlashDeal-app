import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

# --- 1. إعدادات الهوية والتوقيت الحقيقي ---
st.set_page_config(page_title="FlashDeal Star MVP", page_icon="⭐", layout="wide")

# جلب التاريخ الحالي (اليوم 04 مارس 2026)
current_now = datetime.datetime.now()
formatted_date = current_now.strftime("%A, %d %B %Y")
formatted_time = current_now.strftime("%H:%M:%S")

st.markdown(f"""
    <div style='text-align: right; color: #2E8B57; font-weight: bold; padding: 10px;'>
        📅 {formatted_date} | 🕒 {formatted_time}
    </div>
    """, unsafe_allow_html=True)

# --- 2. جماليات البرق والنجمة (Visual Motivation) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #87CEEB 0%, #E0F7FA 50%, #FFFFFF 100%); }
    @keyframes lightning { 0% { opacity: 0.3; } 50% { opacity: 1; color: #FFD700; } 100% { opacity: 0.3; } }
    .star-flash { font-size: 45px; text-align: center; animation: lightning 1.5s infinite; font-weight: bold; margin-bottom: 20px; }
    .secure-card { background: rgba(255,255,255,0.9); border-radius: 20px; padding: 25px; border: 2px solid #2E8B57; box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin: auto; max-width: 600px; }
    </style>
    <div class='star-flash'>⚡ My FlashDeal Star ⭐</div>
    """, unsafe_allow_html=True)

# --- 3. نظام التنقل الشامل ---
selected = option_menu(
    menu_title=None,
    options=["الإعدادات", "سجل المعاملات", "إبرام الصفقة", "الوكيل الذكي", "مركز المساعدة"],
    icons=["shield-lock", "clock-history", "stars", "robot", "patch-question"],
    default_index=2,
    orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# --- 4. الشاشات المتكاملة ---
if selected == "إبرام الصفقة":
    st.markdown("<div class='secure-card'>", unsafe_allow_html=True)
    st.image("https://via.placeholder.com/400x300/87CEEB/FFFFFF?text=Premium+Deal", use_container_width=True)
    st.markdown("<h2 style='text-align: center;'>Wireless Headphones</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #FFD700; text-align: center; font-size: 22px;'>⭐⭐⭐⭐⭐</p>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 28px; font-weight: bold; color: #2E8B57;'>$99.99 <span style='color: #888; text-decoration: line-through; font-size: 18px;'>$199.99</span></div>", unsafe_allow_html=True)
    
    if st.button("Talk. Pay. Done. ✅"):
        with st.spinner("جاري تأمين الصفقة بيومترياً..."):
            time.sleep(1.5)
            st.balloons()
            st.success(f"تمت الصفقة بنجاح في {formatted_time}!")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "سجل المعاملات":
    st.markdown(f"### 📜 سجل الإنجازات (محدث: {formatted_date})")
    # السجل يبدأ من اليوم ويتطلع للمستقبل
    st.write(f"✅ **{formatted_date}**: تم إطلاق النسخة المتكاملة مع عداد الوقت الحقيقي.")
    st.write("🚀 **الخطوة القادمة**: ربط نظام الـ SIM Card ووسائل الدفع المتطورة [cite: 2026-02-20].")

elif selected == "الإعدادات":
    st.markdown("### 🛡️ مركز الأمان (Security Hub)")
    st.toggle("تفعيل بصمة الوجه (Face ID)", value=True)
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True) [cite: 2026-02-20]

elif selected == "الوكيل الذكي":
    st.markdown("### 🤖 الوكيل الذكي (Smart Agent)")
    st.info("الوكيل جاهز لاستقبال الأوامر الصوتية أو النصية [cite: 2026-02-21].")
    st.text_input("أدخل أمرك للوكيل...")

elif selected == "مركز المساعدة":
    st.markdown("### 🆘 الدعم الفني")
    st.write("فريق FlashDeal Star في خدمتك لضمان أمان صفقاتك.")
