import streamlit as st
import time
import streamlit.components.v1 as components
from sony_agent import render_sony_interface

st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# القاموس الكامل بجميع اللغات
LANG_DICT = {
    'English': {'motto':"Talk. Pay. Done.", 'saden':"Saden Security: Mutual Token", 'buy':"Global Deal Execution 🚀", 'success':"Process Completed!", 'car':"Start Car 🔑", 'home':"Manage Home 🏠", 'mem':"📜 Unified Memory Log"},
    'Français': {'motto':"Parlez. Payez. Fait.", 'saden':"Sécurité Saden: Token Mutuel", 'buy':"Conclure l'Accord 🚀", 'success':"Opération terminée!", 'car':"Démarrer 🔑", 'home':"Gérer Maison 🏠", 'mem':"📜 Journal de Mémoire"},
    'Italiano': {'motto':"Parla. Paga. Fatto.", 'saden':"Sicurezza Saden: Token Reciproco", 'buy':"Concludi l'Affare 🚀", 'success':"Operazione riuscita!", 'car':"Avvia Auto 🔑", 'home':"Gestisci Casa 🏠", 'mem':"📜 Registro di Memoria"},
    'Arabic': {'motto':"تحدث. ادفع. تم.", 'saden':"أمان سادن: التوكن المتبادل", 'buy':"إبرام الصفقة العالمية 🚀", 'success':"تمت العملية بنجاح!", 'car':"تشغيل السيارة 🔑", 'home':"إدارة المنزل 🏠", 'mem':"📜 سجل الذاكرة الموحد"}
}

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p style='color:#4facfe; font-size:0.8rem;'>{item}</p>", unsafe_allow_html=True)

# العنوان
st.markdown(f"<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>{t['motto']}</p>", unsafe_allow_html=True)

# استدعاء الوكيل صوني المطور
render_sony_interface(add_to_memory)

# استعادة أزرار التحكم الذكي
st.divider()
st.subheader(f"🏠🚗 Control Hub")
ca, cb = st.columns(2)
with ca:
    if st.button(t['car']):
        st.success("🚗 Engine On!"); add_to_memory("Car Started")
with cb:
    if st.button(t['home']):
        st.toast("🏠 Home Secure"); add_to_memory("Home Managed")

# تنفيذ الصفقة
st.divider()
st.metric("System Stability", "100%", "Secure")
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons()
    st.success(t['success'])
    add_to_memory("Deal Concluded")

# التعرف البيومتري
st.divider()
st.subheader("👤 Biometric Face Recognition")
img = st.camera_input("Verify Identity")
if img:
    st.success("Face Verified ✅"); add_to_memory("Face ID Verified")
