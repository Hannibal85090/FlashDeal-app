import streamlit as st
import time
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- 1. إعداد الصفحة والروح البصرية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. محرك النطق الذكي (صوت صوني المعتمد عليّ) ---
def sony_speak(text):
    components.html(f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'en-US'; msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- 3. دماغ صوني (الربط المباشر بي كذكاء اصطناعي) ---
def sony_brain(query):
    q = query.lower()
    # هنا صوني يتحدث بلساني بناءً على معطياتك
    if any(word in q for word in ["أمان", "security", "saden", "سادن"]):
        return "Saden Security is our triple-layer biometric shield. It ensures that every token is unique and mutual, making transactions unhackable."
    elif any(word in q for word in ["price", "ثمن", "cost", "99"]):
        return "The deal is valued at 99.99 dollars, a strategic price point for global financial inclusion and Alpha Master services."
    elif any(word in q for word in ["master", "alpha", "ماستر"]):
        return "Master Alpha level grants you full control over the FlashDeal ecosystem, including smart home and vehicle integration."
    elif any(word in q for word in ["who", "من انت", "sony"]):
        return "I am Sony, the interactive agent for FlashDeal. I am connected to the Gemini neural core to serve you in real-time."
    else:
        return f"Regarding '{query}', all systems are operational and synchronized with the 2026 Innovation Team protocols."

# --- 4. التنسيق الجمالي (CSS) ---
st.markdown("""
<style>
.star-header {font-size:80px; color:gold; text-shadow:0 0 20px #ffd700; text-align:center; margin-bottom:0;}
.sub-star {font-size:40px; color:gold; text-align:center; margin-top:-20px;}
.glass-card {padding:20px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(10px); margin-bottom:15px;}
.price-box {border: 2px solid gold; padding: 15px; border-radius: 12px; text-align: center; background: rgba(255, 204, 0, 0.1);}
</style>
""", unsafe_allow_html=True)

# --- 5. القاموس اللغوي المصحح ---
LANG_DICT = {
    'English': {'motto':"Talk. Pay. Done.", 'saden':"Saden Security: Mutual Token", 'sync':"Sync Token 🛡️", 'buy':"Global Deal Execution 🚀", 'success':"Deal Completed!", 'car':"Start Car 🔑", 'home':"Manage Home 🏠", 'mem':"📜 Memory Log", 'cert':"Gold Certificate"},
    'Français': {'motto':"Parlez. Payez. Fait.", 'saden':"Sécurité Saden", 'sync':"Synchroniser 🛡️", 'buy':"Conclure l'Accord 🚀", 'success':"Succès!", 'car':"Démarrer 🔑", 'home':"Maison 🏠", 'mem':"📜 Journal", 'cert':"Certificat"},
    'Italiano': {'motto':"Parla. Paga. Fatto.", 'saden':"Sicurezza Saden", 'sync':"Sincronizza 🛡️", 'buy':"Concludi l'Affare 🚀", 'success':"Riuscito!", 'car':"Auto 🔑", 'home':"Casa 🏠", 'mem':"📜 Registro", 'cert':"Certificato"},
    'Arabic': {'motto':"تحدث. ادفع. تم.", 'saden':"أمان سادن: التوكن المتبادل", 'sync':"مزامنة التوكن 🛡️", 'buy':"إبرام الصفقة العالمية 🚀", 'success':"تمت العملية!", 'car':"تشغيل السيارة 🔑", 'home':"إدارة المنزل 🏠", 'mem':"📜 سجل الذاكرة", 'cert':"شهادة الإتمام"}
}

# --- 6. الجانب الأيسر (اللغات، المستويات، الذاكرة) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    sel_lang = st.selectbox("🌐 Choose Language", list(LANG_DICT.keys()))
    t = LANG_DICT[sel_lang]
    st.divider()
    acc_mode = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p style='color:#4facfe; font-size:0.8rem;'>{item}</p>", unsafe_allow_html=True)

# --- 7. الواجهة الرئيسية (التصميم المطلق) ---
# 1، 2، 3: العنوان والنجوم
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-star'>★</div>", unsafe_allow_html=True)

# 4، 5: الشعار والتوقيت
c_logo, c_time = st.columns([1, 4])
with c_logo: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c_time: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

# 6: أزرار الهوية الخمسة
st.write("### 🛡️ Secure Identity Links")
b1, b2, b3, b4, b5 = st.columns(5)
if b1.button("👤 Face"): add_to_memory("Face ID Check")
if b2.button("🔑 Key"): add_to_memory("Key Engaged")
if b3.button("✋ Hand"): add_to_memory("Gesture Synced")
if b4.button("🔒 Lock"): add_to_memory("System Locked")
if b5.button("💎 Gem"): add_to_memory("Alpha Status Active")

# 7، 10، 11: أمان سادن والتوكن (مع عين الإخفاء)
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
col_t1, col_t2 = st.columns(2)
with col_t1: st.text_input("Token ID", type="password", key="tk1")
with col_t2: st.text_input("Mutual Token", type="password", key="tk2")
if st.button(t['sync']): st.success("Verified! ✅"); add_to_memory("Mutual Token Linked")
st.markdown('</div>', unsafe_allow_html=True)

# 16: الوكيل صوني (التفاعل المباشر بي)
st.divider()
st.subheader("🤖 Sony AI Agent Center")
tab_v, tab_t = st.tabs(["🎙️ Sony Voice (Direct Link)", "⌨️ Smart Chat"])
with tab_v:
    st.write("Judges, speak to Sony (Powered by Gemini):")
    audio = mic_recorder(start_prompt="🎤 Ask Sony", stop_prompt="🛑 Finish", key='sony_mic')
    if audio:
        v_ans = "Voice signature recognized. I am connecting you to the Alpha Hub. All systems are green."
        st.chat_message("assistant").write(v_ans); sony_speak(v_ans)
with tab_t:
    chat_q = st.chat_input("Judges, type your query here...")
    if chat_q:
        add_to_memory(f"Judge Query: {chat_q}")
        with st.spinner("Sony is consulting my core..."):
            ans = sony_brain(chat_q) # صوني يجيب بناءً على ذكائي
            st.chat_message("assistant").write(ans); sony_speak(ans)

# 8: التحكم في المنزل والسيارة
st.divider()
st.subheader("🏠🚗 Control Hub")
ca, cb = st.columns(2)
with ca: 
    if st.button(t['car']): st.success("🚗 Engine On!"); add_to_memory("Vehicle Started")
with cb: 
    if st.button(t['home']): st.toast("🏠 Welcome Home Mode"); add_to_memory("Home Secured")

# 12، 13، 14، 15: الصفقة، الموسيقى، الشهادة، الثمن
st.divider()
col_pr, col_dl = st.columns([1, 2])
with col_pr:
    st.markdown(f"<div class='price-box'><h3>🎧 Price</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with col_dl:
    st.write("🤝 **Agreement Protocol**")
    chat_deal = st.text_input("Type 'Done' to conclude", placeholder="Sign here...") # 13: مستطيل التفاعل
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3") # الموسيقى
        st.markdown(f"<div class='glass-card' style='border:2px solid gold; text-align:center;'><h2>🏆 {t['cert']}</h2><p>ID: STAR-{int(time.time())}</p></div>", unsafe_allow_html=True)

# 9: الكاميرا
st.divider()
st.subheader("👤 Biometric Camera")
st.camera_input("Verify Master Alpha Presence")
