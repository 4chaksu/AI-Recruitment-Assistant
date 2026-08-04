import streamlit as st
import requests

st.title("📋 Job Description Upload")

uploaded_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    with st.spinner("Analyzing Job Description..."):

        response = requests.post(
            "http://127.0.0.1:8000/jd/upload",
            files=files
        )

    if response.status_code == 200:

        data = response.json()

        # Save in Session
        st.session_state["jd_text"] = data["jd_text"]
        st.session_state["jd_summary"] = data["summary"]

        st.success("Job Description uploaded successfully!")

        st.subheader("📝 JD Summary")
        st.write(data["summary"])

        with st.expander("📄 Original JD"):
            st.text_area(
                "",
                data["jd_text"],
                height=350
            )

    else:
        st.error("Upload Failed")