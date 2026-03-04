import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

# --- 1. الإعدادات والعداد ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")
st.markdown(f"<div style='text-align: right; color: #2E8B57; font-weight: bold;'>{dt_string}</div>", unsafe_allow_html=True)

# --- 2. التصميم (البرق والنجمة والموجات) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%); min-height: 100vh; }
    @keyframes flash-star { 0%, 100% { opacity: 0.5; transform: scale(1); } 50% { opacity: 1; transform: scale(1.1); color: #FFD700; } }
    .main-logo { font-size: 50px; text-align: center; animation: flash-star 2s infinite; font-weight: bold; }
    .wave-box { background: #1E1E1E; border-radius: 20px; height: 120px; display: flex; align-items: center; justify-content: center; margin: 20px 0; border: 3px solid #2E8B57; }
    .bar { background: #2E8B57; width: 6px; margin: 2px; border-radius: 10px; animation: pulse 1s infinite ease-in-out; }
    @keyframes pulse { 0%, 100% { height: 15px; } 50% { height: 70px; } }
    .secure-card { background: white; border-radius: 25px; padding: 30px; border: 2px solid #2E8B57; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 500px; margin: auto; text-align: center; }
    </style>
    <div class='main-logo'>⚡ ⭐ ⚡</div>
    <h1 style='text-align: center;'>My FlashDeal Star</h1>
    <p style='text-align: center; font-style: italic;'>Talk. Pay. Done.</p>
    """, unsafe_allow_html=True)

# --- 3. القائمة ---
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "المساعدة"],
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "info-circle"],
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# --- 4. المحتوى التفاعلي ---
if selected == "إبرام الصفقة":
    st.markdown("<div class='secure-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500")
    st.subheader("Wireless Headphones")
    st.write("⭐⭐⭐⭐⭐")
    st.markdown("<h2 style='color: #2E8B57;'>$99.99</h2>", unsafe_allow_html=True)
    if st.button("BUY NOW / إتمام الصفقة"):
        st.balloons()
        st.success("تمت العملية بنجاح!")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "الوكيل الذكي":
    st.markdown("### 🤖 تجربة الوكيل الذكي")
    mode = st.radio("اختر نمط التفاعل:", ["نمط الصوت 🎤", "نمط الإيماءة ✋"], horizontal=True)
    
    if mode == "نمط الصوت 🎤":
        st.write("🎥 محاكي الموجات الصوتية النشط:")
        # توليد 20 عمود موجي متحرك
        waves_html = "<div class='wave-box'>" + "".join([f"<div class='bar' style='animation-delay: {i*0.1}s'></div>" for i in range(20)]) + "</div>"
        st.markdown(waves_html, unsafe_allow_html=True)
        st.info("جيمين: 'أنا أسمعك الآن.. قل (تم) لتأكيد الدفع'")
        
    else:
        st.write("📸 محاكي الكاميرا البيومترية:")
        st.markdown("<div style='border: 4px dashed #2E8B57; height: 150px; border-radius: 20px; display: flex; align-items: center; justify-content: center;'>ارفع إبهامك للتأكيد 👍</div>", unsafe_allow_html=True)

elif selected == "الأمان":
    st.header("🛡️ مركز الأمان")
    st.toggle("بصمة الوجه والبيومتري", value=True)
    st.toggle("نظام التوكن المتبادل", value=True)
    st.success("جميع طبقات الأمان مفعلة.")

elif selected == "سجل الصفقات":
    st.header("📜 سجل العمليات")
    st.write(f"آخر عملية: {now.strftime('%Y-%m-%d')}")
    st.write("الحالة: MVP Launch ✅")

else:
    st.write("مركز المساعدة جاهز لخدمتكم.")

# تذييل الصفحة لملء الفراغ
st.markdown("<br><br><br><div style='text-align: center; color: gray; border-top: 1px solid #ddd; padding: 20px;'>FlashDeal Star © 2026 | Talk. Pay. Done.</div>", unsafe_allow_html=True)
