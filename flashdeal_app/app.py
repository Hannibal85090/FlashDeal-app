import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time

# الترجمات
translations = {
    "en": {
        "title": "FlashDeal Star",
        "welcome": "Welcome to FlashDeal Star",
        "tagline": "Simplicity, security, and flexibility in every deal",
        "get_started": "Get Started",
        "security": "Security Center",
        "log": "Transaction Log",
        "agent": "Smart Agent",
        "help": "Help Center",
        "rate": "Rate Product"
    },
    "ar": {
        "title": "فلاش ديل ستار",
        "welcome": "مرحبًا بك في فلاش ديل ستار",
        "tagline": "سهولة، أمان، ومرونة في كل صفقة",
        "get_started": "ابدأ الآن",
        "security": "مركز الأمان",
        "log": "سجل الصفقات",
        "agent": "الوكيل الذكي",
        "help": "مركز المساعدة",
        "rate": "قيّم المنتج"
    },
    "fr": {
        "title": "FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Simplicité, sécurité et flexibilité dans chaque transaction",
        "get_started": "Commencer",
        "security": "Centre de sécurité",
        "log": "Journal des transactions",
        "agent": "Agent intelligent",
        "help": "Centre d'aide",
        "rate": "Évaluer le produit"
    }
}

# اختيار اللغة
lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["en", "ar", "fr"])
t = translations[lang]

# شريط تنقل بين الصفحات
page = st.sidebar.radio("📑 Pages", [t["welcome"], t["security"], t["log"], t["agent"], t["help"], t["rate"]])

# الصفحة الرئيسية
if page == t["welcome"]:
    st.markdown(f"<h1 style='text-align:center; color:#007AFF;'>{t['title']} ⚡⭐</h1>", unsafe_allow_html=True)
    st.subheader(t["welcome"])
    st.write(t["tagline"])
    if st.button(t["get_started"]):
        st.success("🚀 " + t["welcome"])

# صفحة الأمان
elif page == t["security"]:
    st.header(t["security"])
    st.write("✅ Face ID & Biometric enabled\n✅ Mutual Token System active")

# سجل الصفقات
elif page == t["log"]:
    st.header(t["log"])
    st.write("📊 Recent transactions will appear here...")

# الوكيل الذكي
elif page == t["agent"]:
    st.header(t["agent"])
    mode = st.radio("🎛 اختر نمط التفاعل", ["🎤 صوت", "🖐️ إيماء", "✍️ كتابة"])
    if mode == "🎤 صوت":
        st.info("🎙 الوكيل الذكي يستمع إليك الآن...")
    elif mode == "🖐️ إيماء":
        st.info("🖐️ تفاعل بالإيماءات مفعّل.")
    else:
        user_input = st.text_input("✍️ اكتب هنا للتفاعل مع الوكيل الذكي")
        if user_input:
            st.success(f"🤖 الوكيل الذكي: استلمت رسالتك - '{user_input}'")

# مركز المساعدة
elif page == t["help"]:
    st.header(t["help"])
    st.write("❓ هنا تجد إجابات على الأسئلة الشائعة ودعم مباشر.")

# تقييم المنتج
elif page == t["rate"]:
    st.header(t["rate"])
    rating = st.slider("⭐ اختر تقييمك", 1, 5, 3)
    st.write(f"لقد قيّمت المنتج بـ {rating} نجوم.")
