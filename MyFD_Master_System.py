import streamlit as st
import time

# --- ١. إعدادات الصفحة ---
st.set_page_config(page_title="MyFD Master System", layout="wide")

# --- ٢. قاموس اللغات الاحترافي ---
translations = {
    "العربية": {
        "title": "⚡ ⭐ نظام ماستر فلاش ديل",
        "agent": "الوكيل الذكي",
        "sync": "تفعيل المزامنة",
        "deal": "🤝 إبرام الصفقة العالمية",
        "success": "تمت العملية بنجاح! مبروك",
        "cert": "شهادة الإتمام النهائية",
        "token_label": "نظام التوكن المتبادل"
    },
    "English": {
        "title": "⚡ ⭐ My FlashDeal Master System",
        "agent": "Smart Agent",
        "sync": "Sync Now",
        "deal": "🤝 Execute Global Deal",
        "success": "Transaction Successful! Congrats.",
        "cert": "Final Completion Certificate",
        "token_label": "Mutual Token System"
    },
    "Italiano": {
        "title": "⚡ ⭐ MyFD Sistema Master",
        "agent": "Agente Intelligente",
        "sync": "Sincronizza Ora",
        "deal": "🤝 Concludi l'Affare",
        "success": "Transazione Riuscita! Congratulazioni.",
        "cert": "Certificato di Completamento",
        "token_label": "Sistema Token Mutuo"
    },
    "Français": {
        "title": "⚡ ⭐ Système Master MyFD",
        "agent": "Agent Intelligent",
        "sync": "Synchroniser",
        "deal": "🤝 Conclure l'Affaire",
        "success": "Transaction Réussie ! Félicitations.",
        "cert": "Certificat d'Achèvement",
        "token_label": "Système de Jeton Mutuel"
    }
}

# --- ٣. اختيار اللغة وتحديث الواجهة ---
selected_lang = st.sidebar.selectbox("Language / اللغة", list(translations.keys()))
t = translations[selected_lang] # هذا هو المتغير السحري الذي سيحدث كل شيء

# --- ٤. تطبيق النصوص الديناميكية ---
st.markdown(f"<h1 style='text-align: center;'>{t['title']}</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(f"### 🔐 {t['token_label']}")
    if st.button(t['sync']):
        st.success("Sync OK! ✅")

# تبويبات الوكيل
st.subheader(t['agent'])
t1, t2, t3 = st.tabs(["🎤 Voice", "👋 Sign", "⌨️ Text"])
with t3:
    st.chat_input(f"{t['agent']}...")

# لحظة الحسم والاحتفالية
st.divider()
if st.button(t['deal'], use_container_width=True):
    st.balloons()
    st.snow()
    st.success(t['success'])
    st.write(f"**{t['cert']}:** MASTER-{int(time.time())}")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
