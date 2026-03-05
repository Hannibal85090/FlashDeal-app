import streamlit as st

# إعداد الترجمات
translations = {
    "en": {
        "title": "FlashDeal Star",
        "welcome": "Welcome to FlashDeal Star",
        "tagline": "Simplicity, security, and flexibility in every deal",
        "get_started": "Get Started"
    },
    "ar": {
        "title": "فلاش ديل ستار",
        "welcome": "مرحبًا بك في فلاش ديل ستار",
        "tagline": "سهولة، أمان، ومرونة في كل صفقة",
        "get_started": "ابدأ الآن"
    },
    "fr": {
        "title": "FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Simplicité, sécurité et flexibilité dans chaque transaction",
        "get_started": "Commencer"
    }
}

# اختيار اللغة
lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["en", "ar", "fr"])
t = translations[lang]

# واجهة التطبيق
st.title(t["title"])
st.subheader(t["welcome"])
st.write(t["tagline"])

# زر البداية
if st.button(t["get_started"]):
    st.success("🚀 " + t["welcome"])
