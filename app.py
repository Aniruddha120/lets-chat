import streamlit as st
from streamlit_chat import message
import google.generativeai as palm

headers = {
    "auth" : st.secrets['API_KEY'],
    "content-type": "application/json"
}

palm_api_key = st.secrets['API_KEY']

st.markdown("<h1 style='text-align: center; color: yellow;'>Let's Chat!</h1>", unsafe_allow_html=True)
with st.sidebar:
    st.title("💬 Let's Chat")
    st.markdown("Made By Aniruddha Sarkar: https://github.com/Aniruddha120")
    st.markdown("\n\nPowered By Google PaLM 2 API")
    st.markdown("\n\nReload to clear chat ")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What's on your mind??"}]
with st.form("chat_input", clear_on_submit=True):
    col1, col2 = st.columns([8, 1])

    user_prompt = col1.text_input(
        label="Your message:",
        placeholder="ask me anyting...",
        label_visibility="collapsed",
    )

    col2.form_submit_button("✈", use_container_width=True)
for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user") 
if user_prompt and palm_api_key:
    palm.configure(api_key=palm_api_key) 
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    message(user_prompt, is_user=True)
    response = palm.chat(messages=[user_prompt])  
    msg = {"role": "assistant", "content": response.last}  
    st.session_state.messages.append(msg) 
    message(msg["content"])

