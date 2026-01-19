import streamlit as st
import json
import os
import sys

# ---------- Import helper ----------
project_path = r"C:\Users\sashi\OneDrive\Documents\Langchain"
if project_path not in sys.path:
    sys.path.append(project_path)

from grok_json import get_response

# ---------- Page config ----------
st.set_page_config(page_title="🪞 Product → JSON Chatbot", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
body, .stApp {
    background-color: white !important;
    color: black !important;
}
.stChatMessage {
    background-color: white !important;
    color: black !important;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}
pre {
    background-color: #1e1e1e !important;   /* dark box */
    color: #00ff7f !important;               /* green text */
    border-radius: 10px;
    padding: 12px;
    font-family: monospace;
    font-size: 15px;
    line-height: 1.5em;
    overflow-x: auto;
}
</style>
""", unsafe_allow_html=True)

# ---------- Chat init ----------
st.title("🪞 Product → JSON Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I'm your JSON Converter bot. Describe your product and I’ll generate structured JSON for you."}
    ]

# ---------- Show history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        content = msg["content"].strip()
        # Detect JSON-like message
        if (content.startswith("{") or content.startswith("[")) and not content.startswith("👋"):
            try:
                parsed = json.loads(content)
                formatted_json = json.dumps(parsed, indent=4)
                st.markdown(f"<pre>{formatted_json}</pre>", unsafe_allow_html=True)
            except Exception:
                st.code(content, language="json")
        else:
            st.markdown(content)

# ---------- Input ----------
if prompt := st.chat_input("Describe a product here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Converting to JSON..."):
            output = get_response(prompt)

        # Try to pretty print JSON
        try:
            parsed = json.loads(output)
            formatted_json = json.dumps(parsed, indent=4)
            st.markdown(f"<pre>{formatted_json}</pre>", unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": formatted_json})
        except Exception:
            # fallback if invalid JSON
            st.code(output, language="json")
            st.session_state.messages.append({"role": "assistant", "content": output})
