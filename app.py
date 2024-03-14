import streamlit as st
from openai import OpenAI
from pytube import YouTube
import os
from pathlib import Path
import shutil
from dotenv import load_dotenv
import whisper
from zipfile import ZipFile

load_dotenv()

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

@ st.cache_data
def load_model():
    model=whisper.load_model("base")
    return model

def save_audio(url):
    yt=YouTube(url)
    video=yt.streams.filter(only_audio=True).first()
    out_file=video.download()
    base,ext=os.path.splitext(out_file)
    file_name=base+ '.mp3'
    try:
        os.rename(out_file,file_name)
    except WindowsError:
        os.remove(file_name)
        os.rename(out_file, file_name)

    audio_filename= Path(file_name).stem+'.mp3'
    print(yt.title + ' downloaded')
    print(file_name)
    return yt.title, audio_filename

def audio_to_transcript(audio_file):
    model= load_model()
    result= model.transcribe(audio_file)
    transcript= result["text"]
    return transcript

def text_to_news_article(text):
    client = OpenAI()
    response= client.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt='You are a expert journalist,Write a news article in 1000 words from the below text:\n'+text,
        temperature=0.85,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0          
        )
    return response.choices[0].text


st.markdown("# **ARTICLE GENERATOR APP FROM YOUTUBE VIDEO**")
st.header("Input YouTube Video URL")

url=st.text_input('Enter the video url here')

if st.checkbox("Start Analysis"):
    video_title, audio_filename= save_audio(url)
    st.audio(audio_filename)
    transcript=audio_to_transcript(audio_filename)
    st.header('Transcript is being extracted')
    st.success(transcript)
    st.header('Article')
    result= text_to_news_article(transcript)
    st.success(result)

    transcript_txt=open("transcript.txt", "w")
    transcript_txt.write(transcript)
    transcript_txt.close()

    article_txt=open("article.txt", "w")
    article_txt.write(result)
    article_txt.close()

    zip_file= ZipFile('output.zip','w')
    zip_file.write('transcript.txt')
    zip_file.write('article.txt')
    zip_file.close()

    with open('output.zip','rb') as zip_download:
        btn=st.download_button(
            label="Download Transcript and Article",
            data=zip_download,
            file_name= 'output.zip',
            mime='application/zip'
        )
