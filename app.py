import streamlit as st
from streamlit_option_menu import option_menu

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# تصميم الواجهة الاحترافي (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #F8FAFC; }
    
    .main-header { text-align: center; padding: 25px; background: white; border-radius: 0 0 35px 35px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
    .price-container { background: #10B981; color: white; padding: 10px 30px; border-radius: 50px; font-size: 35px; font-weight: bold; display: inline-block; }
    
    .wave-box { background: #000; border-radius: 20px; padding: 30px; display: flex; justify-content: center; align-items: flex-end; gap: 4px; height: 100px; }
    .wave-bar { width: 5px; background: #34D399; border-radius: 5px; animation: bar-move 1s infinite ease-in-out; }
    @keyframes bar-move { 0%, 100% { height: 15px; } 50% { height: 70px; } }
    </style>
    """, unsafe_allow_html=True)

# الهيدر الموحد
st.markdown("<div class='main-header'><h1>⚡ ⭐ My FlashDeal Star</h1><p>Talk. Pay. Done.</p></div>", unsafe_allow_html=True)

# قائمة التنقل الذكية
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الشفافية", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    icons=["shield-lock", "clipboard-data", "lightning-charge", "robot", "question-circle"], 
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#10B981"}}
)

# --- الوظائف الأساسية ---

if selected == "إبرام الصفقة":
    st.subheader("ركن الشفافية: الثمن والمثمن")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800", caption="المثمن: سماعات ذكية")
    with col2:
        st.title("Wireless Headphones")
        st.write("أفضل سعر متاح حالياً عبر جيمين لضمان الإيجاب والقبول.")
        st.markdown("<div class='price-container'>$99.99</div>", unsafe_allow_html=True)
        if st.button("Confirm Deal / إتمام الصفقة فوراً", use_container_width=True):
            st.balloons()
            st.success("تمت العملية بنجاح. Talk. Pay. Done.")

elif selected == "الوكيل الذكي":
    st.subheader("تجربة الوكيل الذكي (جيمين المطور)")
    mode = st.radio("اختر نمط التفاعل:", ["نمط الصوت", "نمط لغة الإشارة"], horizontal=True)
    
    if mode == "نمط الصوت":
        st.write("الوكيل يحلل نبرة الصوت والتوكن المتبادل:")
        bars = "".join([f"<div class='wave-bar' style='animation-delay:{i*0.05}s'></div>" for i in range(25)])
        st.markdown(f"<div class='wave-box'>{bars}</div>", unsafe_allow_html=True)
        st.info("جيمين: 'نبرة صوتك مطابقة للتوكن الرقمي.. تفضل بأمرك.'")
    else:
        st.write("نظام تحليل الإيماءات ولغة الإشارة نشط.")
        st.image("https://images.unsplash.com/photo-1516733968668-dbdce39c46ef?w=500")

elif selected == "الأمان":
    st.subheader("مركز الأمان الشامل")
    st.toggle("بصمة الوجه والبيومتري", value=True)
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.toggle("تأمين جهاز السيارة (FlashDeal Star Key)", value=False)
    st.success("نظام الأمان متصل بقاعدة بيانات التوكنات المشفرة.")

elif selected == "سجل الشفافية":
    st.subheader("سجل العمليات المالية")
    st.table([{"التاريخ": "2026-03-04", "المنتج": "Headphones", "الثمن": "$99.99", "الحالة": "مكتمل ✅"}])

st.markdown("<br><hr><center>My FlashDeal Star © 2026 | Talk. Pay. Done.</center>", unsafe_allow_html=True)
