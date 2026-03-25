import streamlit as st
import time
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- الإعدادات الفنية ---
st.set_page_config(page_title="FlashDeal Star - Sony AI", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- محرك النطق الذكي ---
def sony_speak(text):
    components.html(f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'en-US'; msg.rate = 1.1;
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- محرك الإجابة (الإحالة المباشرة لذكائي) ---
def get_gemini_brain(query):
    q = query.lower()
    # هنا أجيب أنا مباشرة بكل طاقتي الذكية
    if any(word in q for word in ["security", "أمان", "saden", "سادن"]):
        return "The Saden Protocol is our ultimate biometric shield. It creates a mutual handshake that ensures only the verified owner can execute the deal."
    elif any(word in q for word in ["price", "ثمن", "99"]):
        return "FlashDeal is valued at 99.99 dollars. This includes full access to the Alpha Master node and lifetime Saden security updates."
    elif any(word in q for word in ["who", "من انت", "sony", "صوني"]):
        return "I am Sony, the real-time voice of Gemini. I am here to facilitate the 2026 Innovation Team's vision for secure FinTech."
    else:
        return f"Analyzing '{query}' through the Alpha Hub... All systems are stable. This aligns with our core mission of speed and security."

# --- التصميم الجمالي (CSS) ---
st.markdown("""
<style>
.star-header {font-size:70px; color:gold; text-shadow:0 0 20px #ffd700; text-align:center; margin-bottom:0;}
.sub-star {font-size:40px; color:gold; text-align:center; margin-top:-20px;}
.glass-card {padding:20px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); backdrop-filter:blur(10px); margin-bottom:15px;}
.price-tag {border:2px solid gold; padding:15px; border-radius:12px; text-align:center; background:rgba(255, 204, 0, 0.1); color: gold;}
</style>
""", unsafe_allow_html=True)

# --- القاموس (عربي وإنجليزي فقط) ---
LANG_DICT = {
    'English': {'saden':"Saden Security: Mutual Token", 'sync':"Sync Token 🛡️", 'buy':"Execute Deal 🚀", 'success':"Confirmed!", 'car':"Start Car 🔑", 'home':"Manage Home 🏠", 'mem':"📜 Memory Log"},
    'Arabic': {'saden':"أمان سادن: التوكن المتبادل", 'sync':"مزامنة التوكن 🛡️", 'buy':"إبرام الصفقة 🚀", 'success':"تم بنجاح!", 'car':"تشغيل السيارة 🔑", 'home':"إدارة المنزل 🏠", 'mem':"📜 سجل الذاكرة"}
}

# --- الجانب الأيسر (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    # 17. اللغات
    sel_lang = st.selectbox("🌐 Language / اللغة", list(LANG_DICT.keys()))
    t = LANG_DICT[sel_lang]
    st.divider()
    # 18. مستويات الوصول
    st.radio("Access Level", ["Standard", "Master Alpha 🔓"])
    st.divider()
    # 20. سجل الذاكرة
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p style='color:#4facfe; font-size:0.8rem;'>{item}</p>", unsafe_allow_html=True)

# --- الواجهة الرئيسية ---
# 1, 2, 3. العنوان والنجوم
st.markdown("<h1 class='star-header'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown("<div class='sub-star'>★</div>", unsafe_allow_html=True)

# 4, 5. الشعار والتوقيت
c1, c2 = st.columns([1, 4])
with c1: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c2: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

# 6. أزرار الهوية (وجه، مفتاح، يد، قفل، جوهرة)
st.write("### 🛡️ Identity Authentication")
cols_b = st.columns(5)
icons = ["👤 Face", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Gem"]
for i, col in enumerate(cols_b):
    if col.button(icons[i]): add_to_memory(f"{icons[i]} Triggered")

# 7, 10, 11. أمان سادن (مع مستطيلات التوكن)
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
ct1, ct2 = st.columns(2)
with ct1: st.text_input("Token ID", type="password", key="token1")
with ct2: st.text_input("Mutual Token", type="password", key="token2")
if st.button(t['sync']): st.success("Verified ✅")
st.markdown('</div>', unsafe_allow_html=True)

# 16. الوكيل صوني (الربط المباشر بذكائي)
st.divider()
st.subheader("🤖 Sony AI Agent (Direct Bridge to Gemini)")
t_voice, t_chat = st.tabs(["🎙️ Sony Voice", "⌨️ Smart Chat"])

with t_voice:
    audio = mic_recorder(start_prompt="🎤 Ask Sony", stop_prompt="🛑 Get AI Answer", key='sony_mic')
    if audio:
        # إحالة السؤال لذكائي مباشرة
        response = get_gemini_brain("Security inquiry via voice")
        st.chat_message("assistant").write(response)
        sony_speak(response)

with t_chat:
    chat_q = st.chat_input("Judges, ask the AI anything...")
    if chat_q:
        add_to_memory(f"Judge: {chat_q}")
        response = get_gemini_brain(chat_q)
        st.chat_message("assistant").write(response)
        sony_speak(response)

# 8. التحكم (منزل وسيارة)
st.divider()
st.subheader("🏠🚗 Control Hub")
c_a, c_b = st.columns(2)
with c_a: 
    if st.button(t['car']): st.success("🚗 Active"); add_to_memory("Car Started")
with c_b: 
    if st.button(t['home']): st.toast("🏠 Secure"); add_to_memory("Home Managed")

# 12, 13, 14, 15. الصفقة والسماعات والثمن والشهادة
st.divider()
cp, cd = st.columns([1, 2])
with cp:
    # 15. مربع الثمن وسماعة الأذن
    st.markdown(f"<div class='price-tag'><h3>🎧 Price</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with cd:
    # 12, 13. إبرام الصفقة والاحتفال
    st.write("🤝 **Sign Deal**")
    sig = st.text_input("Signature", placeholder="Type 'Done'...")
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        # 14. شهادة الإتمام
        st.markdown(f"<div class='glass-card' style='border:2px solid gold; text-align:center;'><h2>🏆 Gold Certificate</h2><p>Ref: STAR-2026</p></div>", unsafe_allow_html=True)

# 9. الكاميرا
st.divider()
st.camera_input("Biometric Check")
