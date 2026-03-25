import streamlit as st
import time
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- الإعدادات الأساسية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- محرك صوت صوني ---
def sony_speak(text):
    components.html(f"""<script>var msg = new SpeechSynthesisUtterance('{text}'); msg.lang = 'en-US'; window.speechSynthesis.speak(msg);</script>""", height=0)

# --- التنسيق البصري الاحترافي ---
st.markdown("""
<style>
.star-header {font-size:75px; color:gold; text-shadow:0 0 20px #ffd700; text-align:center; margin-bottom:0;}
.sub-star {font-size:45px; color:gold; text-align:center; margin-top:-20px;}
.glass-card {padding:20px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(10px); margin-bottom:15px;}
.price-tag {border:2px solid gold; padding:10px; border-radius:10px; text-align:center; background:rgba(255,204,0,0.1);}
</style>
""", unsafe_allow_html=True)

# --- القاموس اللغوي المصحح (تجنب KeyError) ---
LANG_DICT = {
    'English': {'motto':"Talk. Pay. Done.", 'saden':"Saden Security: Mutual Token", 'sync':"Sync Token 🛡️", 'buy':"Global Deal Execution 🚀", 'success':"Process Completed!", 'car':"Start Car 🔑", 'home':"Manage Home 🏠", 'mem':"📜 Unified Memory Log", 'cert':"Completion Certificate"},
    'Français': {'motto':"Parlez. Payez. Fait.", 'saden':"Sécurité Saden: Token Mutuel", 'sync':"Synchroniser 🛡️", 'buy':"Conclure l'Accord 🚀", 'success':"Opération terminée!", 'car':"Démarrer 🔑", 'home':"Gérer Maison 🏠", 'mem':"📜 Journal de Mémoire", 'cert':"Certificat de réussite"},
    'Italiano': {'motto':"Parla. Paga. Fatto.", 'saden':"Sicurezza Saden: Token Reciproco", 'sync':"Sincronizza 🛡️", 'buy':"Concludi l'Affare 🚀", 'success':"Operazione riuscita!", 'car':"Avvia Auto 🔑", 'home':"Gestisci Casa 🏠", 'mem':"📜 Registro di Memoria", 'cert':"Certificato di completamento"},
    'Arabic': {'motto':"تحدث. ادفع. تم.", 'saden':"أمان سادن: التوكن المتبادل", 'sync':"مزامنة التوكن 🛡️", 'buy':"إبرام الصفقة العالمية 🚀", 'success':"تمت العملية بنجاح!", 'car':"تشغيل السيارة 🔑", 'home':"إدارة المنزل 🏠", 'mem':"📜 سجل الذاكرة الموحد", 'cert':"شهادة إتمام الصفقة"}
}

# --- الجانب الأيسر (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Choose Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.divider()
    acc_mode = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p style='color:#4facfe; font-size:0.8rem;'>{item}</p>", unsafe_allow_html=True)

# --- 1, 2, 3: العنوان والنجوم ---
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-star'>★</div>", unsafe_allow_html=True)

# 4, 5: الشعار والتوقيت
c_l, c_t = st.columns([1, 4])
with c_l: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c_t: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

# 6: أزرار الهوية (وجه، مفتاح، يد، قفل، جوهرة)
st.write("### 🛡️ Secure Identity Links")
b1, b2, b3, b4, b5 = st.columns(5)
if b1.button("👤 Face"): add_to_memory("Face ID Check")
if b2.button("🔑 Key"): add_to_memory("Key Engaged")
if b3.button("✋ Hand"): add_to_memory("Hand Gesture Synced")
if b4.button("🔒 Lock"): add_to_memory("System Locked")
if b5.button("💎 Gem"): add_to_memory("Premium Access")

# 7, 10, 11: أمان سادن ومستطيلات التوكن (عين الإخفاء)
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
col_in1, col_in2 = st.columns(2)
with col_in1: st.text_input("Token ID", type="password", key="t1")
with col_in2: st.text_input("Mutual Token", type="password", key="t2")
if st.button(t['sync']): st.success("Linked! ✅"); add_to_memory("Token Synced")
st.markdown('</div>', unsafe_allow_html=True)

# 16: الوكيل صوني Sony
st.divider()
st.subheader("🤖 Sony AI Agent Center")
t_v, t_t = st.tabs(["🎙️ Sony Voice", "⌨️ Smart Chat"])
with t_v:
    audio = mic_recorder(start_prompt="🎤 Ask Sony", stop_prompt="🛑 Stop", key='sony_mic')
    if audio:
        msg = "I am Sony. Analyzing your biometric data. System is secure."
        st.chat_message("assistant").write(msg); sony_speak(msg)
with t_t:
    chat_val = st.chat_input("Sony-Agent...")
    if chat_val:
        resp = f"Analyzing: {chat_val}. Status: Verified ✅"
        st.chat_message("assistant").write(resp); sony_speak(resp)

# 8: التحكم في المنزل والسيارة
st.divider()
st.subheader("🏠🚗 Control Hub")
ca, cb = st.columns(2)
with ca: 
    if st.button(t['car']): st.success("🚗 Engine On!"); add_to_memory("Car Started")
with cb: 
    if st.button(t['home']): st.toast("🏠 Home Managed"); add_to_memory("Home Managed")

# 12, 13, 14, 15: الصفقة، التصافح، الاحتفال، الشهادة، الثمن
st.divider()
col_p, col_d = st.columns([1, 2])
with col_p:
    st.markdown(f"<div class='price-tag'><h3>🎧 Price</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
    st.metric("System Stability", "100%", "Secure")
with col_d:
    st.write("🤝 **Agreement Protocol**")
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        st.success(t['success'])
        st.markdown(f"<div class='glass-card' style='text-align:center; border:2px solid gold;'><h2>🏆 {t['cert']}</h2><p>ID: STAR-{int(time.time())}</p></div>", unsafe_allow_html=True)

# 9: الكاميرا
st.divider()
st.subheader("👤 Biometric Face Recognition")
st.camera_input("Verify Master Alpha Identity")
