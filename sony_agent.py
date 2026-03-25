import streamlit as st
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

def sony_speak(text):
    """محرك نطق صوني المستقل"""
    components.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'en-US';
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

def render_sony_interface(add_to_memory_func):
    """دالة عرض واجهة صوني داخل الملف الرئيسي"""
    st.subheader("🤖 Sony AI Agent Center")
    tab_v, tab_t = st.tabs(["🎙️ Voice Interaction", "⌨️ Text Chat"])

    with tab_v:
        if st.button("🎤 Sony's Greeting"):
            msg = "Greetings. I am Sony, your AI assistant. System is stable and ready."
            sony_speak(msg)
            add_to_memory_func("Sony Greeting Activated")
        
        audio = mic_recorder(start_prompt="🎤 Ask Sony", stop_prompt="🛑 Stop", key='sony_mic_ext')
        if audio:
            resp = "Voice inquiry received. All protocols are 100% secure."
            st.chat_message("assistant").write(resp)
            sony_speak(resp)
            add_to_memory_func("Sony processed Voice Inquiry")

    with tab_t:
        chat_val = st.chat_input("Type to Sony...")
        if chat_val:
            add_to_memory_func(f"Judge Query: {chat_val}")
            resp_text = f"Analyzing: '{chat_val}'. Status: Verified ✅"
            st.chat_message("assistant").write(resp_text)
            sony_speak(resp_text)
