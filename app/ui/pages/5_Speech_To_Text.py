import streamlit as st
import requests
from streamlit_mic_recorder import mic_recorder

st.set_page_config(page_title="Speech To Text")

st.title("🎤 Live AI Interview")

st.write("Click the microphone and answer the interview question.")

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=True,
    use_container_width=True,
    key="recorder"
)

if audio:

    st.audio(audio["bytes"])

    files = {
        "file": (
            "candidate_answer.wav",
            audio["bytes"],
            "audio/wav"
        )
    }

    with st.spinner("Transcribing..."):

        response = requests.post(
            "http://127.0.0.1:8000/speech/transcribe",
            files=files
        )

    if response.status_code == 200:

        data = response.json()

        st.success("Transcript Generated")

        st.subheader("Transcript")

        st.write(data["transcript"])

        st.session_state["transcript"] = data["transcript"]

    else:

        st.error("Transcription Failed")