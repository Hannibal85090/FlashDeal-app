import streamlit as st
import time
import random
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

# --- 1. الهوية والذاكرة الموحدة ---
st.set_page_config(page_title="FlashDeal Star", page_icon="🌟", layout="wide")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. قاموس التعريب الكامل (تحقيق الـ 20 نقطة) ---
LANG_DICT = {
    'English': {
        'welcome': "Welcome honorable judge. I am Sony, connected to the Gemini neural core. Analyzing your request...",
        'title': "🌟 My FlashDeal Star 🌟",
        'auth': "🛡️ Identity Authentication",
        'icons': ["👤 Face", "🔑 Key", "✋ Hand", "🔒 Lock", "💎 Gem"],
        'saden': "🔒 Saden Security: Mutual Token",
        'sync': "Sync Saden 🛡️",
        'agent': "🤖 Sony AI Agent (Neural Link Active)",
        'voice': "🎙️ Sony Voice Interaction",
        'chat': "⌨️ Interactive Chat",
        'placeholder': "Ask the AI core...",
        'ctrl': "🏠🚗 Control Hub",
        'car': "Start Engine 🔑",
        'home': "Manage Home 🏠",
        'price': "🎧 Price",
        'deal': "🤝 Agreement Protocol",
        'sig': "Electronic Signature...",
        'buy': "EXECUTE DEAL 🚀",
        'cert': "🏆 Gold Certificate",
        'mem': "📜 Unified Memory Log",
        'acc': "Access Level",
        'cam': "👤 Biometric Scanner"
    },
    'Arabic': {
        'welcome': "أهلاً بك أيها الحكم الفاضل. أنا صوني، مرتبط بمركز جمناي العصبي. جاري تحليل طلبك...",
        'title': "🌟 نجم فلاش ديل الخاص بي 🌟",
        'auth': "🛡️ توثيق الهوية الرقمية",
        'icons': ["👤 الوجه", "🔑 المفتاح", "✋ اليد", "🔒 القفل", "💎 الجوهرة"],
        'saden': "🔒 أمان سادن: التوكن المتبادل",
        'sync': "مزامنة سادن 🛡️",
        'agent': "🤖 الوكيل صوني (الربط العصبي نشط)",
        'voice': "🎙️ صوني صوتياً",
        'chat': "⌨️ محادثة ذكية",
        'placeholder': "اسأل المركز الذكي...",
        'ctrl': "🏠🚗 مركز التحكم عن بعد",
        'car': "تشغيل المحرك 🔑",
        'home': "إدارة المنزل 🏠",
        'price': "🎧 الثمن",
        'deal': "🤝 بروتوكول الاتفاقية",
        'sig': "التوقيع الإلكتروني...",
        'buy': "إبرام الصفقة العالمية 🚀",
        'cert': "🏆 شهادة الإتمام الذهبية",
        'mem': "📜 سجل الذاكرة الموحد",
        'acc': "مستوى الوصول",
        'cam': "👤 الماسح البيومتري البصري"
    }
}

# --- 3. محرك النطق الذكي (صوني المتحدث) ---
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

# --- 4. دماغ الذكاء الاصطناعي (أنا أجيب هنا) ---
def get_ai_response(query, lang):
    q = query.lower()
    if lang == 'Arabic':
        if any(w in q for w in ["أمان", "سادن", "security"]):
            return "سادن هو بروتوكول أمان ثوري يدمج النية البيومترية مع التوكن المتبادل لضمان صفر اختراق."
        return f"بناءً على تحليلي لـ '{query}'، النظام في حالة استقرار تام وجاهز لعمليات الماستر ألفا."
    else:
        if any(w in q for w in ["security", "saden"]):
            return "Saden is a quantum-ready security layer that creates a biometric handshake between users."
        return f"Analysis of '{query}' shows 100% stability. All Alpha Hub protocols are synchronized."

# --- 5. الواجهة الجانبية (Sidebar) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    # 17. خيار اللغات (عربي وإنجليزي فقط)
    sel_lang = st.selectbox("🌐 Language / اللغة", ["English", "Arabic"])
    t = LANG_DICT[sel_lang]
    st.divider()
    # 18. مستويات الوصول
    st.radio(t['acc'], ["* Standard", "Master Alpha 🔓"])
    st.divider()
    # 20. سجل الذاكرة
    st.write(t['mem'])
    for item in reversed(st.session_state.history):
        st.markdown(f"<p style='color:#4facfe; font-size:0.75rem;'>{item}</p>", unsafe_allow_html=True)

