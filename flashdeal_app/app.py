import streamlit as st
import time

# الترجمات
translations = {
    "en": {
        "title": "⚡⭐ FlashDeal Star",
        "welcome": "Welcome to FlashDeal Star",
        "tagline": "Discover amazing deals on your favorite products!",
        "get_started": "Get Started",
        "security": "Comprehensive Security Center",
        "log": "Transparency Log",
        "deal": "Deal Execution",
        "agent": "Smart Agent",
        "help": "Help Center",
        "rate": "Rate Product"
    },
    "ar": {
        "title": "⚡⭐ فلاش ديل ستار",
        "welcome": "مرحبًا بك في فلاش ديل ستار",
        "tagline": "اكتشف أفضل العروض على منتجاتك المفضلة!",
        "get_started": "ابدأ الآن",
        "security": "مركز الأمان الشامل",
        "log": "سجل الشفافية",
        "deal": "إبرام الصفقة",
        "agent": "الوكيل الذكي",
        "help": "مركز المساعدة",
        "rate": "قيّم المنتج"
    },
    "fr": {
        "title": "⚡⭐ FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Découvrez des offres incroyables sur vos produits préférés!",
        "get_started": "Commencer",
        "security": "Centre de sécurité complet",
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
    # تأثير النجمة والبرق
    placeholder = st.empty()
    for i in range(6):
        placeholder.markdown(
            f"<h3 style='text-align:center; color:{'#FFD700' if i%2==0 else '#007AFF'};'>⭐ ⚡ FlashDeal Star is shining...</h3>",
            unsafe_allow_html=True
        )
        time.sleep(0.4)

# صفحة الأمان
elif page == t["security"]:
    st.header(t["security"])
    st.write("🔒 بصمة الوجه والبيومتري")
    st.write("🔑 نظام التوكن المتبادل")
    st.write("🚗 مفتاح السيارة الذكي")

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
    st.write("💲 أفضل سعر متاح: $99.99 (بدلاً من $199.99)")
    if st.button("Confirm Deal / إتمام الصفقة فوراً"):
        st.success("✅ Deal Confirmed!")

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
    st.write("❓ كيف يمكننا مساعدتك اليوم في بيئة FlashDeals؟")
    st.write("📌 كيفية استخدام الأمر الصوتي؟")
    st.write("📌 كيفية تأكيد الصفقة؟")

# تقييم المنتج
elif page == t["rate"]:
    st.header(t["rate"])
    rating = st.slider("⭐ اختر تقييمك", 1, 5, 3)
    st.write(f"لقد قيّمت المنتج بـ {rating} نجوم.")
