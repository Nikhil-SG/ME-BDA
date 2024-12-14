import streamlit as st
import pandas as pd
import json
from streamlit.components.v1 import html
from streamlit.logger import get_logger
import asyncio
import vertexai
from vertexai.generative_models import GenerationConfig, GenerativeModel

logger = get_logger(__name__)

vertexai.init(project="bubbly-benefit-426415-h5", location="us-central1")
def fetch_response(prompt):
    system_prompt = f"""You are a bot that is an expert in data engineering, Analytics, ML , AI and Generative AI. You are puposed to answer
                        student questions. Please make sure you explain the answer to the student. If th student is making small talk
                        provide appropriate answers. If the student deviates from the topic do not answer the questions.
                        {prompt}
                        """
    model = GenerativeModel("gemini-1.5-flash")
    return(model.generate_content(system_prompt).text)


def generate_response(prompt):
    """Generates and displays a response to the user's prompt.

    This function takes a user prompt as input, generates an SQL query and
    response using the `generate_sql_results` function, and displays the
    results in a conversational format using Streamlit's chat message feature.

    Args:
        prompt (str): The user's input prompt.
    """
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    msg = "Generating Response"
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    msg = fetch_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)


    
st.set_page_config(page_title='Manipal Student Assist', page_icon="📊", initial_sidebar_state="expanded", layout='wide')
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.title("Manipal Student Assist")

       
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Frequently Asked Questions"}]

if prompt := st.chat_input():
   generate_response(prompt)