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
        "rating_label": "⭐ Choose your rating"
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
        "rating_label": "⭐ اختر تقييمك"
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
        "rating_label": "⭐ Choisissez votre évaluation"
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

# صفحة الأمان
elif page == t["security"]:
    st.header(t["security"])
    st.write("🔒 " + ("Facial & Biometric Authentication" if lang=="en" else "بصمة الوجه والبيومتري" if lang=="ar" else "Authentification faciale et biométrique"))
    st.write("🔑 " + ("Mutual Token System" if lang=="en" else "نظام التوكن المتبادل" if lang=="ar" else "Système de jeton mutuel"))
    st.write("🚗 " + ("FlashDeal Star Key" if lang=="en" else "مفتاح فلاش ديل ستار" if lang=="ar" else "Clé FlashDeal Star"))
    st.success("✅ " + ("Security system connected to encrypted token database." if lang=="en" else "نظام الأمان متصل بقاعدة بيانات التوكنات المشفرة." if lang=="ar" else "Système de sécurité connecté à la base de données des jetons chiffrés."))

# سجل الشفافية
elif page == t["log"]:
    st.header(t["log"])
    st.table({
        "Date": ["2026-03-04"],
        "Product": ["Wireless Headphones"],
        "Price": ["$99.99"],
        "Status": ["✅ " + ("Completed" if lang=="en" else "مكتمل" if lang=="ar" else "Terminé")]
    })

# إبرام الصفقة
elif page == t["deal"]:
    st.header(t["deal"])
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/22/Wireless_headphones.jpg", caption="Wireless Headphones")
    st.write("💲 " + ("Special Price: $99.99 (instead of $199.99)" if lang=="en" else "السعر الخاص: 99.99$ (بدلاً من 199.99$)" if lang=="ar" else "Prix spécial: 99.99$ (au lieu de 199.99$)"))
    if st.button("Confirm Deal / إتمام الصفقة فوراً / Confirmer l'offre"):
        st.success("✅ " + ("Deal Confirmed!" if lang=="en" else "تم تأكيد الصفقة!" if lang=="ar" else "Offre confirmée!"))

# الوكيل الذكي
elif page == t["agent"]:
    st.header(t["agent"])
    mode = st.radio("🎛 " + ("Choose interaction mode" if lang=="en" else "اختر نمط التفاعل" if lang=="ar" else "Choisissez le mode d'interaction"),
                    [t["voice"], t["gesture"], t["writing"]])
    if mode == t["voice"]:
        st.info("🎙 " + ("Smart agent is listening..." if lang=="en" else "الوكيل الذكي يستمع إليك..." if lang=="ar" else "L'agent intelligent écoute..."))
    elif mode == t["gesture"]:
        st.info("🖐️ " + ("Gesture interaction enabled." if lang=="en" else "تم تفعيل التفاعل بالإيماءات." if lang=="ar" else "Interaction gestuelle activée."))
    else:
        user_input = st.text_input("✍️ " + ("Write here to interact" if lang=="en" else "اكتب هنا للتفاعل" if lang=="ar" else "Écrivez ici pour interagir"))
        if user_input:
            st.success("🤖 " + ("Smart Agent: Received your message - " + user_input if lang=="en" else "الوكيل الذكي: استلم رسالتك - " + user_input if lang=="ar" else "Agent intelligent: Message reçu - " + user_input))

# مركز المساعدة
elif page == t["help"]:
    st.header(t["help"])
    st.write("❓ " + ("How can we help you today in FlashDeals?" if lang=="en" else "كيف يمكننا مساعدتك اليوم في بيئة فلاش ديلز؟" if lang=="ar" else "Comment pouvons-nous vous aider aujourd'hui dans FlashDeals?"))
    st.write("📌 " + ("How to use voice commands?" if lang=="en" else "كيفية استخدام الأوامر الصوتية؟" if lang=="ar" else "Comment utiliser les commandes vocales?"))
    st.write("📌 " + ("How to confirm a deal?" if lang=="en" else "كيفية تأكيد الصفقة؟" if lang=="ar" else "Comment confirmer une offre?"))

# تقييم المنتج
elif page == t["rate"]:
    st.header(t["rate"])
    rating = st.slider(t["rating_label"], 1, 7, 3)  # من 1 إلى 7 نجوم
    stars = "⭐" * rating + "☆" * (7 - rating)  # نجوم مضاءة ومطفأة
    st.markdown(f"<h2 style='color:red;'>{stars}</h2>", unsafe_allow_html=True)
    st.write(f"{'You rated the product' if lang=='en' else 'لقد قيّمت المنتج' if lang=='ar' else 'Vous avez évalué le produit'} {rating} {'stars' if lang=='en' else 'نجوم' if lang=='ar' else 'étoiles'}.")    rating = st.slider("⭐ Choose your rating", 1, 5, 3)
    st.write(f"You rated the product {rating} stars.")
