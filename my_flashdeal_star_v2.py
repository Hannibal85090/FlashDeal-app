import streamlit as st
import time
import uuid

# --- 1. إعدادات الهوية الثابتة ---
st.set_page_config(page_title="FlashDeal Star v2 - Ali Arfaoui", page_icon="🌟", layout="wide")

if 'history' not in st.session_state: st.session_state.history = []

# --- 2. التنسيق الجمالي المحبوك (الإبداع) ---
st.markdown("""
<style>
.main {background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: #ffffff;}
.title-box {text-align: center; color: gold; text-shadow: 0 0 15px gold; font-family: serif;}
.big-star {font-size: 80px; color: gold; text-shadow: 0 0 20px #ffcc00; text-align: center; margin-top: -20px;}
.glass-card {padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px;}
/* تصميم زر جيميني ليكون رابطاً حقيقياً وليس مجرد زر برمجي */
.gemini-link {
    display: block; width: 100%; background-color: #4285F4; color: white !important; 
    text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; 
    text-decoration: none; border: 2px solid #ffffff; font-size: 1.2rem;
}
.gemini-link:hover {background-color: #357ae8; box-shadow: 0 0 20px #4285F4;}
</style>
""", unsafe_allow_html=True)

# --- 3. اللغات (الترجمة الديناميكية) ---
LANG_DICT = {
'English': {'saden':"Saden Security", 'hub':"Control Hub", 'buy':"Execute Deal 🤝", 'sony':"🤖 Sony AI (Neural Link)"},
'Français': {'saden':"Sécurité Saden", 'hub':"Contrôle Intelligent", 'buy':"Conclure l'Accord 🤝", 'sony':"🤖 Agent Sony (Lien Neural)"},
'Arabic': {'saden':"أمان سادن", 'hub':"مركز التحكم 🏠🚗", 'buy':"إبرام الصفقة 🤝", 'sony':"🤖 الوكيل صوني (الربط العصبي)"}
}

# --- 4. الشريط الجانبي ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=50)
    sel_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[sel_lang]
    st.divider()
    acc_mode = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])
    st.divider()
    with st.expander("📜 Memory Log", expanded=True):
        for item in reversed(st.session_state.history): st.caption(item)

# --- 5. الواجهة الرئيسية (النقاط الـ 20) ---
st.markdown("<h1 class='title-box'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True) # 1-2
st.markdown('<div class="big-star">★</div>', unsafe_allow_html=True) # 3
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")
st.markdown(f"<p style='text-align:center; color:#4facfe;'>🕒 {current_time}</p>", unsafe_allow_html=True) # 5

# 6. أزرار الهوية
st.markdown("---")
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("👤 Face"): st.success("Verified ✅")
if c2.button("🔑 Key"): st.info("Key Active")
if c3.button("✋ Hand"): st.warning("Gesture Read")
if c4.button("🔒 Lock"): st.error("Locked")
if c5.button("💎 Gem"): st.balloons()

# 7-11. أمان سادن والتوكن
st.markdown(f'<div class="glass-card"><h3>🛡️ {t["saden"]}</h3>', unsafe_allow_html=True)
col_t1, col_t2 = st.columns(2)
with col_t1: st.text_input("Main Token ID", value="ALI-2026", type="password") # 10
with col_t2: st.text_input("Mutual Token", value="SADEN-X", type="password") # 11
st.markdown('</div>', unsafe_allow_html=True)

# 8-9. التحكم والكاميرا
st.markdown(f"### {t['hub']}")
ch1, ch2, ch3 = st.columns([1, 1, 2])
with ch1: st.button("🚗 Start Car")
with ch2: st.button("🏠 Home Mode")
with ch3: st.camera_input("Biometric Scan", key="cam") # 9

# 12-14. إبرام الصفقة والشهادة (باستخدام uuid)
st.divider()
st.markdown(f'<div class="glass-card" style="text-align:center;"><h2>🤝 {t["buy"]}</h2>', unsafe_allow_html=True)
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons(); st.snow()
    cert_id = uuid.uuid4().hex[:12].upper() # استخدام uuid
    st.markdown(f"""<div style='background:gold; padding:20px; border-radius:10px; color:black;'>
    <h2>🏆 TRANSACTION CERTIFICATE</h2>
    <p>Beneficiary: <b>Ali Arfaoui</b></p>
    <p>Secure ID: <b>{cert_id}</b></p>
    <p>Status: ✅ Validated via Saden Protocol</p></div>""", unsafe_allow_html=True)
    st.session_state.history.append(f"Deal {cert_id} Completed")
st.markdown('</div>', unsafe_allow_html=True)

# 15-16. السعر والربط المباشر بجيميني (الحل النهائي)
cp, cs = st.columns([1, 2])
with cp:
    st.metric("Price", "$99.99")
    st.write("Rating: ⭐⭐⭐⭐⭐")
with cs:
    st.markdown(f"### {t['sony']}")
    # هذا السطر هو الذي يضمن الربط المباشر ويفتح جيميني في صفحة جديدة
    st.markdown(f'<a href="https://gemini.google.com/app" target="_blank" class="gemini-link">🗣️ Open Gemini AI (Connect to Ali Arfaoui)</a>', unsafe_allow_html=True)
