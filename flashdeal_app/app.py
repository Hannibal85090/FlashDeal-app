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
        "rate": "Rate Product"
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
        "rate": "قيّم المنتج"
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
        "rate": "Évaluer le produit"
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
    st.write("🔒 Facial & Biometric Authentication")
    st.write("🔑 Mutual Token System")
    st.write("🚗 FlashDeal Star Key")
    st.success("✅ Security system connected to encrypted token database.")

# سجل الشفافية
elif page == t["log"]:
    st.header(t["log"])
    st.table({
        "Date": ["2026-03-04"],
        "Product": ["Wireless Headphones"],
        "Price": ["$99.99"],
        "Status": ["✅ Completed"]
    })

# إبرام الصفقة
elif page == t["deal"]:
    st.header(t["deal"])
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/22/Wireless_headphones.jpg", caption="Wireless Headphones")
    st.write("💲 Special Price: $99.99 (instead of $199.99)")
    if st.button("Confirm Deal / إتمام الصفقة فوراً"):
        st.success("✅ Deal Confirmed!")

# الوكيل الذكي
elif page == t["agent"]:
    st.header(t["agent"])
    mode = st.radio("🎛 اختر نمط التفاعل", ["🎤 Voice", "🖐️ Gesture", "✍️ Writing"])
    if mode == "🎤 Voice":
        st.info("🎙 The smart agent is listening...")
    elif mode == "🖐️ Gesture":
        st.info("🖐️ Gesture interaction enabled.")
    else:
        user_input = st.text_input("✍️ Write here to interact with the smart agent")
        if user_input:
            st.success(f"🤖 Smart Agent: Received your message - '{user_input}'")

# مركز المساعدة
elif page == t["help"]:
    st.header(t["help"])
    st.write("❓ How can we help you today in FlashDeals?")
    st.write("📌 How to use voice commands?")
    st.write("📌 How to confirm a deal?")

# تقييم المنتج
elif page == t["rate"]:
    st.header(t["rate"])
    rating = st.slider("⭐ Choose your rating", 1, 5, 3)
    st.write(f"You rated the product {rating} stars.")
