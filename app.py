import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. إعدادات الهوية البصرية FlashDeal Star ---
st.set_page_config(page_title="FlashDeal Star", page_icon="⭐", layout="centered")

# تطبيق التدرج اللوني (سماوي إلى أبيض) وتنسيق الأزرار والنجوم
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #87CEEB 0%, #F0F8FF 100%);
    }
    .stButton>button {
        background-color: #2E8B57 !important;
        color: white !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        width: 100%;
        border: none !important;
        height: 3em;
    }
    .star-rating {
        color: #FFD700;
        font-size: 1.5rem;
        text-align: center;
        margin-top: -15px;
    }
    .product-title {
        text-align: center;
        font-weight: bold;
        color: #1E1E1E;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. منطق الوكيل الذكي (FlashDeal Agent Logic) ---
class FlashDealAgent:
    def __init__(self):
        self.slogan = "Talk. Pay. Done."
        self.vision = "Simple Production [cite: 2026-02-21]"
    
    def execute_deal(self):
        return f"Executing with: {self.slogan}"

agent = FlashDealAgent()

# --- 3. نظام التنقل (النقاط الثلاث) ---
# هذا يحاكي النقاط التي تظهر في الصور أسفل الشاشة
selected = option_menu(
    menu_title=None, 
    options=["الإعدادات", "إبرام الصفقة", "الوكيل الذكي"], 
    icons=["gear", "stars", "robot"], 
    menu_icon="cast", 
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px"},
        "nav-link-selected": {"background-color": "#2E8B57"},
    }
)

# --- 4. محتوى الصفحات ---

if selected == "إبرام الصفقة":
    # عرض صورة المنتج (السماعات) من مجلد assets
    try:
        st.image("assets/1000022439.jpg", use_container_width=True)
    except:
        st.image("https://via.placeholder.com/400x300/87CEEB/FFFFFF?text=FlashDeal+Star", use_container_width=True)
    
    st.markdown('<h2 class="product-title">Wireless Headphones</h2>', unsafe_allow_html=True)
    # النجوم تحت العنوان مباشرة لإظهار الجودة العالية كما اتفقنا
    st.markdown('<p class="star-rating">⭐⭐⭐⭐⭐ (4.9)</p>', unsafe_allow_html=True)
    
    st.write("Experience rich, wireless sound.")
    st.markdown("### $99.99 <span style='color:grey; text-decoration:line-through; font-size:15px'>$199.99</span>", unsafe_allow_html=True)
    
    if st.button("Buy Now / إتمام الصفقة"):
        st.balloons()
        st.success(f"Success! {agent.execute_deal()}")

elif selected == "الإعدادات":
    st.markdown("## ⚙️ Settings & Security")
    st.write("خيارات الأمان المتقدمة: بصمة، وجه، ورمز سري [cite: 2026-02-20].")
    st.checkbox("تفعيل البطاقة البيومترية")
    st.checkbox("ربط My FlashDeal Star بالسيارة")

elif selected == "الوكيل الذكي":
    st.markdown(f"## 🤖 FlashDeal AI Assistant")
    st.info(f"Vision: {agent.vision}")
    st.write("توجيه الصوت والتقاط الإشارات الحيوية قيد التشغيل...")
    
    if st.button('Execute Trading Command / تنفيذ أمر التداول'):
        st.success(agent.execute_deal())
        st.write("تم تحليل حركة الجسم ومطابقة البصمة.")
