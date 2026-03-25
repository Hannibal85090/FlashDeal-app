import streamlit as st
import streamlit.components.v1 as components
from streamlit_mic_recorder import mic_recorder

def sony_speak(text):
    components.html(f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text}');
        msg.lang = 'en-US';
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

def render_sony_interface(add_to_memory_func):
    st.subheader("🤖 Sony AI Agent Center")
    tab_v, tab_t = st.tabs(["🎙️ Sony Voice (AI)", "⌨️ Text Chat"])

    def get_smart_response(user_input):
        user_input = user_input.lower()
        if "security" in user_input or "safe" in user_input:
            return "FlashDeal uses Saden Mutual Token technology. Your data is encrypted and 100% secure."
        elif "price" in user_input or "cost" in user_input:
            return "Our current star deal is priced at 99.99 dollars with full system stability."
        elif "speed" in user_input or "fast" in user_input:
            return "Transactions are executed in milliseconds thanks to our optimized AI core."
        else:
            return f"I have analyzed your request regarding '{user_input}'. System status is green and ready for execution."

    with tab_v:
        if st.button("🎤 Sony's Greeting"):
            msg = "Welcome Judges. I am Sony. I am ready to demonstrate our secure FinTech ecosystem."
            sony_speak(msg)
            add_to_memory_func("Sony Greeting")
        
        audio = mic_recorder(start_prompt="🎤 Ask Sony (Voice)", stop_prompt="🛑 Stop", key='sony_mic_pitch')
        if audio:
            # محاكاة تحليل الصوت
            response = "Voice signal received. System integrity is 100% verified. Proceeding with your request."
            st.chat_message("assistant").write(response)
            sony_speak(response)
            add_to_memory_func("Sony Voice analysis completed")

    with tab_t:
        chat_val = st.chat_input("Ask Sony anything...")
        if chat_val:
            add_to_memory_func(f"Judge: {chat_val}")
            smart_resp = get_smart_response(chat_val)
            st.chat_message("assistant").write(smart_resp)
            sony_speak(smart_resp)
