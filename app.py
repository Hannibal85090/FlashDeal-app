    st.info("Ready for your voice command.")
    if st.button("ACTIVATE VOICE RECORDING"):
        st.success("Voice recognition active: 'Send 50 Tokens to My Star'...")

with tab2:
    st.markdown("### My FlashDeal Wallet")
    c1, c2 = st.columns(2)
    # Handling the 'token' aspect as requested
    c1.metric("Current Balance", "1,250 FTK", delta="Synced")
    c2.metric("Last Move", "-50 FTK", delta_color="inverse")
    st.divider()
    st.caption("All transactions are secured via Mutual Token encryption.")

with tab3:
    st.markdown("### Protection Layers")
    # Security options for customers
    st.checkbox("Face ID Biometrics", value=True)
    st.checkbox("Mutual Token Protocol", value=True)
    st.checkbox("Body Movement Matching", value=False)
    st.checkbox("Simple/Complex Secret Code", value=True)

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color: #7000FF;'>My FlashDeal Star</h2>", unsafe_allow_html=True)
st.sidebar.write("User: Hannibal85090")
st.sidebar.write("Device: Active 🟢")
st.sidebar.divider()
st.sidebar.info("Quality Level: High Premium")
