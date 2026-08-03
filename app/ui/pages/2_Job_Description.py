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

        st.success("Job Description uploaded successfully!")

        # ===== JD Summary =====
        st.subheader("📝 Job Description Summary")
        st.write(data["summary"])

        # ===== Original JD =====
        with st.expander("📄 Original Job Description"):
            st.text_area(
                "Job Description",
                data["jd_text"],
                height=400
            )

    else:
        st.error("Failed to upload Job Description.")