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

    with st.spinner("Analyzing resume..."):
        response = requests.post(
            "http://127.0.0.1:8000/resume/upload",
            files=files
        )

    if response.status_code == 200:

        data = response.json()

        st.success("Resume uploaded successfully!")

        # ===== Resume Summary =====
        st.subheader("📝 Resume Summary")
        st.write(data["summary"])

        # ===== Resume Text =====
        with st.expander("📄 Extracted Resume Text"):
            st.text_area(
                "Resume Content",
                data["resume_text"],
                height=400
            )

    else:
        st.error("Upload failed")