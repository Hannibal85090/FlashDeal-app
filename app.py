import streamlit as st
from streamlit_option_menu import option_menu
import datetime

st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# الوقت الحقيقي لتعزيز المصداقية [cite: 2026-03-04]
now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")

st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%); }}
    .price-box {{ background: white; padding: 10px; border-radius: 10px; border: 2px solid #2E8B57; display: inline-block; }}
    .price-text {{ color: #2E8B57; font-size: 28px; font-weight: bold; }}
    </style>
    <div style='text-align: right; font-weight: bold; color: #2E8B57;'>{dt_string}</div>
    <h1 style='text-align: center;'>⚡ My FlashDeal Star ⚡</h1>
    <p style='text-align: center;'>Talk. Pay. Done.</p>
    """, unsafe_allow_html=True)

# قائمة التنقل مع تحديث أيقونة المساعدة إلى (؟) [cite: 2026-02-18]
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    # question-circle هي أيقونة الاستفهام (?) المطلوبة للحداثة
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "question-circle"], 
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

if selected == "إبرام الصفقة":
    st.markdown("### 🛒 أركان التجارة: الثمن والمثمن")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500")
    with col2:
        st.subheader("Premium Wireless Headphones")
        # إظهار الثمن بوضوح للشفافية
        st.markdown("<div class='price-box'><span class='price-text'>الثمن: $99.99</span></div>", unsafe_allow_html=True)
        if st.button("BUY NOW / إتمام الصفقة"):
            st.balloons()
            st.success("تم الإيجاب والقبول بنجاح! Talk. Pay. Done.")

elif selected == "الوكيل الذكي":
    st.markdown("### 🤖 تفاعل مع جيمين")
    mode = st.radio("نمط التفاعل:", ["الصوت 🎤", "الكتابة/الخصوصية ✍️"], horizontal=True)
    if mode == "الكتابة/الخصوصية ✍️":
        st.text_input("أدخل أمرك المالي هنا بسرية تامة:") [cite: 2026-02-20]

elif selected == "Aide / Help":
    st.markdown("### ❓ مركز المساعدة (Aide)")
    st.write("مرحباً بك في مركز الدعم. هنا تجد إجابات حول البرمجة، الأمان، والخطوات العملية.") [cite: 2026-02-18]
    st.info("جيمين: 'أنا هنا لمساعدتك في فهم نظام التوكن والصفقات اللحظية.'")

elif selected == "الأمان":
    st.markdown("### 🛡️ درع الأمان")
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True)

st.markdown("<br><hr><center>FlashDeal Star © 2026 | الحداثة في الخدمة</center>", unsafe_allow_html=True)
