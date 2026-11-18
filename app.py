import streamlit as st
from groq import Groq
st.set_page_config(page_title = '', layout='centered')
st.title("AI Interview Assistant")
st.caption("Launched by baby")
try:
  client = Groq(api_key = st.secrets["GROQ_API"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
