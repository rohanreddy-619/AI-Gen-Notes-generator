import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile

def convert_and_get_text(uploaded_file):
    
    
    
    text = ""
    temp_path = None
    try:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            sound = AudioSegment.from_file(uploaded_file)
            sound.export(temp_audio_file.name, format="wav")
            temp_path = temp_audio_file.name

        
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_path) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                text = "Could not understand the audio. The speech might be unclear."
            except sr.RequestError as e:
                text = f"API service error; {e}"
        return text
    finally:
        
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)

def main():
    
    st.set_page_config(layout="wide", page_title="AI - Gen Notes", page_icon="📝")
    
    st.title("📝 AI - Gen Notes")
    st.header("Speech to Text Converter")
    st.write("Upload an audio file (WAV, MP3, etc.) and the app will transcribe the speech into text.")

    uploaded_file = st.file_uploader("Choose an audio file...", type=["wav", "mp3", "m4a", "ogg"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format=uploaded_file.type)
        
        with st.spinner('Transcribing audio... Please wait.'):
            text = convert_and_get_text(uploaded_file)
        
        st.success("Transcription Complete!")
        st.text_area("Converted Text:", text, height=250)

if __name__ == "__main__":
    main()