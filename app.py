import streamlit as st
import time
from streamlit_option_menu import option_menu

# --- ١. إعدادات النخبة والهوية ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# --- ٢. إدارة الذاكرة السيادية (يجب أن تكون في الأعلى لتجنب NameError) ---
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_memory(action):
    """تخزين الحدث في الذاكرة لضمان عدم ضياعه بتغير الصوت أو اللغة"""
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

def trigger_emergency_protocol():
    """وحدة الطوارئ SOS - مطابقة للصورة 1000023601"""
    st.error("🚨 SOS: Emergency Protocol Activated!")
    add_to_memory("SOS Triggered - Alerts sent to Master Alpha Hub")
    with st.status("Verifying Security Links..."):
        time.sleep(1)
        st.warning("All Smart Links: IMMOBILIZED 🔒")

# --- ٣. قاموس اللغات الاحترافي (الربط الرباعي) ---
LANG = {
    "العربية": {
        "dir": "rtl", "slogan": "Talk. Pay. Done.", 
        "menu": ["الأمان", "سجل الشفافية", "إبرام الصفقة", "الوكيل الذكي", "مركز المساعدة"],
        "price_title": "ركن الشفافية: الثمن والمثمن", "confirm": "إتمام الصفقة فوراً", 
        "token_msg": "التوكن المتبادل النشط:", "agent_title": "تجربة الوكيل الذكي (Sony-Agent)", 
        "modes": ["⌨️ الكتابة", "🎤 الصوت", "🖐️ الإشارة"], "write_prompt": "اكتب أمرك هنا:",
        "help_title": "❓ مركز المساعدة المطور", "help_q1": "كيفية استخدام الأمر الصوتي؟"
    },
    "English": {
        "dir": "ltr", "slogan": "Talk. Pay. Done.", 
        "menu": ["Security", "Transparency Log", "Close Deal", "Smart Agent", "Help Center"],
        "price_title": "Transparency Corner: Price & Value", "confirm": "Confirm Deal Now", 
        "token_msg": "Active Mutual Token:", "agent_title": "Smart Agent Experience (Sony-Agent)", 
        "modes": ["⌨️ Writing", "🎤 Voice", "🖐️ Sign"], "write_prompt": "Write your command here:",
        "help_title": "❓ Advanced Help Center", "help_q1": "How to use voice commands?"
    },
    "Français": {
        "dir": "ltr", "slogan": "Talk. Pay. Done.", 
        "menu": ["Sécurité", "Registre", "Conclure", "Agent Intelligent", "Aide"],
        "price_title": "Transparence: Prix et Valeur", "confirm": "Confirmer l'accord", 
        "token_msg": "Token Mutuel Actif:", "agent_title": "Expérience Agent Intelligent", 
        "modes": ["⌨️ Écriture", "🎤 Vocal", "🖐️ Signes"], "write_prompt": "Écrivez votre commande ici:",
        "help_title": "❓ Centre d'Aide Avancé", "help_q1": "Comment utiliser les commandes vocales?"
    }
}

# --- ٤. القائمة الجانبية (Sidebar) والمراقبة ---
with st.sidebar:
    st.markdown("### 🌐 Language / اللغة")
    selected_lang = st.selectbox("", list(LANG.keys()))
    L = LANG[selected_lang]
    
    st.divider()
    st.markdown("### 🛡️ Master Controls")
    if st.button("🔔 Activate SOS Mode", type="secondary", use_container_width=True):
        trigger_emergency_protocol()
    
    st.divider()
    with st.expander("📜 Unified Memory Log"):
        for item in reversed(st.session_state.history):
            st.write(item)

# --- ٥. بناء الواجهة الرئيسية بناءً على اللغة ---
st.markdown(f"<div dir='{L['dir']}'>", unsafe_allow_html=True)

# استدعاء خط "تجوال" وتنسيق البطاقات
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Tajawal', sans-serif; text-align: {'right' if L['dir']=='rtl' else 'left'}; }}
    .price-tag {{ background: #10B981; color: white; padding: 15px; border-radius: 50px; font-size: 30px; font-weight: bold; display: inline-block; }}
    </style>
    """, unsafe_allow_html=True)

# الهيدر
st.markdown(f"<div style='text-align:center;'><h1>⚡ ⭐ My FlashDeal Star</h1><p>{L['slogan']}</p></div>", unsafe_allow_html=True)

# القائمة التفاعلية
selected = option_menu(
    menu_title=None, options=L["menu"],
    icons=["shield-lock", "clipboard-check", "lightning-fill", "robot", "question-circle-fill"], 
    default_index=2, orientation="horizontal", 
    styles={"nav-link-selected": {"background-color": "#10B981"}}
)

# توكن متغير حقيقي لضمان الأمان
dynamic_token = f"FD-{int(time.time()) % 99999:05d}-STAR"

if selected == L["menu"][2]: # إبرام الصفقة
    st.subheader(L["price_title"])
    col1, col2 = st.columns([1, 1])
    with col1: st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600")
    with col2:
        st.markdown(f"<div class='price-tag'>$99.99</div>", unsafe_allow_html=True)
        st.write(f"**{L['token_msg']}** `{dynamic_token}`")
        if st.button(L["confirm"], use_container_width=True): 
            st.success(f"Success! {L['slogan']}")
            add_to_memory(f"Deal Closed in {selected_lang}")

elif selected == L["menu"][3]: # الوكيل الذكي
    st.subheader(L["agent_title"])
    mode = st.radio("", L["modes"], horizontal=True)
    if "⌨️" in mode:
        cmd = st.text_input(L["write_prompt"])
        if cmd: add_to_memory(f"Command: {cmd}")
    elif "🎤" in mode:
        st.info(f"Sony-Agent is listening... (Token: {dynamic_token})")

elif selected == L["menu"][4]: # مركز المساعدة
    st.markdown(f"### {L['help_title']}")
    with st.expander(L["help_q1"]): 
        st.write("يمكنك البدء بالضغط على أيقونة الميكروفون ونطق كلمة 'Star'.")

st.markdown("</div>", unsafe_allow_html=True)
