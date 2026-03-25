import streamlit as st
import time
import random
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- 1. إعدادات الهوية والذاكرة ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. قاموس اللغات الشامل (ترجمة كل تفصيلة) ---
LANG_DICT = {
    'English': {
        'title': "🌟 My FlashDeal Star 🌟",
        'auth_title': "🛡️ Identity Authentication",
        'icons': ["👤 Face", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Gem"],
        'saden_title': "🔒 Saden Security: Mutual Token",
        'sync_btn': "Sync Saden 🛡️",
        'agent_title': "🤖 Sony AI Agent (Powered by Gemini)",
        'voice_tab': "🎙️ Sony Voice",
        'chat_tab': "⌨️ Interactive Chat",
        'chat_placeholder': "Judges, ask Sony anything...",
        'ctrl_title': "🏠🚗 Control Hub",
        'car_btn': "Start Engine 🔑",
        'home_btn': "Manage Home 🏠",
        'price_label': "🎧 Price",
        'deal_title': "🤝 Agreement Protocol",
        'sig_placeholder': "Sign to seal...",
        'buy_btn': "EXECUTE DEAL 🚀",
        'cert_title': "🏆 Gold Certificate",
        'mem_title': "📜 Unified Memory Log",
        'acc_label': "Access Level",
        'cam_title': "👤 Biometric Verification"
    },
    'Arabic': {
        'title': "🌟 نجم فلاش ديل الخاص بي 🌟",
        'auth_title': "🛡️ توثيق الهوية الرقمية",
        'icons': ["👤 الوجه", "🔑 المفتاح", "✋ اليد", "🔒 القفل", "💎 الجوهرة"],
        'saden_title': "🔒 أمان سادن: التوكن المتبادل",
        'sync_btn': "مزامنة سادن 🛡️",
        'agent_title': "🤖 الوكيل الذكي صوني (بمحرك جمناي)",
        'voice_tab': "🎙️ صوني صوتياً",
        'chat_tab': "⌨️ محادثة ذكية",
        'chat_placeholder': "أيها الحكام، اسألوا صوني عن أي شيء...",
        'ctrl_title': "🏠🚗 مركز التحكم عن بعد",
        'car_btn': "تشغيل المحرك 🔑",
        'home_btn': "إدارة المنزل 🏠",
        'price_label': "🎧 الثمن",
        'deal_title': "🤝 بروتوكول الاتفاقية",
        'sig_placeholder': "وقع هنا لإتمام الصفقة...",
        'buy_btn': "إبرام الصفقة العالمية 🚀",
        'cert_title': "🏆 شهادة الإتمام الذهبية",
        'mem_title': "📜 سجل الذاكرة الموحد",
        'acc_label': "مستوى الوصول",
        'cam_title': "👤 التحقق البيومتري البصري"
    }
}

# --- 3. محرك النطق (صوني المتحدث) ---
def sony_speak(text, lang='en-US'):
    # تحديد لغة النطق بناءً على الاختيار
    voice_lang = 'ar-SA' if lang == 'Arabic' else 'en-US'
    components.html(f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = '{voice_lang}';
        msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- 4. ذكاء صوني (إجابات متغيرة ومترجمة) ---
def get_ai_response(query, lang):
    q = query.lower()
    if lang == 'Arabic':
        if any(word in q for word in ["أمان", "سادن"]):
            return "بروتوكول سادن هو درعنا الحي؛ إنه مصافحة رقمية تضمن عدم إتمام أي صفقة إلا بهوية Master Alpha."
        return f"بناءً على سؤالك '{query}'، النظام مستقر بنسبة 100% وجاهز للانطلاق."
    else:
        if any(word in q for word in ["security", "saden"]):
            return "Saden is a living security protocol that fuses biometric intent with mutual tokens."
        return f"Regarding '{query}', the Alpha Hub confirms all protocols are synchronized for 2026."

# --- 5. التصميم الجمالي (CSS) ---
st.markdown("""
<style>
body {background: #00050a; color: white;}
.star-header {font-size: 65px; color: gold; text-shadow: 0 0 20px #ffd700; text-align: center;}
.glass-card {padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); margin-bottom: 15px;}
.price-tag {border: 2px solid gold; padding: 10px; border-radius: 12px; text-align: center; background: rgba(255, 204, 0, 0.1); color: gold;}
</style>
""", unsafe_allow_html=True)

# --- 6. الواجهة الجانبية (تعريب كامل) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    sel_lang = st.selectbox("🌐 Language / اللغة", ["English", "Arabic"])
    t = LANG_DICT[sel_lang]
    st.divider()
    st.radio(t['acc_label'], ["* Standard", "Master Alpha 🔓"])
    st.divider()
    st.write(t['mem_title'])
    for item in reversed(st.session_state.history):
        st.markdown(f"<p style='color:#4facfe; font-size:0.75rem;'>{item}</p>", unsafe_allow_html=True)

# --- 7. الواجهة الرئيسية (تحقيق الـ 20 شرطاً بالتعريب الكامل) ---

# 1، 2، 3: العناوين والنجوم
st.markdown(f"<h1 class='star-header'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown("<div style='font-size:40px; color:gold; text-align:center; margin-top:-20px;'>★</div>", unsafe_allow_html=True)

# 4، 5: الشعار والوقت
c_l, c_t = st.columns([1, 4])
with c_l: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c_t: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

# 6: أزرار الهوية الخمسة (معربة)
st.write(f"### {t['auth_title']}")
cols_auth = st.columns(5)
for i, col in enumerate(cols_auth):
    if col.button(t['icons'][i]): add_to_memory(f"{t['icons'][i]} Verified")

# 7، 10، 11: أمان سادن
st.markdown(f'<div class="glass-card"><h3>{t["saden_title"]}</h3>', unsafe_allow_html=True)
ct1, ct2 = st.columns(2)
with ct1: st.text_input("Token ID", type="password", key="tk1")
with ct2: st.text_input("Mutual Token", type="password", key="tk2")
if st.button(t['sync_btn']): st.success("Verified ✅")
st.markdown('</div>', unsafe_allow_html=True)

# 16: الوكيل صوني (تفاعل ذكي مترجم)
st.divider()
st.subheader(t['agent_title'])
tab_v, tab_c = st.tabs([t['voice_tab'], t['chat_tab']])

with tab_v:
    if st.button("🎤 Start Sony"): 
        ans = get_ai_response("Voice", sel_lang)
        st.write(ans); sony_speak(ans, sel_lang)

with tab_c:
    q = st.chat_input(t['chat_placeholder'])
    if q:
        add_to_memory(f"Judge: {q}")
        ans = get_ai_response(q, sel_lang)
        st.chat_message("assistant").write(ans)
        sony_speak(ans, sel_lang)

# 8: التحكم (معرب)
st.divider()
st.subheader(t['ctrl_title'])
ca, cb = st.columns(2)
if ca.button(t['car_btn']): st.success("🚗 Online"); add_to_memory("Car Started")
if cb.button(t['home_btn']): st.toast("🏠 Secure"); add_to_memory("Home Managed")

# 12، 13، 14، 15: الصفقة والشهادة
st.divider()
cp, cd = st.columns([1, 2])
with cp:
    st.markdown(f"<div class='price-tag'><h3>{t['price_label']}</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with cd:
    st.write(f"### {t['deal_title']}")
    st.text_input("Signature", placeholder=t['sig_placeholder'])
    if st.button(t['buy_btn'], type="primary", use_container_width=True):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        st.markdown(f"<div class='glass-card' style='border:2px solid gold; text-align:center;'><h2>{t['cert_title']}</h2></div>", unsafe_allow_html=True)

# 9: الكاميرا
st.divider()
st.subheader(t['cam_title'])
st.camera_input("Scanner")
