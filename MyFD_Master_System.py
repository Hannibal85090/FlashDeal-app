import streamlit as st
import time

# --- ١. إعدادات الهوية والجمال (Sony Elite Style) ---
st.set_page_config(page_title="FlashDeal Star Universal", page_icon="🌟", layout="wide")

# --- ٢. وحدة الذاكرة والسيادة (المحرك الخفي) ---
# التأكد من بقاء الذاكرة نشطة حتى عند تغيير اللغة
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    """تخزين الحدث في الذاكرة لضمان الاستمرارية"""
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

def trigger_emergency_protocol():
    """بروتوكول الطوارئ SOS - الربط السيادي"""
    st.error("🚨 SOS: Emergency Protocol Activated!")
    add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")
    with st.status("Verifying Security Links..."):
        time.sleep(1)
        st.warning("All Smart Links: IMMOBILIZED 🔒")

# --- ٣. تنسيق الجمال (CSS المطور) ---
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
    /* تنسيق سجل الذاكرة الجانبي */
    .log-text { font-size: 0.85rem; color: #4facfe; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

# --- ٤. محرك اللغات الرباعي ---
LANG_DICT = {
    'Arabic': {
        'title': "نجم فلاش ديل العالمي 🌟", 'motto': "تحدث. ادفع. تم.",
        'saden': "أمان سادن: التوكن المتبادل", 'home_car': "التحكم الذكي 🏠🚗",
        'buy': "إبرام الصفقة العالمية 🚀", 'success': "تمت العملية بنجاح! مبروك شريكي",
        'sync': "مزامنة التوكن 🛡️", 'car': "تشغيل السيارة 🔑", 'home': "إدارة المنزل 🏠",
        'sos': "تفعيل وضع الطوارئ 🔔", 'mem': "📜 سجل الذاكرة الموحد"
    },
    'English': {
        'title': "FlashDeal Star Universal 🌟", 'motto': "Talk. Pay. Done.",
        'saden': "Saden Security: Mutual Token", 'home_car': "Smart Control 🏠🚗",
        'buy': "Global Deal Execution 🚀", 'success': "Process Completed Successfully!",
        'sync': "Sync Token 🛡️", 'car': "Start Car 🔑", 'home': "Manage Home 🏠",
        'sos': "Activate SOS Mode 🔔", 'mem': "📜 Unified Memory Log"
    },
    'Italiano': {
        'title': "FlashDeal Star Universale 🌟", 'motto': "Parla. Paga. Fatto.",
        'saden': "Sicurezza Saden: Token Reciproco", 'home_car': "Controllo Casa e Auto 🏠🚗",
        'buy': "Concludi l'Affare 🚀", 'success': "Operazione riuscita!",
        'sync': "Sincronizza 🛡️", 'car': "Avvia Auto 🔑", 'home': "Gestisci Casa 🏠",
        'sos': "Attiva SOS 🔔", 'mem': "📜 Registro di Memoria"
    },
    'Français': {
        'title': "FlashDeal Star Universel 🌟", 'motto': "Parlez. Payez. Fait.",
        'saden': "Sécurité Saden: Token Mutuel", 'home_car': "Contrôle Maison & Voiture 🏠🚗",
        'buy': "Conclure l'Accord 🚀", 'success': "Opération terminée!",
        'sync': "Synchroniser 🛡️", 'car': "Démarrer 🔑", 'home': "Gérer Maison 🏠",
        'sos': "Activer SOS 🔔", 'mem': "📜 Journal de Mémoire"
    }
}

# --- ٥. القائمة الجانبية (هنا تظهر الإضافات التي طلبتها) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60)
    selected_lang = st.selectbox("🌐 Global Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang]
    
    st.divider()
    # إضافة زر الطوارئ في الجانب
    if st.button(t['sos'], type="secondary"):
        trigger_emergency_protocol()
    
    st.divider()
    # إضافة سجل الذاكرة الموحد (الذي كان مفقوداً في النسخة السابقة)
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history:
            st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)
    
    st.divider()
    acc = st.radio("Access Level", ["Standard", "Master Alpha 🔓"])

# --- ٦. الواجهة الرئيسية ---
st.markdown(f"<h1 style='text-align: center; color: #4facfe;'>{t['title']}</h1>", unsafe_allow_html=True)

# أ. التوكن والوكيل
st.markdown(f'<div class="glass-card"><h3>🔒 {t["saden"]}</h3>', unsafe_allow_html=True)
c1, c2 = st.columns([3, 1])
with c1: st.text_input("Token ID", type="password", label_visibility="collapsed", key="token_main")
with c2: 
    if st.button(t['sync']): 
        st.success("Linked! ✅")
        add_to_memory(f"Token Synced: {selected_lang}")
st.markdown('</div>', unsafe_allow_html=True)

# ب. الوكيل الذكي (تبويبات)
tab1, tab2, tab3 = st.tabs(["🎙️ Voice", "👋 Sign", "⌨️ Text"])
with tab1: 
    if st.button(f"{t['motto']} (Mic Active)"):
        add_to_memory("Voice command engaged")
with tab3: 
    chat_val = st.chat_input("Sony-Agent...")
    if chat_val: add_to_memory(f"Chat: {chat_val}")

# ج. التحكم الذكي
st.markdown(f"### {t['home_car']}")
ca, cb = st.columns(2)
with ca: 
    if st.button(t['car']): 
        with st.status("Linking..."): time.sleep(1); st.success("🚗 Engine On!")
        add_to_memory("Car Started")
with cb:
    if st.button(t['home']): 
        st.toast("🏠 Welcome Home Mode Active")
        add_to_memory("Home Managed")

# --- ٧. إبرام الصفقة (الاحتفالية) ---
st.divider()
if st.button(t['buy'], type="primary", use_container_width=True):
    st.balloons(); st.snow()
    add_to_memory("Deal Concluded Successfully")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3")
    st.markdown(f"<div class='glass-card' style='text-align: center;'><h2>🏆 {t['success']}</h2><p>Cert: STAR-UNIV-2026-{int(time.time())}</p></div>", unsafe_allow_html=True)

