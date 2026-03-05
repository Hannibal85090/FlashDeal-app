import streamlit as st

# الترجمات
translations = {
    "en": {
        "title": "⚡⭐ FlashDeal Star",
        "welcome": "Welcome to FlashDeal Star",
        "tagline": "Talk. Pay. Done.",
        "get_started": "Get Started",
        "security": "Security Center",
        "log": "Transparency Log",
        "deal": "Deal Execution",
        "agent": "Smart Agent",
        "help": "Help Center",
        "rate": "Rate Product",
        "voice": "🎤 Voice",
        "gesture": "🖐️ Gesture",
        "writing": "✍️ Writing",
        "rating_label": "⭐ Choose your rating",
        "price": "Price"
    },
    "ar": {
        "title": "⚡⭐ فلاش ديل ستار",
        "welcome": "مرحبًا بك في فلاش ديل ستار",
        "tagline": "تحدث. ادفع. تم.",
        "get_started": "ابدأ الآن",
        "security": "مركز الأمان",
        "log": "سجل الشفافية",
        "deal": "إبرام الصفقة",
        "agent": "الوكيل الذكي",
        "help": "مركز المساعدة",
        "rate": "قيّم المنتج",
        "voice": "🎤 صوت",
        "gesture": "🖐️ إيماء",
        "writing": "✍️ كتابة",
        "rating_label": "⭐ اختر تقييمك",
        "price": "السعر"
    },
    "fr": {
        "title": "⚡⭐ FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Parlez. Payez. Terminé.",
        "get_started": "Commencer",
        "security": "Centre de sécurité",
        "log": "Journal de transparence",
        "deal": "Exécution de l'offre",
        "agent": "Agent intelligent",
        "help": "Centre d'aide",
        "rate": "Évaluer le produit",
        "voice": "🎤 Voix",
        "gesture": "🖐️ Geste",
        "writing": "✍️ Écriture",
        "rating_label": "⭐ Choisissez votre évaluation",
        "price": "Prix"
    }
}

# اختيار اللغة
lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["en", "ar", "fr"])
t = translations[lang]

# شريط تنقل بين الصفحات
page = st.sidebar.radio("📑 Pages", [t["welcome"], t["security"], t["log"], t["deal"], t["agent"], t["help"], t["rate"]])

# الصفحة الرئيسية
if page == t["welcome"]:
    st.markdown(f"<h1 style='text-align:center; color:#007AFF;'>{t['title']}</h1>", unsafe_allow_html=True)
    st.subheader(t["welcome"])
    st.write(t["tagline"])
    if st.button(t["get_started"]):
        st.success("🚀 " + t["welcome"])
    st.markdown("<h3 style='text-align:center; color:#FFD700;'>⭐ ⚡ FlashDeal Star is shining...</h3>", unsafe_allow_html=True)

# صفحة الصفقة
elif page == t["deal"]:
    st.header(t["deal"])
    
    # صورة المنتج
    st.image("product.png", caption="Wireless Headphones", use_column_width=True)
    
    # السعر مترجم
    if lang == "en":
        st.subheader("💲 Price: $99.99")
    elif lang == "ar":
        st.subheader("💲 السعر: 99.99 دولار")
    else:
        st.subheader("💲 Prix: 99.99 $")
    
    # زر تأكيد الصفقة
    if st.button("Confirm Deal / إتمام الصفقة / Confirmer l'offre"):
        st.success("✅ الصفقة تمت بنجاح!!")
        st.balloons()
        st.markdown("<h2 style='text-align:center; color:gold;'>⭐⭐⭐⭐⭐</h2>", unsafe_allow_html=True)
