📝 AI-Notes Generator

A simple web application built with Streamlit that transcribes audio files into text. Upload your lectures, meetings, or voice memos and get a written transcription in seconds.

🌟 Features

Easy-to-Use Interface: Simple web UI powered by Streamlit.

Multiple File Formats: Supports various audio formats (e.g., .mp3, .wav, .m4a, .ogg) thanks to pydub.

Accurate Transcription: Uses Google's Speech-to-Text API via the speech_recognition library.

Instant Playback: Listen to your uploaded audio file directly in the app.

🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Python 3.8+

FFmpeg

pydub requires FFmpeg for handling audio formats like MP3. You must install it on your system.

On macOS (using Homebrew): brew install ffmpeg

On Windows (using Chocolatey): choco install ffmpeg

On Ubuntu/Debian: sudo apt update && sudo apt install ffmpeg

1. Clone the Repository

First, clone this repository to your local machine:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name


2. Create a Virtual Environment (Recommended)

It's best practice to create a virtual environment to manage your project's dependencies.

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

Install all the required Python libraries using pip:

pip install streamlit speechrecognition pydub


(Alternatively, if you have a requirements.txt file, just run pip install -r requirements.txt)

🏃‍♂️ How to Run the App

With your environment activated and dependencies installed, you can run the app with a single command:

streamlit run app.py


(Replace app.py with the name of your Python script if it's different.)

Streamlit will automatically open a new tab in your default web browser pointing to your app's local URL (usually http://localhost:8501).

🙏 Thank You!

Thanks for checking out and using the AI-Notes Generator.