import streamlit as st
import requests

st.title("🎤 Interview Question Generator")

if "resume_summary" not in st.session_state:
    st.warning("Please upload Resume first.")
    st.stop()

if "jd_summary" not in st.session_state:
    st.warning("Please upload Job Description first.")
    st.stop()

st.subheader("Resume Summary")

st.write(st.session_state["resume_summary"])

st.subheader("Job Description Summary")

st.write(st.session_state["jd_summary"])

if st.button("Generate Interview Questions"):

    payload = {
        "resume_summary": st.session_state["resume_summary"],
        "jd_summary": st.session_state["jd_summary"]
    }

    response = requests.post(
        "http://127.0.0.1:8000/interview/generate",
        json=payload
    )

    if response.status_code == 200:

        data = response.json()

        st.success("Interview Questions Generated")

        st.markdown(data["questions"])

    else:

        st.error("Generation Failed")