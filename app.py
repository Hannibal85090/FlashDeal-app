import streamlit as st
from streamlit_option_menu import option_menu
import time

# --- إعدادات النخبة ---
st.set_page_config(page_title="My FlashDeal Star", page_icon="⭐", layout="wide")

# قاموس اللغات الاحترافي
LANG = {
    "العربية": {
        "dir": "rtl", "slogan": "Talk. Pay. Done.", "menu": ["الأمان", "سجل الشفافية", "إبرام الصفقة", "الوكيل الذكي", "Aide / Help"],
        "price_title": "ركن الشفافية: الثمن والمثمن", "confirm": "إتمام الصفقة فوراً", "token_msg": "التوكن المتبادل النشط:",
        "agent_title": "تجربة الوكيل الذكي (جيمين)", "modes": ["⌨️ الكتابة", "🎤 الصوت", "🖐️ الإشارة"], "write_prompt": "اكتب أمرك هنا:",
        "help_title": "❓ (Aide) مركز المساعدة المطور", "help_q1": "كيفية استخدام الأمر الصوتي؟"
    },
    "English": {
        "dir": "ltr", "slogan": "Talk. Pay. Done.", "menu": ["Security", "Transparency Log", "Close Deal", "Smart Agent", "Aide / Help"],
        "price_title": "Transparency Corner: Price & Value", "confirm": "Confirm Deal Now", "token_msg": "Active Mutual Token:",
        "agent_title": "Smart Agent Experience (Gemini)", "modes": ["⌨️ Writing", "🎤 Voice", "🖐️ Sign"], "write_prompt": "Write your command here:",
        "help_title": "❓ (Aide) Advanced Help Center", "help_q1": "How to use voice commands?"
    },
    "Français": {
        "dir": "ltr", "slogan": "Talk. Pay. Done.", "menu": ["Sécurité", "Registre", "Conclure", "Agent Intelligent", "Aide / Help"],
        "price_title": "Transparence: Prix et Valeur", "confirm": "Confirmer l'accord", "token_msg": "Token Mutuel Actif:",
        "agent_title": "Expérience Agent Intelligent", "modes": ["⌨️ Écriture", "🎤 Vocal", "🖐️ Signes"], "write_prompt": "Écrivez votre commande ici:",
        "help_title": "❓ (Aide) Centre d'Aide Avancé", "help_q1": "Comment utiliser les commandes vocales?"
    }
}

# اختيار اللغة
with st.sidebar:
    st.markdown("### 🌐 Language / اللغة")
    selected_lang = st.selectbox("", ["العربية", "English", "Français"])
    L = LANG[selected_lang]

# تطبيق اتجاه الصفحة بناءً على اللغة
st.markdown(f"<div dir='{L['dir']}'>", unsafe_allow_html=True)

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Tajawal', sans-serif; text-align: {'right' if L['dir']=='rtl' else 'left'}; }}
    .price-tag {{ background: #10B981; color: white; padding: 15px; border-radius: 50px; font-size: 30px; font-weight: bold; display: inline-block; }}
    </style>
    """, unsafe_allow_html=True)

# الهيدر
st.markdown(f"<div style='text-align:center;'><h1>⚡ ⭐ My FlashDeal Star</h1><p>{L['slogan']}</p></div>", unsafe_allow_html=True)

# القائمة (تتغير لغتها تلقائياً)
selected = option_menu(
    menu_title=None, options=L["menu"],
    icons=["shield-lock", "clipboard-check", "lightning-fill", "robot", "question-circle-fill"], 
    default_index=2, orientation="horizontal", styles={"nav-link-selected": {"background-color": "#10B981"}}
)

# توكن متغير حقيقي [cite: 2026-02-22]
dynamic_token = f"FD-{int(time.time()) % 99999:05d}-STAR"

if selected in [L["menu"][2]]: # إبرام الصفقة
    st.subheader(L["price_title"])
    col1, col2 = st.columns([1, 1])
    with col1: st.image("https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600")
    with col2:
        st.markdown(f"<div class='price-tag'>$99.99</div>", unsafe_allow_html=True)
        st.write(f"**{L['token_msg']}** `{dynamic_token}`")
        if st.button(L["confirm"], use_container_width=True): st.success(f"Success! {L['slogan']}")

elif selected in [L["menu"][3]]: # الوكيل الذكي
    st.subheader(L["agent_title"])
    mode = st.radio("", L["modes"], horizontal=True)
    if "⌨️" in mode:
        st.text_input(L["write_prompt"]) # خيار الكتابة المطلوب
    elif "🎤" in mode:
        st.info(f"Gemini is listening... (Token: {dynamic_token})")

elif selected in [L["menu"][4]]: # مركز المساعدة
    st.markdown(f"### {L['help_title']}") # محاكاة الصورة
    with st.expander(L["help_q1"]): st.write("...")

st.markdown("</div>", unsafe_allow_html=True)
