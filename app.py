import streamlit as st

# إعدادات الصفحة والهوية البصرية الجديدة
st.set_page_config(page_title="FlashDeal - Talk. Pay. Done.", page_icon="⚡", layout="centered")

# CSS لتحويل الواجهة إلى الأسود والبنفسجي وتصغير العناصر
st.markdown("""
    <style>
    /* خلفية سوداء بالكامل */
    .stApp { background-color: #000000; color: #ffffff; }
    
    /* تنسيق الأزرار (تصغير وجعلها بنفسجية نيون) */
    .stButton>button {
        background-color: #6a0dad; 
        color: white; 
        border-radius: 10px;
        padding: 5px 15px;
        font-size: 14px;
        border: 1px solid #bc13fe;
        box-shadow: 0 0 10px #6a0dad;
    }
    
    /* تصغير مستطيل الإدخال وجعله غامضاً */
    .stTextInput>div>div>input {
        background-color: #1a1a1a;
        color: #bc13fe;
        border: 1px solid #333;
        text-align: center;
        font-size: 20px;
    }
    
    /* إخفاء تسميات الحقول لجعلها أكثر بساطة */
    label { display: none !important; }
    
    /* تنسيق موجة الصوت (محاكاة) */
    .voice-wave {
        border: 1px solid #bc13fe;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        background: linear-gradient(45deg, #000, #1a0033);
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان والشعار
st.markdown("<h1 style='text-align: center; color: #ffffff;'>⚡ FlashDeal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #bc13fe; letter-spacing: 2px;'>Talk. Pay. Done.</p>", unsafe_allow_html=True)

# الجزء التقني: التحدث (Talk)
st.markdown("<div class='voice-wave'>🎙️</div>", unsafe_allow_html=True)
if st.button("Voice Command"):
    st.write("Listening...")

# الجزء المالي: (Pay) - مستطيل صغير للدولار بدون أرقام ثابتة
st.markdown("<p style='text-align: center; margin-top:20px;'>Amount</p>", unsafe_allow_html=True)
amount = st.text_input("Amount", value="$ 1")

# خيارات الدفع (تصغير الأيقونات)
col1, col2, col3 = st.columns(3)
with col1: st.button("Wallet")
with col2: st.button("Card")
with col3: st.button("Flash")

# تذييل الصفحة (Done)
st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 10px; color: #555;'>Powered by Gemini 1.5 Flash</p>", unsafe_allow_html=True)
