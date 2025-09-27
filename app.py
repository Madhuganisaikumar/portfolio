import streamlit as st
import time
import datetime

# ----------- Custom CSS (same as before) ----------
st.markdown("""...CSS block (as in previous code)...""", unsafe_allow_html=True)

# ----------- Hacker Loading Splash ----------
if "loaded" not in st.session_state:
    loading_msgs = [
        "In",
        "Loading essential services..",
        "Configuring security protocols...",
        "Launching interface..."
    ]

    progress_bar = st.empty()
    glow_header = st.empty()
    loadmsg = st.empty()
    statusmsg = st.empty()

    glow_header.markdown('<div class="glow">ZAP</div>', unsafe_allow_html=True)

    for i in range(101):
        if i < 25:
            msg = loading_msgs[0]
        elif i < 50:
            msg = loading_msgs[1]
        elif i < 85:
            msg = loading_msgs[2]
        else:
            msg = loading_msgs[3]
        loadmsg.markdown(f'<div class="loading-msg">{msg}</div>', unsafe_allow_html=True)
        progress_bar.progress(i)
        statusmsg.markdown(f'<div class="init-status">System initialization: {i}%</div>', unsafe_allow_html=True)
        time.sleep(0.03)
    st.session_state.loaded = True
    st.experimental_set_query_params(loaded=True)
    st.success("System Initialized! Click 'Rerun' if stuck.")
    st.stop()  # This will stop the script after splash; next run will show desktop

# ----------- Desktop Portfolio Screen -----------
# ... rest of your desktop interface code ...
