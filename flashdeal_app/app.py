import streamlit as st
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
        "agent": "Smart Agent"
    },
    "ar": {
        "title": "فلاش ديل ستار",
        "welcome": "مرحبًا بك في فلاش ديل ستار",
        "tagline": "سهولة، أمان، ومرونة في كل صفقة",
        "get_started": "ابدأ الآن",
        "security": "مركز الأمان",
        "log": "سجل الصفقات",
        "agent": "الوكيل الذكي"
    },
    "fr": {
        "title": "FlashDeal Star",
        "welcome": "Bienvenue à FlashDeal Star",
        "tagline": "Simplicité, sécurité et flexibilité dans chaque transaction",
        "get_started": "Commencer",
        "security": "Centre de sécurité",
        "log": "Journal des transactions",
        "agent": "Agent intelligent"
    }
}

# اختيار اللغة
lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["en", "ar", "fr"])
t = translations[lang]

# واجهة رئيسية
st.markdown(f"<h1 style='text-align:center; color:#007AFF;'>{t['title']} ⚡⭐</h1>", unsafe_allow_html=True)
st.subheader(t["welcome"])
st.write(t["tagline"])

# زر البداية
if st.button(t["get_started"]):
    st.success("🚀 " + t["welcome"])

# أقسام إضافية
st.markdown("---")
st.header(t["security"])
st.write("✅ Face ID & Biometric enabled\n✅ Mutual Token System active")

st.header(t["log"])
st.write("📊 Recent transactions will appear here...")

st.header(t["agent"])
st.write("🤖 Your smart assistant is ready to help!")

# ✨ تأثير النجمة والبرق (محاكاة وميض متحرك)
placeholder = st.empty()
for i in range(5):
    placeholder.markdown(
        f"<h2 style='text-align:center; color:{'#FFD700' if i%2==0 else '#007AFF'};'>⭐ ⚡ FlashDeal Star is shining...</h2>",
        unsafe_allow_html=True
    )
    time.sleep(0.5)
