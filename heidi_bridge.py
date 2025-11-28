import streamlit as st
from datetime import datetime

# ——— MAKE IT LOOK EXACTLY LIKE REAL HEIDI ———
st.set_page_config(page_title="Heidi Patient Bridge", page_icon="favicon", layout="centered")

# Custom CSS – makes it 100% Heidi-blue and clean
st.markdown("""
<style>
    .main {background-color: #f8f9ff; padding: 2rem;}
    .stChatMessage {background-color: white; border-radius: 12px; padding: 1rem; margin: 0.5rem 0;}
    .user {background-color: #e6f0ff !important;}
    .heidi {background-color: #0066ff; color: white; border-radius: 12px 12px 12px 0;}
    h1 {color: #0066ff; text-align: center; font-family: 'Helvetica Neue', sans-serif;}
    .qr {text-align: center; margin: 2rem 0;}
</style>
""", unsafe_allow_html=True)

st.title("Heidi Patient Bridge")
st.markdown("**Type one of the two commands below** – watch the magic happen")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "heidi", "content": "Hello! I'm ready when you are.\n\nTry typing:\n`pull full record`\nor\n`give patient QR`"}
    ]

# Display chat
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"<div class='stChatMessage user'><strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='stChatMessage heidi'><strong>Heidi:</strong> {message['content']}</div>", unsafe_allow_html=True)

# Input box
if prompt := st.chat_input("Ask Heidi Anything…"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

    # ——— THIS IS WHERE THE MAGIC WILL START ———
    # (We will fill this in the next steps)
    if "pull full record" in prompt.lower():
        st.session_state.messages.append({"role": "heidi", "content": "Fetching full record from the EMR… please wait 15 seconds"})
        st.rerun()
    elif "give patient qr" in prompt.lower():
        st.session_state.messages.append({"role": "heidi", "content": "Creating your patient’s forever health folder…\n\n[Big QR will appear here in Step 7]"})
        st.rerun()
