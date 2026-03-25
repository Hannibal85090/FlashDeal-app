import streamlit as st
import time
# استيراد الوكيل من ملفه الخاص الذي أنشأته
from sony_agent import render_sony_interface 

# --- إعدادات الصفحة ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

# --- تهيئة الذاكرة الموحدة ---
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- تنسيق الواجهة ---
st.markdown("""
<style>
    .star {font-size:80px; text-align:center; margin:10px 0;}
    .glass-card {padding:20px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(10px);}
    .log-text {font-size:0.8rem; color:#4facfe; font-family:'Courier New',monospace;}
</style>
""", unsafe_allow_html=True)

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.title("🌟 Control Hub")
    selected_lang = st.selectbox("🌐 Language", ["English", "Arabic"])
    st.divider()
    with st.expander("📜 Unified Memory Log", expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.markdown("<h1 style='text-align:center;'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>🕒 {time.strftime('%d/%m/%Y')}</p>", unsafe_allow_html=True)
st.markdown('<div class="star">★</div>', unsafe_allow_html=True)

# --- استدعاء الوكيل صوني (المحرك الخارجي) ---
# قمنا بتمرير دالة الذاكرة ليبقى صوني متصلاً بسجل العمليات
st.divider()
render_sony_interface(add_to_memory) 
st.divider()

# --- بقية وظائف النظام (Smart Controls) ---
st.subheader("🏠🚗 Smart Control Dashboard")
c1, c2 = st.columns(2)
with c1:
    if st.button("Start Car 🔑"):
        st.success("🚗 Engine On!"); add_to_memory("Car Started")
with c2:
    if st.button("Manage Home 🏠"):
        st.toast("🏠 Home Secure"); add_to_memory("Home Managed")

# --- تنفيذ الصفقة ---
st.divider()
if st.button("Global Deal Execution 🚀", type="primary", use_container_width=True):
    st.balloons()
    add_to_memory("Deal Concluded Successfully")
    st.success("Transaction Validated by Sony AI Agent ✅")

# --- التعرف البيومتري ---
st.divider()
st.subheader("👤 Identity Verification")
img = st.camera_input("Verify for Pitch Day")
if img:
    st.success("Identity Confirmed ✅"); add_to_memory("Face ID Verified")

