import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

# --- 1. إعدادات الهوية والعداد الحي ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")

st.markdown(f"<div style='text-align: right; color: #2E8B57; font-weight: bold;'>{dt_string}</div>", unsafe_allow_html=True)

# --- 2. محرك الجماليات (البرق والنجمة + الأنيميشن الجديد) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%); min-height: 100vh; }
    @keyframes flash-star { 0%, 100% { opacity: 0.5; transform: scale(1); } 50% { opacity: 1; transform: scale(1.1); color: #FFD700; } }
    .main-logo { font-size: 50px; text-align: center; animation: flash-star 2s infinite; font-weight: bold; }
    .wave-container { background: #1E1E1E; border-radius: 15px; height: 100px; display: flex; align-items: center; justify-content: center; margin: 20px 0; }
    .wave { background: #2E8B57; margin: 2px; width: 5px; border-radius: 5px; animation: wave-motion 1s infinite; }
    @keyframes wave-motion { 0%, 100% { height: 10px; } 50% { height: 50px; } }
    .secure-box { background: white; border-radius: 25px; padding: 30px; border: 2px solid #2E8B57; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 550px; margin: auto; }
    </style>
    <div class='main-logo'>⚡ ⭐ ⚡</div>
    <h1 style='text-align: center;'>My FlashDeal Star</h1>
    """, unsafe_allow_html=True)

# --- 3. التنقل ---
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "المساعدة"],
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "info-circle"],
    default_index=2, orientation="horizontal", styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# --- 4. الشاشات ---
if selected == "إبرام الصفقة":
    st.markdown("<div class='secure-box'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", caption="Premium Headphones")
    st.subheader("Wireless Headphones")
    st.write("⭐⭐⭐⭐⭐ (4.9)")
    st.markdown("<h2 style='color: #2E8B57;'>$99.99</h2>", unsafe_allow_html=True)
    if st.button("BUY NOW / إتمام الصفقة"):
        st.balloons()
        st.success(f"تمت الصفقة بنجاح في {now.strftime('%H:%M:%S')}")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "الوكيل الذكي":
    st.header("🤖 FlashDeal AI Agent")
    mode = st.radio("اختر وسيلة التفاعل مع الوكيل:", ["الصوت 🎤", "الإيماءة ✋", "النص ✍️"], horizontal=True)
    
    if mode == "الصوت 🎤":
        st.markdown("<div class='wave-container'>" + "".join(["<div class='wave' style='animation-delay:"+str(i/10)+"s'></div>" for i in range(20)]) + "</div>", unsafe_allow_html=True)
        st.info("جيمين: 'أنا أسمعك.. قل (إتمام الصفقة) لبدء العملية'")
        
    elif mode == "الإيماءة ✋":
        st.markdown("<div style='border: 3px dashed #2E8B57; height: 200px; display: flex; align-items: center; justify-content: center; border-radius: 20px;'>📸 محاكي الكاميرا الذكية: حرك يدك للأعلى للتأكيد</div>", unsafe_allow_html=True)
        
    st.write("---")
    st.caption("هذه الميزة تعزز الأمان والسرعة في شعارنا: Talk. Pay. Done. [cite: 2026-02-07]")

elif selected == "الأمان":
    st.header("🛡️ مركز الأمان")
    st.checkbox("بصمة الوجه (Biometric)", value=True)
    st.checkbox("التوكن المتبادل (Mutual Token)", value=True) [cite: 2026-02-20]
    st.success("نظام الأمان نشط ومتصل بجهازك الذكي.")

# سجل الصفقات والمساعدة
else:
    st.write("المحتوى جاهز للاستعراض..")

# ملء الفراغ بلمسة أخيرة
st.markdown("<br><br><br><p style='text-align: center; color: gray;'>FlashDeal Star © 2026 | Talk. Pay. Done.</p>", unsafe_allow_html=True)
