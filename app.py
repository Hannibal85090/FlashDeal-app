import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. الإعدادات الأساسية (بدون حشو) ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# --- 2. التصميم البصري الاحترافي (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #F0F2F6; }
    
    /* هوية العلامة التجارية */
    .brand-header { text-align: center; padding: 2rem; background: #ffffff; border-radius: 0 0 30px 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
    .star-logo { font-size: 50px; color: #FFD700; text-shadow: 0 0 10px rgba(255,215,0,0.5); }
    
    /* بطاقة المنتج (وضوح الثمن والمثمن) */
    .product-card { background: white; border-radius: 20px; padding: 2rem; border: 1px solid #E1E4E8; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }
    .price-tag { color: #2E7D32; font-size: 42px; font-weight: bold; margin: 1rem 0; }
    
    /* الوكيل الذكي (موجات تفاعلية) */
    .wave-container { display: flex; align-items: flex-end; justify-content: center; height: 100px; gap: 5px; background: #000; border-radius: 15px; padding: 20px; }
    .wave-bar { width: 6px; background: #00E676; border-radius: 5px; animation: pulse 1s infinite ease-in-out; }
    @keyframes pulse { 0%, 100% { height: 20px; } 50% { height: 80px; } }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر والقائمة ---
st.markdown("<div class='brand-header'><div class='star-logo'>⚡ ⭐ ⚡</div><h1>My FlashDeal Star</h1><p>Talk. Pay. Done.</p></div>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل العمليات", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    icons=["shield-lock", "clock-history", "lightning-fill", "mic-fill", "question-circle-fill"], 
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#2E7D32"}}
)

# --- 4. المنطق الوظيفي للأقسام ---

if selected == "إبرام الصفقة":
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800", caption="المثمن: سماعات بريميوم")
    with col2:
        st.title("Wireless Headphones")
        st.write("نظام الإيجاب والقبول اللحظي - My FlashDeal Star Edition")
        # السعر نظيف تماماً بدون تداخل HTML
        st.markdown("<div class='price-tag'>$99.99</div>", unsafe_allow_html=True)
        if st.button("إتمام الصفقة الآن / BUY NOW", use_container_width=True):
            st.balloons()
            st.success("تمت العملية بنجاح. Talk. Pay. Done.")
    st.markdown("</div>", unsafe_allow_html=True)

elif selected == "الوكيل الذكي":
    st.subheader("تجربة الوكيل الذكي (جيمين)")
    mode = st.radio("اختر نمط التفاعل المفضل:", ["🎤 نمط الصوت (الحساس)", "🖐️ نمط لغة الإشارة (الخصوصية)"], horizontal=True)
    
    if "الصوت" in mode:
        st.write("الوكيل يستشعر الآن نبرة صوتك واهتزازاتها:")
        waves = "".join([f"<div class='wave-bar' style='animation-delay:{i*0.1}s'></div>" for i in range(20)])
        st.markdown(f"<div class='wave-container'>{waves}</div>", unsafe_allow_html=True)
        st.info("جيمين: 'نبرة صوتك مطابقة للتوكن الرقمي.. تفضل بأمرك.'") [cite: 2026-02-22]
    else:
        st.write("نظام تحليل لغة الإشارة والإيماءات نشط (لأصحاب الهمم والخصوصية):") [cite: 2026-02-21]
        st.image("https://images.unsplash.com/photo-1516733968668-dbdce39c46ef?w=500", caption="تحليل الكاميرا البيومتري")

elif selected == "الأمان":
    st.markdown("### 🛡️ مركز الأمان المتقدم")
    st.checkbox("بصمة الوجه والبيومتري", value=True)
    st.checkbox("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.checkbox("تأمين جهاز السيارة (FlashDeal Star Key)", value=True) [cite: 2026-02-20]
    st.success("جميع طبقات الأمان نشطة.")

elif selected == "سجل العمليات":
    st.markdown("### 📜 سجل الشفافية")
    st.table([{"التاريخ": "2026-03-04", "المنتج": "Headphones", "الثمن": "$99.99", "الحالة": "مكتمل ✅"}])

st.markdown("<br><hr><center>My FlashDeal Star © 2026</center>", unsafe_allow_html=True)
