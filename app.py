import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")

# 1. الهوية البصرية
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%); }}
    .main-logo {{ font-size: 50px; text-align: center; animation: pulse 2s infinite; font-weight: bold; }}
    @keyframes pulse {{ 0%, 100% {{ transform: scale(1); opacity: 0.7; }} 50% {{ transform: scale(1.1); opacity: 1; }} }}
    .wave-container {{ background: #1a1a1a; border-radius: 15px; padding: 20px; text-align: center; border: 2px solid #2E8B57; }}
    .bar {{ background: #2E8B57; width: 4px; height: 30px; display: inline-block; margin: 1px; animation: wave 1s infinite ease-in-out; }}
    @keyframes wave {{ 0%, 100% {{ height: 10px; }} 50% {{ height: 50px; }} }}
    </style>
    <div style='text-align: right; font-weight: bold;'>{dt_string}</div>
    <div class='main-logo'>⚡ ⭐ ⚡</div>
    <h1 style='text-align: center;'>My FlashDeal Star</h1>
    <p style='text-align: center;'>Talk. Pay. Done.</p>
    """, unsafe_allow_html=True)

# 2. القائمة
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "المساعدة"],
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "info-circle"],
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# 3. محتوى الوكيل الذكي (المطور ليدعم الخصوصية)
if selected == "الوكيل الذكي":
    st.markdown("### 🤖 تجربة الوكيل الذكي (جيمين)")
    mode = st.radio("اختر نمط التفاعل المفضل لديك:", 
                    ["نمط الصوت 🎤", "نمط الإيماءة ✋", "نمط الكتابة/الخصوصية ✍️"], 
                    horizontal=True)
    
    if mode == "نمط الصوت 🎤":
        st.write("🎥 محاكي الموجات الصوتية النشط:")
        waves = "".join([f"<div class='bar' style='animation-delay: {i*0.1}s'></div>" for i in range(30)])
        st.markdown(f"<div class='wave-container'>{waves}</div>", unsafe_allow_html=True)
        st.info("جيمين: 'أنا أسمعك الآن بوضوح.. تفضل بأمرك'")
        
    elif mode == "نمط الإيماءة ✋":
        st.markdown("<div style='border: 3px dashed #2E8B57; height: 150px; display: flex; align-items: center; justify-content: center; border-radius: 20px;'>📸 استشعار بصمة الحركة نشط.. (👍 للتأكيد)</div>", unsafe_allow_html=True)
        
    elif mode == "نمط الكتابة/الخصوصية ✍️":
        st.text_input("اكتب أمرك هنا بسرية تامة (مثال: اتمم الصفقة رقم 5):")
        st.write("✨ جيمين: 'أوامرك سرية ومحفوظة بتوكن الأمان'")

# 4. باقي الأقسام
elif selected == "إبرام الصفقة":
    st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", caption="المنتج المختار")
    if st.button("BUY NOW / إتمام الصفقة"):
        st.balloons()
        st.success("تمت العملية بنجاح! Talk. Pay. Done.")

elif selected == "الأمان":
    st.toggle("بصمة الوجه", value=True)
    st.toggle("نظام التوكن المتبادل", value=True)
    st.success("درع الأمان الخاص بـ FlashDeal Star يعمل بكفاءة.")

st.markdown("<br><br><br><div style='text-align: center; color: gray; border-top: 1px solid #ddd; padding: 10px;'>FlashDeal Star © 2026 | Talk. Pay. Done.</div>", unsafe_allow_html=True)
