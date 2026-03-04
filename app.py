import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import time

# --- 1. الإعدادات الأساسية والهوية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

now = datetime.datetime.now()
dt_string = now.strftime("%A, %d %B %Y | %H:%M:%S")

# --- 2. محرك الجماليات والحركة (CSS) ---
st.markdown(f"""
    <style>
    .stApp {{ background: linear-gradient(180deg, #E0F2F1 0%, #FFFFFF 100%); }}
    
    /* أنيميشن الشعار (البرق والنجمة) */
    @keyframes flash-glow {{
        0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 5px #FFD700); }}
        50% {{ transform: scale(1.1); filter: drop-shadow(0 0 20px #FFD700); color: #FFD700; }}
    }}
    .main-logo {{ font-size: 60px; text-align: center; animation: flash-glow 2s infinite; font-weight: bold; cursor: default; }}
    
    /* تنسيق الثمن والشفافية */
    .price-container {{ 
        background: #f8f9fa; border-left: 5px solid #2E8B57; padding: 15px; 
        border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }}
    .price-val {{ color: #2E8B57; font-size: 35px; font-weight: bold; }}
    
    /* موجات الوكيل الذكي الحساسة */
    .wave-bar {{
        display: inline-block; background: #2E8B57; width: 6px; margin: 2px;
        border-radius: 5px; animation: sensitive-pulse 1.2s infinite ease-in-out;
    }}
    @keyframes sensitive-pulse {{
        0%, 100% {{ height: 15px; opacity: 0.5; }}
        50% {{ height: 60px; opacity: 1; }}
    }}
    </style>
    <div style='text-align: right; font-weight: bold; color: #1a1a1a;'>{dt_string}</div>
    <div class='main-logo'>⚡ ⭐ ⚡</div>
    <h1 style='text-align: center; color: #1a1a1a;'>My FlashDeal Star</h1>
    <p style='text-align: center; font-size: 1.2rem; font-style: italic;'>Talk. Pay. Done.</p>
    """, unsafe_allow_html=True)

# --- 3. نظام التنقل الحديث (استبدال i بـ ؟) ---
selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الصفقات", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    icons=["shield-lock", "list-check", "lightning-charge", "robot", "question-circle"], 
    default_index=2, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#2E8B57"}
    }
)

# --- 4. الأقسام البرمجية المعتمدة ---

if selected == "إبرام الصفقة":
    st.markdown("### 🛒 ركن الشفافية: الثمن والمثمن")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600", caption="المثمن: سماعات ذكية بريميوم")
    with col2:
        st.markdown("<div class='price-container'>", unsafe_allow_html=True)
        st.subheader("Wireless Headphones - Gold Star Edition")
        st.write("أفضل سعر متاح حالياً عبر جيمين لضمان الإيجاب والقبول.")
        st.markdown("<span class='price-val'>$99.99</span> <small style='text-decoration:line-through;'>$199.99</small>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("إتمام الصفقة فوراً / Confirm Deal"):
            with st.spinner("جاري تأمين التوكن والتحقق من الهوية..."):
                time.sleep(1.5)
                st.balloons()
                st.success("تم الإيجاب والقبول بنجاح. Talk. Pay. Done.")

elif selected == "الوكيل الذكي":
    st.markdown("### 🤖 وكيل جيمين الذكي (حساس للنبرة)")
    tab1, tab2 = st.tabs(["🎤 التفاعل الصوتي", "✍️ الخصوصية واللمس"])
    
    with tab1:
        st.write("الوكيل يستشعر الآن أبسط اهتزازات نبرة صوتك:")
        wave_html = "<div style='text-align:center; background:#1a1a1a; padding:30px; border-radius:20px;'>" + \
                    "".join([f"<div class='wave-bar' style='animation-delay:{i*0.05}s'></div>" for i in range(35)]) + "</div>"
        st.markdown(wave_html, unsafe_allow_html=True)
        st.info("جيمين: 'أنا مسجل عندك.. حللت نبرة صوتك، يمكنك طلب أي منتج الآن'")
        
    with tab2:
        st.text_input("للعملاء اللمسيين وعشاق السرية، أدخل أمرك هنا:")
        st.write("✨ جميع الأوامر النصية مشفرة بالكامل.")

elif selected == "الأمان":
    st.markdown("### 🛡️ مركز الأمان الشامل")
    st.toggle("بصمة الوجه والبيومتري", value=True)
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.toggle("تأمين جهاز السيارة (FlashDeal Star Key)", value=False)
    st.success("نظام الأمان نشط ومتصل بقاعدة بيانات التوكنات المشفرة.")

elif selected == "سجل الصفقات":
    st.markdown("### 📜 سجل الشفافية المالية")
    st.table([
        {"التاريخ": now.strftime("%Y-%m-%d"), "المنتج": "Wireless Headphones", "الثمن": "$99.99", "الحالة": "مكتمل ✅"}
    ])

elif selected == "Aide / Help":
    st.markdown("### ❓ مركز المساعدة المطور (Aide)")
    st.write("كيف يمكننا مساعدتك اليوم في بيئة FlashDeal؟")
    with st.expander("كيفية استخدام الأمر الصوتي؟"):
        st.write("فقط قل 'اتمم الصفقة' وسيقوم جيمين بتحليل نبرة صوتك ومطابقتها مع التوكن الخاص بك.")

# --- 5. التذييل (Footer) لملء الفراغ ---
st.markdown("<br><br><br><div style='text-align: center; color: #888; border-top: 1px solid #ddd; padding: 20px;'>My FlashDeal Star © 2026 | Talk. Pay. Done.</div>", unsafe_allow_html=True)
