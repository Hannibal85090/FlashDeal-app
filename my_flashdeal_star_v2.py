import streamlit as st
import time
import uuid

# --- 1. إعدادات الصفحة والهوية الرقمية لـ علي العرفاوي ---
st.set_page_config(page_title="My FlashDeal Star - Ali Arfaoui", page_icon="🌟", layout="wide")

# دالة النطق للوكيل صوني (تعمل محلياً بالمتصفح)
def sony_speak(text, lang_code):
    components_code = f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = '{lang_code}'; msg.rate = 1.0; msg.pitch = 1.1;
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.components.v1.html(components_code, height=0)

if 'history' not in st.session_state: st.session_state.history = []

# دالة إضافة العمليات للذاكرة
def add_to_memory(action):
    timestamp = time.strftime("%H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] - {action}")

# --- 2. التنسيق الجمالي (روح الإبداع والاحترافية) ---
st.markdown("""
<style>
/* خلفية متدرجة فخمة */
.main {background: linear-gradient(135deg, #00050a 0%, #011627 100%); color: #ffffff;}
/* تنسيق النجوم الذهبية والعنوان */
.title-box {text-align: center; color: gold; text-shadow: 0 0 15px gold; font-family: 'Times New Roman', serif; margin-bottom: 0;}
.big-star {font-size: 100px; color: gold; text-shadow: 0 0 20px #ffcc00; text-align: center; margin-top: -30px; margin-bottom: 20px;}
/* تنسيق الكروت الزجاجية */
.glass-card {padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); backdrop-filter: blur(10px); margin-bottom: 15px;}
.log-text {font-size: 0.8rem; color: #4facfe; font-family: 'Courier New', monospace;}
/* تنسيق الأزرار */
.stButton>button {width: 100%; border-radius: 8px; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# --- 3. قاموس اللغات (الترجمة الديناميكية الكاملة) ---
LANG_DICT = {
'English': {'motto':"Talk. Pay. Done.", 'saden':"Saden Security: Mutual Token", 'hub':"Smart Control Hub 🏠🚗", 'buy':"Execute Deal 🤝", 'success':"Deal Success!", 'sync':"Sync Token 🛡️", 'car':"Start Car 🔑", 'home':"Manage Home 🏠", 'sos':"Activate SOS Mode 🚨", 'mem':"📜 Memory Log", 'standard':"Standard Mode", 'master':"Master Alpha 🔓", 'price':"Price", 'stability':"Stability", 'rating':"Rating", 'camera':"👤 Biometric Face Cam", 'sony_t':"🤖 Sony Agent - Welcome", 'sony_s':"Welcome. I am Sony, presenting for Ali Arfaoui. FlashDeal is ready.", 'lang_c': 'en-US'},
'Français': {'motto':"Parlez. Payez. Fait.", 'saden':"Sécurité Saden: Token Mutuel", 'hub':"Contrôle Intelligent 🏠🚗", 'buy':"Conclure l'Accord 🤝", 'success':"Accord Réussi!", 'sync':"Synchroniser 🛡️", 'car':"Démarrer 🔑", 'home':"Gérer Maison 🏠", 'sos':"Activer SOS 🚨", 'mem':"📜 Journal de Mémoire", 'standard':"Mode Standard", 'master':"Maître Alpha 🔓", 'price':"Prix", 'stability':"Stabilité", 'rating':"Note", 'camera':"👤 Caméra Biométrique", 'sony_t':"🤖 Agent Sony - Bienvenue", 'sony_s':"Bienvenue. Je suis Sony, je présente pour Ali Arfaoui. FlashDeal est prêt.", 'lang_c': 'fr-FR'},
'Italiano': {'motto':"Parla. Paga. Fatto.", 'saden':"Sicurezza Saden: Token Reciproco", 'hub':"Controllo Intelligente 🏠🚗", 'buy':"Concludi Affare 🤝", 'success':"Affare Fatto!", 'sync':"Sincronizza 🛡️", 'car':"Avvia Auto 🔑", 'home':"Gestisci Casa 🏠", 'sos':"Attiva SOS 🚨", 'mem':"📜 Registro Memoria", 'standard':"Modalità Standard", 'master':"Maestro Alpha 🔓", 'price':"Prezzo", 'stability':"Stabilità", 'rating':"Voto", 'camera':"👤 Telecamera Biometrica", 'sony_t':"🤖 Agente Sony - Benvenuto", 'sony_s':"Benvenuto. Sono Sony, presento per Ali Arfaoui. FlashDeal è pronto.", 'lang_c': 'it-IT'},
'Arabic': {'motto':"تحدث. ادفع. تم.", 'saden':"أمان سادن: التوكن المتبادل", 'hub':"مركز التحكم الذكي 🏠🚗", 'buy':"إبرام الصفقة 🤝", 'success':"تمت الصفقة بنجاح!", 'sync':"مزامنة التوكن 🛡️", 'car':"تشغيل السيارة 🔑", 'home':"إدارة المنزل 🏠", 'sos':"تفعيل الطوارئ 🚨", 'mem':"📜 سجل الذاكرة", 'standard':"الوضع العادي", 'master':"ماستر ألفا 🔓", 'price':"الثمن", 'stability':"الاستقرار", 'rating':"التقييم", 'camera':"👤 كاميرا الهوية الحيوية", 'sony_t':"🤖 الوكيل صوني - ترحيب", 'sony_s':"أهلاً بكم. أنا صوني، أتحدث نيابة عن علي العرفاوي. فلاش ديل جاهز للعرض.", 'lang_c': 'ar-SA'}
}

# --- 4. الجانب الأيسر (الخيارات والذاكرة) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/star--v1.png", width=60) # 4. الشعار
    # 17. خيارات اللغات الأربع (مترجمة ديناميكياً)
    selected_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
    t = LANG_DICT[selected_lang] # قمة النص المترجم
    
    st.divider()
    # 18. خيارات Standard و Master Alpha
    acc_mode = st.radio("Access Level", [t['standard'], t['master']])
    
    # 19. زر SOS
    if st.button(t['sos'], type="secondary"): 
        st.error("🚨 EMERGENCY ACTIVATED"); add_to_memory("SOS Triggered by Ali")
    
    st.divider()
    # 20. سجل الذاكرة
    with st.expander(t['mem'], expanded=True):
        if not st.session_state.history: st.write("No active logs.")
        else:
            for item in reversed(st.session_state.history):
                st.markdown(f"<p class='log-text'>{item}</p>", unsafe_allow_html=True)

# --- 5. الواجهة الرئيسية (تنفيذ الـ 20 نقطة بدقة) ---

# 1-3: العنوان، النجمتان، والنجمة الثالثة تحتهم
current_time = time.strftime("%d/%m/%Y - %H:%M:%S")
st.markdown("<h1 class='title-box'>🌟 My FlashDeal Star 🌟</h1>", unsafe_allow_html=True)
st.markdown('<div class="big-star">★</div>', unsafe_allow_html=True) # النجمة الثالثة

# 5: التوقيت والتاريخ
st.markdown(f"<p style='text-align:center; color:#4facfe; font-weight:bold;'>🕒 {current_time}</p>", unsafe_allow_html=True)
st.divider()

# 6: أزرار الهوية الخمسة (بأيقونات وروح كودك الأولي)
st.markdown("### 👤 Identity Verification")
cols_auth = st.columns(5)
with cols_auth[0]: 
    if st.button("👤 Face"): st.success("Verified ✅"); add_to_memory("Face Auth: Ali")
with cols_auth[1]:
    if st.button("🔑 Key"): st.info("Key Synced 🔑"); add_to_memory("Key Auth: Ali")
with cols_auth[2]:
    if st.button("✋ Sign"): st.warning("Gesture Read ✋"); add_to_memory("Sign Auth: Ali")
with cols_auth[3]:
    if st.button("🔒 Lock"): st.error("System Locked 🔒"); add_to_memory("Lock Triggered")
with cols_auth[4]:
    if st.button("💎 Gem"): st.balloons(); add_to_memory("Premium Gem Activated")

# 7, 10-11: أمان سادن والتوكن (بكلمة مرور لإخفائها "العين")
st.markdown(f'<div class="glass-card"><h3>🛡️ {t["saden"]}</h3>', unsafe_allow_html=True)
col_tok1, col_tok2, col_sync = st.columns([2, 2, 1])
with col_tok1: 
    st.text_input("Main Token ID", value="ALI-ALPHA-99", type="password", help="Hides for security") # 10
with col_tok2:
    st.text_input("Mutual Token ID", value="SADEN-2026-X", type="password") # 11
with col_sync:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(t['sync']): st.success("Tokens Synced ✅"); add_to_memory("Saden Tokens Synced")
st.markdown('</div>', unsafe_allow_html=True)

# 8-9: التحكم والكاميرا
st.markdown(f"### {t['hub']}")
col_hub1, col_hub2, col_cam = st.columns([1, 1, 2])
with col_hub1: 
    if st.button(t['car']): st.toast("🚗 Engine On!"); add_to_memory("Car Started") # 8
with col_hub2:
    if st.button(t['home']): st.toast("🏠 Home Mode Active"); add_to_memory("Home Managed") # 8
with col_cam:
    st.camera_input(t['camera'], key="cam_input") # 9

# 12-14: إبرام الصفقة، مستطيل التفاعل، الاحتفال، الشهادة
st.divider()
st.markdown(f'<div class="glass-card" style="text-align:center;"><h2>🤝 {t["buy"]}</h2>', unsafe_allow_html=True)
st.markdown("<h1>🤝</h1>", unsafe_allow_html=True) # رمز التصافح (12)
chat_val = st.text_input("💬 Talk to Sony / Ali (Text Interaction)", placeholder="Type command...", key="deal_chat") # 13
if st.button(t['buy'], type="primary", use_container_width=True): # زر إتمام الصفقة (13)
    # الاحتفال (13)
    st.balloons(); st.snow(); st.toast(t['success'])
    add_to_memory("Deal Executed Successfully by Ali")
    # الموسيقى (13)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", start_time=0)
    # 14. إصدار الشهادة الذهبية باسم علي العرفاوي
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%); padding: 30px; border-radius: 15px; color: #000; border: 2px solid #fff;'>
        <h2 style='text-align:center; font-family:serif;'>🏆 TRANSACTION CERTIFICATE 🏆</h2>
        <p style='text-align:center; font-size:1.2rem;'>This confirms that <b>ALI ARFAOUI</b> (Hannibal85090)</p>
        <p style='text-align:center;'>has successfully completed the deal via <b>FlashDeal Star</b>.</p>
        <p style='text-align:center; font-family:monospace;'>Code: STAR-{uuid.uuid4().hex[:12].upper()}-{int(time.time())}</p>
        <p style='text-align:center;'>Date: {current_time} | Secured by Saden</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 15-16: سماعات الأذن، الثمن، تقييم البضاعة، والوكيل صوني
st.divider()
col_price, col_sony = st.columns([1, 2])
with col_price: # 15
    st.markdown(f'<div class="glass-card" style="text-align:center;"><h3>🎧 {t["motto"]}</h3>', unsafe_allow_html=True)
    st.metric(label=t['price'], value="$99.99", delta=t['stability']+" 100%", delta_color="normal")
    # تقييم البضاعة بالنجوم (طلب إضافي)
    st.write(f"{t['rating']}:")
    st.markdown("<span style='color:green; font-size:1.5rem;'>★ ★ ★ ★ ☆</span>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_sony: # 16. الوكيل صوني للعرض والتفاعل
    st.markdown(f'<div class="glass-card"><h3>{t["sony_t"]}</h3>', unsafe_allow_html=True)
    # مستطيل للتفاعل (كتابة وصوت كلاهما)
    col_s_text, col_s_voice = st.columns([3, 1])
    with col_s_text:
        sony_chat = st.text_input("Talk to Sony Agent:", key="sony_chat_in", placeholder="How can I help you, Ali?")
        if sony_chat: add_to_memory(f"Chat with Sony: {sony_chat}")
    with col_s_voice:
        st.markdown("<br>", unsafe_allow_html=True)
        # زر تشغيل العرض الصوتي الترحيبي باسم علي العرفاوي
        if st.button("🔊 Start Pitch"):
            sony_speak(t['sony_s'], t['lang_c'])
            add_to_memory("Sony Agent started voice pitch")
    # رابط مباشر بـ Gemini (الحل الجذري للتعقيد)
    st.markdown('<a href="https://gemini.google.com/app" target="_blank" style="text-decoration:none;"><button style="width:100%; background-color:#4285F4; color:white; border:none; padding:10px; border-radius:8px; font-weight:bold;">🗣️ Open Gemini for Live Chat (Advanced AI)</button></a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
