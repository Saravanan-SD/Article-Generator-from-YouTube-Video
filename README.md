# Article-Generator-from-YouTube-Video

This Streamlit app extracts audio from a YouTube video, transcribes it, and generates a news article using OpenAI's GPT-3.5 model.

## Features

- **Input YouTube Video URL**: Enter the URL of the video to analyze.
- **Start Analysis**: Click to begin the process.
- **Audio Playback**: Listen to the extracted audio.
- **Transcript Extraction**: View the transcribed text.
- **Generated Article**: Read the article generated from the transcript.
- **Download Transcript and Article**: Get a zip file with both transcript and article.

## How it Works

1. **Audio Extraction**: Download audio from the YouTube video.
2. **Transcription**: Convert audio to text.
3. **Article Generation**: Use the text to generate a news article.
4. **Output Download**: Save transcript and article as text files in a zip.

## Dependencies

- `streamlit`: Web app framework.
- `pytube`: Download YouTube videos.
- `whisper`: Audio processing.
- `openai`: Interact with GPT-3.5.
- `dotenv`: Manage environment variables.
- `pathlib`, `shutil`, `zipfile`: File handling.

## Setup

1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set your OpenAI API key in the environment: `OPENAI_API_KEY`.
4. Run the app: `streamlit run app.py`.
5. Enter YouTube URL and start.

## Note

Ensure correct environment variables and an internet connection.
