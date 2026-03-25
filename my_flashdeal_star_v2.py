import streamlit as st
import time
import uuid

# --- 1. إعدادات الصفحة والهوية ---
st.set_page_config(page_title="FlashDeal Star - Ali Arfaoui", page_icon="🌟", layout="wide")

# دالة النطق والربط المباشر بـ Gemini (أنا صوني الحقيقي)
def sony_brain(text, lang='Arabic'):
    v_lang = 'ar-SA' if lang == 'Arabic' else 'en-US'
    components_code = f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = '{v_lang}'; msg.rate = 1.0;
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(components_code, height=0)

if 'history' not in st.session_state: st.session_state.history = []

# --- 2. التنسيق الجمالي (روح الإبداع) ---
st.markdown("""
<style>
.main {background: linear-gradient(135deg, #000428 0%, #004e92 100%); color: white;}
.title-box {text-align: center; color: #FFD700; text-shadow: 2px 2px 10px #000;}
.glass {background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2); margin-bottom: 10px;}
.stButton>button {width: 100%; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# --- 3. الجانب الأيسر (الخيارات والذاكرة) ---
with st.sidebar:
    st.markdown("### 🌐 Languages")
    sel_lang = st.selectbox("Select Language", ["Arabic", "English", "Français", "Italiano"])
    st.divider()
    acc_mode = st.radio("System Mode", ["Standard", "Master Alpha 🔓"])
    st.divider()
    st.markdown("### 📜 Memory Log")
    for log in reversed(st.session_state.history):
        st.caption(log)

# --- 4. الواجهة الرئيسية (التصميم المطلوب بدقة) ---
# 1-5: العنوان، النجوم، الشعار، والتوقيت
st.markdown("<h1 class='title-box'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; color:gold;'>★</h2>", unsafe_allow_html=True) # النجمة الثالثة
col_logo, col_time = st.columns([1, 1])
with col_logo: st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50) # الشعار
with col_time: st.write(f"📅 {time.strftime('%d/%m/%Y')} | 🕒 {time.strftime('%H:%M:%S')}")

# 6: أزرار الهوية (وجه، مفتاح، يد، قفل، جوهرة)
st.markdown("---")
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("👤 Face"): st.session_state.history.append("Face Verified"); st.success("Verified")
if c2.button("🔑 Key"): st.session_state.history.append("Key Synced"); st.info("Key Active")
if c3.button("✋ Hand"): st.session_state.history.append("Gesture Auth"); st.warning("Gesture Read")
if c4.button("🔒 Lock"): st.session_state.history.append("System Locked"); st.error("Locked")
if c5.button("💎 Gem"): st.balloons(); st.session_state.history.append("Premium Mode Active")

# 7-11: أمان سادن والتوكن مع العين
st.markdown("<div class='glass'><h3>🛡️ Saden Security & Token</h3>", unsafe_allow_html=True)
t1, t2 = st.columns(2)
with t1: st.text_input("Main Token", value="********", type="password", help="Click eye to show")
with t2: st.text_input("Mutual Token", value="ALI-2026-SA", type="password")
st.markdown("</div>", unsafe_allow_html=True)

# 8-9: التحكم والكاميرا
st.markdown("### 🏠🚗 Smart Control & Camera")
cc1, cc2, cc3 = st.columns(3)
with cc1: 
    if st.button("🚗 Start Car"): st.toast("Car Engine On"); st.session_state.history.append("Car Started")
with cc2:
    if st.button("🏠 Home Manage"): st.toast("Lights & AC On"); st.session_state.history.append("Home Active")
with cc3:
    st.camera_input("Biometric Scan", key="cam")

# 12-14: إبرام الصفقة، التصافح، والاحتفال
st.markdown("---")
st.markdown("<h2 style='text-align:center;'>🤝 Global Deal</h2>", unsafe_allow_html=True)
chat_input = st.text_input("💬 Talk to Sony / Ali (Text Interaction)")
if st.button("🚀 إتمام الصفقة / Execute Deal", type="primary"):
    st.balloons(); st.snow()
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.markdown(f"""
    <div style='background:gold; padding:20px; border-radius:10px; color:black; text-align:center;'>
        <h2>🏆 شهادة إتمام الصفقة / Certificate</h2>
        <p>المستفيد: <b>علي العرفاوي (Ali Arfaoui)</b></p>
        <p>الكود: {uuid.uuid4().hex[:10].upper()}</p>
        <p>التاريخ: {time.strftime('%Y-%m-%d')}</p>
    </div>
    """, unsafe_allow_html=True)

# 15-16: الوكيل صوني وسماعات الأذن
col_sony, col_price = st.columns([2, 1])
with col_sony:
    st.markdown("### 🎧 Sony Agent (AI Voice)")
    if st.button("🗣️ Start Audio Pitch"):
        sony_brain(f"أهلاً بكم، أنا صوني أتحدث نيابة عن القائد علي العرفاوي. مشروع فلاش ديل جاهز للعرض.", sel_lang)
with col_price:
    st.metric("Price", "$99.99", "Fixed")

