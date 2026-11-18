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
year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)
if st.button("View My Profile"):

    if name and roll and department:

        st.success("Profile Created Successfully!")

        st.subheader("🎓 Student Profile Details")

        st.write("*Student Name:*", name)
        st.write("*USN / Roll No.:*", roll)
        st.write("*Department:*", department)
        st.write("*Current Year:*", year)

    else:
        st.warning("Please fill all the details!")
