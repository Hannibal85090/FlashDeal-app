import streamlit as st
from streamlit_option_menu import option_menu
import datetime

# --- إعدادات النخبة الفنية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# تصميم UI/UX مستوحى من أرقى التطبيقات [cite: 2026-02-16]
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #F8FBFF; }
    
    /* أنيميشن الشعار (نبض البرق والنجمة) */
    .header-box { text-align: center; padding: 25px; background: white; border-radius: 0 0 50px 50px; shadow: 0 4px 15px rgba(0,0,0,0.05); }
    .flash-icon { font-size: 55px; animation: pulse-glow 2s infinite; }
    @keyframes pulse-glow { 0% { transform: scale(1); filter: drop-shadow(0 0 2px #FFD700); } 
                            50% { transform: scale(1.1); filter: drop-shadow(0 0 15px #FFD700); } 
                            100% { transform: scale(1); filter: drop-shadow(0 0 2px #FFD700); } }
    
    /* بطاقة الصفقة (الثمن والمثمن بوضوح) */
    .deal-card { background: white; border-radius: 30px; padding: 40px; border: 1px solid #E3E9EF; box-shadow: 0 20px 40px rgba(0,0,0,0.08); }
    .price-badge { background: #2E8B57; color: white; padding: 12px 35px; border-radius: 100px; font-size: 38px; font-weight: bold; display: inline-block; }
    
    /* الوكيل الذكي (موجات حساسة) */
    .ai-container { background: #0F172A; border-radius: 20px; padding: 40px; text-align: center; }
    .wave-bar { display: inline-block; width: 5px; background: #34D399; margin: 0 3px; border-radius: 5px; animation: wave-anim 1.2s infinite ease-in-out; }
    @keyframes wave-anim { 0%, 100% { height: 15px; } 50% { height: 75px; } }
    </style>
    """, unsafe_allow_html=True)

# الهيدر الموحد
st.markdown("<div class='header-box'><div class='flash-icon'>⚡ ⭐ ⚡</div><h1>My FlashDeal Star</h1><p style='color: #64748B;'>Talk. Pay. Done.</p></div>", unsafe_allow_html=True)

# نظام التنقل (الرموز المعتمدة: ؟ للمساعدة، ورق للسجل)
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الشفافية", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    icons=["shield-lock", "receipt", "lightning-charge", "person-video3", "question-circle"], 
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E8B57"}}
)

# 1. إبرام الصفقة (الوضوح التام - الثمن والمثمن)
if selected == "إبرام الصفقة":
    st.markdown("<div class='deal-card'>", unsafe_allow_html=True)
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800", caption="المثمن: سماعات ذكية بريميوم")
    with col_b:
        st.title("Wireless Headphones")
        st.write("نظام الإيجاب والقبول اللحظي - الإصدار الماسي")
        st.markdown("<div class='price-badge'>$99.99</div>", unsafe_allow_html=True)
        if st.button("BUY NOW / إبرام الصفقة", use_container_width=True):
            st.balloons()
            st.success("تمت العملية بنجاح. Talk. Pay. Done.")
    st.markdown("</div>", unsafe_allow_html=True)

# 2. الوكيل الذكي (لغة إشارة + حساس نبرة)
elif selected == "الوكيل الذكي":
    st.subheader("تجربة الوكيل الذكي (جيمين)")
    t1, t2 = st.tabs(["🎤 تحليل النبرة الحساس", "🖐️ لغة الإشارة والإيماء"])
    with t1:
        st.write("جيمين يستشعر أدق اهتزازات نبرة صوتك الآن:")
        waves_html = "<div class='ai-container'>" + "".join([f"<div class='wave-bar' style='animation-delay:{i*0.08}s'></div>" for i in range(30)]) + "</div>"
        st.markdown(waves_html, unsafe_allow_html=True)
        st.info("جيمين: 'نبرة صوتك مطابقة للتوكن. تفضل بأمرك المالي.'")
    with t2:
        st.write("نظام التعرف على لغة الإشارة (Gestures) نشط بالكامل.")
        st.image("https://images.unsplash.com/photo-1516733968668-dbdce39c46ef?w=500", caption="كاميرا التحليل البيومتري")

# 3. الأمان الشامل (التوكن والجهاز)
elif selected == "الأمان":
    st.markdown("### 🛡️ مركز الأمان المتقدم")
    st.toggle("بصمة الوجه والبيومتري", value=True)
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.toggle("ربط مفتاح FlashDeal Star الذكي", value=True) [cite: 2026-02-20]
    st.success("جميع طبقات الأمان نشطة وتعمل بالتوازي.")

# 4. سجل الشفافية
elif selected == "سجل الشفافية":
    st.markdown("### 📜 سجل الشفافية المالية")
    st.table([{"التاريخ": "2026-03-04", "المنتج": "Wireless Headphones", "الثمن الصافي": "$99.99", "الحالة": "مكتمل ✅"}])

st.markdown("<br><hr><center>My FlashDeal Star © 2026 | الحداثة والوظيفية</center>", unsafe_allow_html=True)
