import streamlit as st
import time
import random
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- 1. الهوية والذاكرة الموحدة ---
st.set_page_config(page_title="FlashDeal Star - AI Neural Link", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. محرك النطق (صوني التفاعلي) ---
def sony_speak(text, lang='English'):
    v_lang = 'ar-SA' if lang == 'Arabic' else 'en-US'
    components.html(f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = '{v_lang}'; msg.rate = 1.0; msg.pitch = 1.1;
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- 3. قاموس التعريب الشامل (20 نقطة) ---
LANG_DICT = {
    'English': {
        'welcome': "Welcome, honorable judge. Analyzing your request through my neural core...",
        'title': "🌟 My FlashDeal Star 🌟",
        'auth': "🛡️ Identity Authentication",
        'icons': ["👤 Face", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Gem"],
        'saden': "🔒 Saden Security: Mutual Token",
        'sync': "Sync Saden 🛡️",
        'agent': "🤖 Sony AI Agent (Neural Link)",
        'voice': "🎙️ Sony Voice",
        'chat': "⌨️ Smart Chat",
        'placeholder': "Ask the AI...",
        'ctrl': "🏠🚗 Control Hub",
        'car': "Start Engine 🔑",
        'home': "Manage Home 🏠",
        'price': "🎧 Price",
        'deal': "🤝 Agreement Protocol",
        'sig': "Sign here...",
        'buy': "EXECUTE DEAL 🚀",
        'cert': "🏆 Gold Certificate",
        'mem': "📜 Memory Log",
        'acc': "Access Level",
        'cam': "👤 Biometric Scanner"
    },
    'Arabic': {
        'welcome': "أهلاً بك أيها الحكم الفاضل. جاري تحليل سؤالك عبر مركزي العصبي...",
        'title': "🌟 نجم فلاش ديل الخاص بي 🌟",
        'auth': "🛡️ توثيق الهوية",
        'icons': ["👤 الوجه", "🔑 المفتاح", "✋ اليد", "🔒 القفل", "💎 الجوهرة"],
        'saden': "🔒 أمان سادن: التوكن المتبادل",
        'sync': "مزامنة سادن 🛡️",
        'agent': "🤖 الوكيل صوني (الربط العصبي)",
        'voice': "🎙️ صوني صوتياً",
        'chat': "⌨️ دردشة ذكية",
        'placeholder': "اسأل الذكاء الاصطناعي...",
        'ctrl': "🏠🚗 مركز التحكم",
        'car': "تشغيل المحرك 🔑",
        'home': "إدارة المنزل 🏠",
        'price': "🎧 الثمن",
        'deal': "🤝 بروتوكول الاتفاقية",
        'sig': "وقع هنا...",
        'buy': "إبرام الصفقة 🚀",
        'cert': "🏆 الشهادة الذهبية",
        'mem': "📜 سجل الذاكرة",
        'acc': "مستوى الوصول",
        'cam': "👤 الماسح البيومتري"
    }
}

# --- 4. دماغ الذكاء الاصطناعي (أنا أجيب هنا) ---
def get_ai_response(query, lang):
    # محاكاة لربط سؤالي بمركزي العصبي (Gemini)
    q = query.lower()
    if lang == 'Arabic':
        if any(w in q for w in ["أمان", "سادن", "security"]):
            return "سادن ليس مجرد قفل، بل هو بروتوكول حي يربط نيتك البيومترية بالتوكن المتبادل لحظياً."
        return f"بناءً على تحليلي لـ '{query}'، فإن نظام فلاش ديل يضمن لك استقراراً بنسبة مئة بالمئة."
    else:
        if any(w in q for w in ["security", "saden"]):
            return "Saden security protocol represents the future of trust, merging biometric DNA with quantum tokens."
        return f"Regarding '{query}', the Alpha node confirms all systems are optimized for the 2026 pitch."

# --- 5. الواجهة الجانبية (تعريب كامل) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    sel_lang = st.selectbox("🌐 Global Language", ["English", "Arabic"])
    t = LANG_DICT[sel_lang]
    st.divider()
    st.radio(t['acc'], ["* Standard", "Master Alpha 🔓"])
    st.divider()
    with st.expander(t['mem'], expanded=True):
        for item in reversed(st.session_state.history):
            st.markdown(f"<p style='color:#4facfe; font-size:0.75rem;'>{item}</p>", unsafe_allow_html=True)

# --- 6. الواجهة الرئيسية (تحقيق الـ 20 نقطة) ---
# 1، 2، 3. العنوان والنجوم
st.markdown(f"<h1 style='text-align:center; color:gold; font-size:60px;'>🌟 {t['title']} 🌟</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:40px; color:gold; margin-top:-25px;'>★</div>", unsafe_allow_html=True)

# 4، 5. الشعار والتوقيت
c_l, c_t = st.columns([1, 4])
with c_l: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
with c_t: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**")

# 6. أزرار الهوية الخمسة
st.write(f"### {t['auth']}")
cols_a = st.columns(5)
for i, col in enumerate(cols_a):
    if col.button(t['icons'][i]): add_to_memory(f"{t['icons'][i]} Verified")

# 7، 10، 11. أمان سادن والتوكن
st.markdown(f'<div style="padding:15px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);"><h3>{t["saden"]}</h3>', unsafe_allow_html=True)
ct1, ct2 = st.columns(2)
with ct1: st.text_input("Token ID", type="password", key="tk1")
with ct2: st.text_input("Mutual Token", type="password", key="tk2")
if st.button(t['sync']): st.success("Handshake Confirmed ✅")
st.markdown('</div>', unsafe_allow_html=True)

# 16. الوكيل صوني (الربط المباشر بذكائي مع ترحيب)
st.divider()
st.subheader(t['agent'])
t_v, t_c = st.tabs([t['voice'], t['chat']])

with t_v:
    if st.button("🎤 Activate Sony (Neural Link)"):
        sony_speak(t['welcome'], sel_lang) # صوني يرحب بالحكم أولاً
        with st.spinner("Processing through Gemini Core..."):
            time.sleep(1.5)
            ans = get_ai_response("Saden security inquiry", sel_lang)
            st.chat_message("assistant").write(ans)
            sony_speak(ans, sel_lang) # صوني ينطق إجابتي الذكية ثانياً

with t_c:
    q = st.chat_input(t['placeholder'])
    if q:
        add_to_memory(f"Judge: {q}")
        sony_speak(t['welcome'], sel_lang) # ترحيب فوري عند الكتابة
        ans = get_ai_response(q, sel_lang)
        st.chat_message("assistant").write(ans)
        sony_speak(ans, sel_lang) # نطق الإجابة الذكية المترجمة

# 8. التحكم و 9. الكاميرا
st.divider()
st.subheader(t['ctrl'])
ca, cb = st.columns(2)
if ca.button(t['car']): st.success("🚗 Ready"); add_to_memory("Car Started")
if cb.button(t['home']): st.toast("🏠 Safe"); add_to_memory("Home Secure")
st.camera_input(t['cam'])

# 12، 13، 14، 15. الصفقة والثمن والاحتفال
st.divider()
cp, cd = st.columns([1, 2])
with cp:
    st.markdown(f"<div style='border:2px solid gold; padding:10px; border-radius:10px; text-align:center; background:rgba(255,204,0,0.1); color:gold;'><h3>{t['price']}</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with cd:
    st.write(f"### {t['deal']}")
    st.text_input("Signature", placeholder=t['sig'])
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons(); st.snow()
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
        st.markdown(f"<div style='border:2px solid gold; border-radius:15px; padding:20px; text-align:center;'><h2>{t['cert']}</h2><p>Ref: ALPHA-2026</p></div>", unsafe_allow_html=True)
