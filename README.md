# ARTICLE GENERATOR APP FROM YOUTUBE VIDEO

This Streamlit application serves to extract audio from a YouTube video, transcribe it, and generate a news article using OpenAI's GPT-3.5 model.

## Features

- **YouTube Video URL Input**: Input the URL of the video you want to analyze.
- **Start Analysis Checkbox**: Initiates the analysis process.
- **Audio Playback**: Listen to the extracted audio.
- **Transcript Extraction**: Displays the transcript extracted from the audio.
- **Generated Article Display**: Presents the generated news article based on the transcript.
- **Download Functionality**: Offers the ability to download both the transcript and the generated article as a zip file.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.
4. Run the `app.py` file using `streamlit run app.py`.
5. Input the YouTube video URL in the provided field.
6. Click the "Start Analysis" checkbox to begin the analysis.
7. Listen to the audio playback if desired.
8. View the extracted transcript.
9. Read the generated news article.
10. Download the transcript and article using the provided download button.

## Requirements

- `streamlit`: Web application framework.
- `openai`: Python library for interacting with OpenAI's API.
- `pytube`: Library for downloading YouTube videos.
- `whisper`: Library for working with pre-trained models for audio processing.
- `python-dotenv`: Library for managing environment variables.
- `pathlib`, `shutil`, `zipfile`: Python libraries for file manipulation.


## Contact Information

- **Name**: Saravanan S
- **Email**: saravanansd634@gmail.com
- **Linkedin**:https://www.linkedin.com/in/sdsaravanan/



