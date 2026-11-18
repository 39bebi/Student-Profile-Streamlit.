import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'Student Profile Application', layout='centered')
st.title("🎓Student Profile Application")
st.caption("Developed by:Baby")
try:
  client = Groq(api_key = st.secrets["GROQ_API"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
name = st.text_area("Student Name", placeholder="Enter your name")

roll = st.text_area("USN / Roll no.", placeholder="Enter your USN")

department = st.text_area("Department", placeholder="Enter your department")
