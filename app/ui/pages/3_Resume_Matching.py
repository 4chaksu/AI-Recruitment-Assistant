import streamlit as st
import requests

st.title("🎯 Resume Matching")

# Check Resume
if "resume_text" in st.session_state:
    st.success("✅ Resume Uploaded")
else:
    st.warning("Please upload Resume first.")

# Check JD
if "jd_text" in st.session_state:
    st.success("✅ Job Description Uploaded")
else:
    st.warning("Please upload Job Description first.")

# Stop if missing
if (
    "resume_text" not in st.session_state
    or
    "jd_text" not in st.session_state
):
    st.stop()

# Show summaries
with st.expander("Resume Summary"):
    st.write(st.session_state["resume_summary"])

with st.expander("Job Description Summary"):
    st.write(st.session_state["jd_summary"])

# Match Button
if st.button("🚀 Match Candidate"):

    payload = {
        "resume_text": st.session_state["resume_text"],
        "jd_text": st.session_state["jd_text"]
    }

    response = requests.post(
        "http://127.0.0.1:8000/match/",
        json=payload
    )

    if response.status_code == 200:

        data = response.json()

        st.metric(
            label="Match Score",
            value=f"{data['match_score']}%"
        )

        st.success(data["recommendation"])

    else:
        st.error("Matching Failed")