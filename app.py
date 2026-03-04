import streamlit as st
from streamlit_option_menu import option_menu
import time

# --- الإعدادات السيادية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #f0f2f6; border-radius: 10px; padding: 10px 20px; }
    .token-box { background: #0F172A; color: #00E676; padding: 15px; border-radius: 15px; text-align: center; font-family: monospace; font-size: 20px; border: 1px solid #00E676; }
    .help-header { color: #E63946; font-weight: bold; font-size: 24px; display: flex; align-items: center; gap: 10px; }
    </style>
    """, unsafe_allow_html=True)

# الهيدر الموحد (نفس نمط صورك الناجحة)
st.markdown("<div style='text-align:center;'><h1>⚡ ⭐ My FlashDeal Star</h1><p>Talk. Pay. Done.</p></div>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["الأمان", "سجل الشفافية", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
    icons=["shield-lock", "clipboard-check", "lightning-fill", "robot", "question-circle-fill"], 
    default_index=2, orientation="horizontal",
    styles={"nav-link-selected": {"background-color": "#10B981"}}
)

# --- محاكاة التوكن المتبادل اللحظي ---
current_token = f"FD-{int(time.time()) % 1000000:06d}-STAR"

if selected == "إبرام الصفقة":
    st.subheader("ركن الشفافية: الثمن والمثمن")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800", caption="سماعات ذكية بريميوم")
    with col2:
        st.title("Wireless Headphones")
        st.markdown("<h2 style='color:#10B981;'>$99.99</h2>", unsafe_allow_html=True)
        st.write("التوكن المتبادل النشط لهذه العملية:")
        st.markdown(f"<div class='token-box'>{current_token}</div>", unsafe_allow_html=True)
        if st.button("إتمام الصفقة فوراً / Confirm Deal", use_container_width=True):
            st.success("تمت العملية بنجاح. Talk. Pay. Done.")

elif selected == "الوكيل الذكي":
    st.subheader("تجربة الوكيل الذكي (جيمين المطور)")
    # إضافة خيار الكتابة/الخصوصية كما طلبت
    mode = st.radio("اختر نمط التفاعل المفضل لديك:", 
                    ["⌨️ نمط الكتابة/الخصوصية", "🎤 نمط الصوت", "🖐️ نمط لغة الإشارة"], horizontal=True)
    
    if "الكتابة" in mode:
        user_text = st.text_input("تفضل بكتابة أمرك للوكيل:")
        if user_text: st.info(f"جيمين: 'جاري معالجة طلبك: {user_text}'")
    elif "الصوت" in mode:
        st.write("الوكيل يحلل نبرة الصوت والتوكن المتبادل:")
        st.image("https://upload.wikimedia.org/wikipedia/commons/b/b9/Waveform.png", width=400) # محاكاة الموجة
        st.info(f"جيمين: 'نبرة صوتك مطابقة للتوكن: {current_token}'")

elif selected == "Aide / Help":
    # محاكاة دقيقة لمركز المساعدة المطور
    st.markdown("<div class='help-header'>❓ (Aide) مركز المساعدة المطور</div>", unsafe_allow_html=True)
    st.write("كيف يمكننا مساعدتك اليوم في بيئة FlashDeal؟")
    
    with st.expander("كيفية استخدام الأمر الصوتي؟"):
        st.write("يمكنك تفعيل الوكيل عبر الضغط على أيقونة الميكروفون والتحدث بوضوح.")
    with st.expander("ما هو نظام التوكن المتبادل (Mutual Token)؟"):
        st.write("هو تشفير لحظي يتغير كل ثانية لضمان أمان العملية بينك وبين التاجر.") [cite: 2026-02-22]

elif selected == "الأمان":
    st.subheader("مركز الأمان الشامل")
    st.toggle("بصمة الوجه والبيومتري", value=True)
    st.toggle("نظام التوكن المتبادل (Mutual Token)", value=True)
    st.toggle("تأمين جهاز السيارة (FlashDeal Star Key)", value=False)
    st.info("نظام الأمان متصل بقاعدة بيانات التوكنات المشفرة.")

elif selected == "سجل الشفافية":
    st.subheader("سجل العمليات المالية")
    st.table([{"التاريخ": "2026-03-04", "المنتج": "Headphones", "الثمن": "$99.99", "الحالة": "مكتمل ✅"}])

st.markdown("<br><hr><center>My FlashDeal Star © 2026 | Talk. Pay. Done.</center>", unsafe_allow_html=True)
