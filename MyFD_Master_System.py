import streamlit as st
import time

# --- ١. إعدادات الهوية والجمال (Sony Elite Style) ---
st.set_page_config(page_title="FlashDeal Star Universal", page_icon="🌟", layout="wide")

st.markdown("""
    <style>
    .main { background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 15px; background: linear-gradient(45deg, #004e92, #000428);
        border: 1px solid #4facfe; color: white; font-weight: bold; height: 3.8em; transition: 0.4s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,78,146,0.4); }
    .glass-card { 
        padding: 25px; border-radius: 20px; background: rgba(255, 255, 255, 0.05); 
        border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ٢. محرك اللغات الرباعي الكامل ---
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟", 'motto': "تحدث. ادفع. تم.",
        'agent': "الوكيل الذكي (Multimodal)", 'saden': "أمان سادن: التوكن المتبادل",
        'home_car': "التحكم الذكي (المنزل والسيارة) 🏠🚗", 'product': "سماعات الرأس (إصدار النجم)",
        'buy': "إبرام الصفقة العالمية 🚀", 'success': "تمت العملية بنجاح! مبروك شريكي",
        'sync': "مزامنة التوكن 🛡️", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠"
    },
    'English': {
        'title': "FlashDeal Star Universal 🌟", 'motto': "Talk. Pay. Done.",
        'agent': "Smart Agent (Multimodal)", 'saden': "Saden Security: Mutual Token",
        'home_car': "Smart Control (Home & Car) 🏠🚗", 'product': "Headphones (Star Edition)",
        'buy': "Global Deal Execution 🚀", 'success': "Process Completed Successfully!",
        'sync': "Sync Token 🛡️", 'car': "Start Car 🔑", 'home': "Manage Home 🏠"
    },
    'Italiano': {
        'title': "FlashDeal Star Universale 🌟", 'motto': "Parla. Paga. Fatto.",
        'agent': "Agente Intelligente", 'saden': "Sicurezza Saden: Token Reciproco",
        'home_car': "Controllo Intelligente (Casa e Auto) 🏠🚗", 'product': "Cuffie (Edizione Star)",
        'buy': "Concludi l'Affare 🚀", 'success': "Operazione riuscita!",
        'sync': "Sincronizza 🛡️", 'car': "Avvia Auto 🔑", 'home': "Gestisci Casa 🏠"
    },
    'Français': {
        'title': "FlashDeal Star Universel 🌟", 'motto': "Parlez. Payez. Fait.",
        'agent': "Agent Intelligent", 'saden': "Sécurité Saden: Token Mutuel",
        'home_car': "Contrôle Intelligent (Maison & Voiture) 🏠🚗", 'product': "Casque (Édition Star)",
        'buy': "Conclure l'Accord 🚀", 'success': "Opération terminée!",
        'sync': "Synchroniser 🛡️", 'car': "Démarrer 🔑", 'home': "Gérer Maison 🏠"
    }
}

# --- ٣. القائمة الجانبية وإدارة الحالة ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=70)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    st.markdown(f"**Slogan:** `{t['motto']}`")
    st.divider()
    acc = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])

# --- ٤. الواجهة الرئيسية (التفاعل الشامل) ---
st.markdown(f"<h1 style='text-align: center; color: #4facfe;'>{t['title']}</h1>", unsafe_allow_html=True)

# أ. التوكن المتبادل والوكيل
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
c1, c2 = st.columns([3, 1])
with c1: st.text_input("Token ID", type="password", label_visibility="collapsed")
with c2: 
    if st.button(t['sync']): st.success("Linked! ✅")
st.markdown('</div>', unsafe_allow_html=True)

# ب. الوكيل الذكي (تبويبات)
tab1, tab2, tab3 = st.tabs(["🎙️ Voice", "👋 Sign", "⌨️ Text"])
with tab1: st.button(f"{t['motto']} (Mic Active)")
with tab3: st.chat_input("Sony-Agent...")

# ج. التحكم الذكي (Hub)
st.markdown(f"### {t['home_car']}")
ca, cb = st.columns(2)
with ca: 
    if st.button(t['car']): 
        with st.status("Linking..."): time.sleep(1); st.success("🚗 Engine On!")
with cb:
    if st.button(t['home']): st.toast("🏠 Welcome Home Mode Active")

# --- ٥. إبرام الصفقة (الاحتفالية الكبرى) ---
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons(); st.snow()
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
    st.markdown(f"<div class='glass-card' style='text-align: center;'><h2>🏆 {t['success']}</h2><p>Cert: STAR-UNIV-2026-{int(time.time())}</p></div>", unsafe_allow_html=True)