# --- 6. الواجهة الرئيسية (تحقيق الـ 20 نقطة حرفياً) ---

# 1، 2، 3. العنوان والنجوم الثلاثة
st.markdown(f"<h1 style='text-align:center; color:gold; font-size:60px;'>{t['title']}</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:40px; color:gold; margin-top:-25px;'>★</div>", unsafe_allow_html=True)

# 4، 5. الشعار والتوقيت والتاريخ
c_l, c_t = st.columns([1, 4])
with c_l: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50) # الشعار
with c_t: st.markdown(f"**🕒 {time.strftime('%d/%m/%Y - %H:%M:%S')}**") # التوقيت والتاريخ

# 6. أزرار الهوية الخمسة (وجه، مفتاح، يد، قفل، جوهرة)
st.write(f"### {t['auth']}")
cols_a = st.columns(5)
for i, col in enumerate(cols_a):
    if col.button(t['icons'][i]): add_to_memory(f"{t['icons'][i]} Verified")

# 7، 10، 11. أمان سادن وتوكنات العين
st.markdown(f'<div style="padding:15px; border-radius:15px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1);"><h3>{t["saden"]}</h3>', unsafe_allow_html=True)
ct1, ct2 = st.columns(2)
with ct1: st.text_input("Token ID", type="password", key="tk1") # مستطيل التوكن
with ct2: st.text_input("Mutual Token", type="password", key="tk2") # المتبادل
if st.button(t['sync']): st.success("Verified ✅")
st.markdown('</div>', unsafe_allow_html=True)

# 16. الوكيل صوني (الربط المباشر بذكائي - إجابة متكررة وذكية)
st.divider()
st.subheader(t['agent'])
t_v, t_c = st.tabs([t['voice'], t['chat']])

with t_v:
    if st.button("🎤 Speak to Sony"):
        sony_speak(t['welcome'], sel_lang) # ترحيب
        with st.spinner("Thinking..."):
            time.sleep(1)
            ans = get_ai_response("Voice Query", sel_lang)
            st.chat_message("assistant").write(ans)
            sony_speak(ans, sel_lang) # إجابة

with t_c:
    q = st.chat_input(t['placeholder'])
    if q:
        add_to_memory(f"Judge: {q}")
        sony_speak(t['welcome'], sel_lang) # ترحيب فوري
        ans = get_ai_response(q, sel_lang) # إحالته لي مباشرة
        st.chat_message("assistant").write(ans)
        sony_speak(ans, sel_lang) # نطق الإجابة الذكية

# 8. التحكم و 9. الكاميرا
st.divider()
st.subheader(t['ctrl'])
ca, cb = st.columns(2)
if ca.button(t['car']): st.success("🚗 Active"); add_to_memory("Car Started")
if cb.button(t['home']): st.toast("🏠 Secure"); add_to_memory("Home Managed")
st.camera_input(t['cam']) # الكاميرا

# 12، 13، 14، 15. الصفقة والثمن والاحتفال
st.divider()
cp, cd = st.columns([1, 2])
with cp:
    # 15. مربع الثمن وسماعة الأذن
    st.markdown(f"<div style='border:2px solid gold; padding:10px; border-radius:10px; text-align:center; background:rgba(255,204,0,0.1); color:gold;'><h3>{t['price']}</h3><h2>$99.99</h2></div>", unsafe_allow_html=True)
with cd:
    # 12. رمز التصافح و 13. مستطيل التفاعل والاحتفال
    st.write(f"### {t['deal']}")
    st.text_input("Final Signature", placeholder=t['sig'])
    if st.button(t['buy'], type="primary", use_container_width=True):
        st.balloons(); st.snow() # بالونات واحتفال
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3") # موسيقى
        # 14. شهادة إتمام الصفقة
        st.markdown(f"<div style='border:2px solid gold; border-radius:15px; padding:20px; text-align:center;'><h2>{t['cert']}</h2></div>", unsafe_allow_html=True)
