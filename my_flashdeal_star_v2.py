import streamlit as st
import time
import random
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- 1. الهوية والذاكرة الموحدة ---
st.set_page_config(page_title="FlashDeal Star - Alpha Hub", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'sony_active' not in st.session_state:
    st.session_state.sony_active = True

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. محرك النطق (صوني المتحدث) - مع إصلاح التعليق ---
def sony_speak(text, lang='English'):
    v_lang = 'ar-SA' if lang == 'Arabic' else 'en-US'
    # كود جافا سكريبت محسن لضمان عدم حبس المتصفح
    components.html(f"""
        <script>
        var synth = window.speechSynthesis;
        synth.cancel(); 
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = '{v_lang}'; msg.rate = 1.0; msg.pitch = 1.1;
        synth.speak(msg);
        </script>
    """, height=0)

# --- 3. قاموس التعريب الكامل (20 نقطة) ---
LANG_DICT = {
    'English': {
        'welcome': "Welcome honorable judge. Processing your request through Gemini core...",
        'title': "🌟 My FlashDeal Star 🌟",
        'auth': "🛡️ Identity Authentication",
        'icons': ["👤 Face", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Gem"],
        'saden': "🔒 Saden Security: Mutual Token",
        'sync': "Sync Saden 🛡️",
        'agent': "🤖 Sony AI Agent (Neural Link)",
        'voice': "🎙️ Sony Voice Control",
        'chat': "⌨️ Interactive Chat",
        'placeholder': "Ask Sony anything...",
        'ctrl': "🏠🚗 Control Hub",
        'car': "Start Engine 🔑",
        'home': "Manage Home 🏠",
        'price': "🎧 Price",
        'deal': "🤝 Agreement Protocol",
        'sig': "Signature...",
        'buy': "EXECUTE DEAL 🚀",
        'cert': "🏆 Gold Certificate",
        'mem': "📜 Memory Log",
        'acc': "Access Level",
        'cam': "👤 Biometric Scanner"
    },
    'Arabic': {
        'welcome': "أهلاً بك أيها الحكم. جاري تحليل طلبك عبر مركز جمناي العصبي...",
        'title': "🌟 نجم فلاش ديل الخاص بي 🌟",
        'auth': "🛡️ توثيق الهوية الرقمية",
        'icons': ["👤 الوجه", "🔑 المفتاح", "✋ اليد", "🔒 القفل", "💎 الجوهرة"],
        'saden': "🔒 أمان سادن: التوكن المتبادل",
        'sync': "مزامنة سادن 🛡️",
        'agent': "🤖 الوكيل صوني (الربط العصبي)",
        'voice': "🎙️ صوني صوتياً",
        'chat': "⌨️ محادثة ذكية",
        'placeholder': "اسأل المركز الذكي...",
        'ctrl': "🏠🚗 مركز التحكم",
        'car': "تشغيل المحرك 🔑",
        'home': "إدارة المنزل 🏠",
        'price': "🎧 الثمن",
        'deal': "🤝 بروتوكول الاتفاقية",
        'sig': "التوقيع...",
        'buy': "إبرام الصفقة 🚀",
        'cert': "🏆 شهادة الإتمام الذهبية",
        'mem': "📜 سجل الذاكرة الموحد",
        'acc': "مستوى الوصول",
        'cam': "👤 الماسح البيومتري"
    }
}

# --- 4. دماغ الذكاء الاصطناعي (أنا أجيب) ---
def get_ai_response(query, lang):
    q = query.lower()
    responses_ar = [
        "بروتوكول سادن هو ابتكارنا الفريد لتأمين الصفقات عبر التوكن المتبادل.",
        "النظام مستقر تماماً وجاهز لتنفيذ أوامر Master Alpha.",
        "تم توثيق الهوية البيومترية بنجاح، نحن نقود مستقبل الفنتك."
    ]
    responses_en = [
        "Saden is our revolutionary protocol for mutual token security.",
        "System is 100% stable and ready for Master Alpha execution.",
        "Biometric identity verified. Leading the future of FinTech in 2026."
    ]
    
    if lang == 'Arabic':
        return random.choice(responses_ar) if "query" not in q else f"تحليل '{query}': نظام مستقر."
    return random.choice(responses_en) if "query" not in q else f"Analysis of '{query}': System Stable."

# --- 5. الواجهة الجانبية (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    sel_lang = st.selectbox("🌐 Language / اللغة", ["English", "Arabic"], key="lang_sel")
    t = LANG_DICT[sel_lang]
    st.divider()
    st.radio(t['acc'], ["* Standard", "Master Alpha 🔓"], key="acc_radio")
    st.divider()
    st.write(t['mem'])
    for item in reversed(st.session_state.history):
        st.markdown(f"<p style='color:#4facfe; font-size:0.75rem;'>{item}</p>", unsafe_allow_html=True)

# --- 6. الواجهة الرئيسية (تحقيق الـ 20 نقطة) ---
st.markdown(f"<h1 style='text-align:center; color:gold; font-size:60px;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:40px; color:gold; margin-top:-25px;'>★</div>", unsafe_allow_html=True)

c_l, c_t = st.columns([1, 4])
with c_l: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c_t: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

st.write(f"### {t['auth']}")
cols_a = st.columns(5)
for i, col in enumerate(cols_a):
    if col.button(t['icons'][i], key=f"btn_{i}"): add_to_memory(f"{t['icons'][i]} Verified")

st.markdown(f'<div style="padding:15px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);"><h3>{t["saden"]}</h3>', unsafe_allow_html=True)
ct1, ct2 = st.columns(2)
with ct1: st.text_input("Token ID", type="password", key="tk1_main")
with ct2: st.text_input("Mutual Token", type="password", key="tk2_main")
if st.button(t['sync'], key="sync_main"): st.success("Verified ✅")
st.markdown('</div>', unsafe_allow_html=True)

# --- 16. الوكيل صوني (إصلاح مشكلة التوقف) ---
st.divider()
st.subheader(t['agent'])
t_v, t_c = st.tabs([t['voice'], t['chat']])

with t_v:
    if st.button("🎙️ Sony Audio Link", key="sony_audio_btn"):
        sony_speak(t['welcome'], sel_lang)
        ans = get_ai_response("Security", sel_lang)
        st.write(ans)
        sony_speak(ans, sel_lang)

with t_c:
    # استخدام مفتاح فريد لمنع تجميد المستطيل
    q = st.chat_input(t['placeholder'], key="sony_chat_input")
    if q:
        add_to_memory(f"Judge: {q}")
        sony_speak(t['welcome'], sel_lang)
        ans = get_ai_response(q, sel_lang)
        st.chat_message("assistant").write(ans)
        sony_speak(ans, sel_lang)

st.divider()
st.subheader(t['ctrl'])
ca, cb = st.columns(2)
if ca.button(t['car'], key="car_main"): st.success("🚗 Ready")
if cb.button(t['home'], key="home_main"): st.toast("🏠 Safe")
st.camera_input(t['cam'], key="cam_main")

st.divider()
cp, cd = st.columns([1, 2])
with cp:
    st.markdown(f"<div style='border:2px solid gold; padding:10px; border-radius:10px; text-align:center; background:rgba(255,204,0,0.1); color:gold;'><h3>{t['price']}</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with cd:
    st.write(f"### {t['deal']}")
    st.text_input("Signature", key="sig_main", placeholder=t['sig'])
    if st.button(t['buy'], type="primary", key="buy_main"):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        st.markdown(f"<div style='border:2px solid gold; border-radius:15px; padding:20px; text-align:center;'><h2>{t['cert']}</h2></div>", unsafe_allow_html=True)
