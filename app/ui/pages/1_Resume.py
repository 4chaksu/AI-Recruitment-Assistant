import streamlit as st
import requests

st.title("📄 Resume Upload")

uploaded_file = st.file_uploader(
    "Upload Resume",
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

    with st.spinner("Analyzing Resume..."):

        response = requests.post(
            "http://127.0.0.1:8000/resume/upload",
            files=files
        )

    if response.status_code == 200:

        data = response.json()

        # Save in Session
        st.session_state["resume_text"] = data["resume_text"]
        st.session_state["resume_summary"] = data["summary"]

        st.success("Resume uploaded successfully!")

        st.subheader("📝 Resume Summary")
        st.write(data["summary"])

        with st.expander("📄 Extracted Resume"):
            st.text_area(
                "",
                data["resume_text"],
                height=350
            )

    else:
        st.error("Upload Failed")