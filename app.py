import os
import streamlit as st
from youtube_downloader import download_youtube_video
from ai_enhancements import suggest_related_videos
from pytube import YouTube
from progress_hook import progress_hook

# Function to get the default download directory
def get_default_download_directory():
    if os.name == 'nt':  # For Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # For macOS and Linux
        return os.path.join(os.environ['HOME'], 'Downloads')

# Set the default output path
default_output_path = get_default_download_directory()

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL")
output_path = st.text_input("Enter Output Path", default_output_path)

if 'download_percentage' not in st.session_state:
    st.session_state.download_percentage = 0

if st.button("Download"):
    if url and output_path:
        try:
            yt = YouTube(url)
            st.image(yt.thumbnail_url, caption=yt.title)
            download_youtube_video(url, output_path, progress_hook)
            st.success("Video downloaded successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL and output path.")

if st.session_state.download_percentage:
    st.progress(st.session_state.download_percentage)

if st.button("Suggest Related Videos"):
    if url:
        try:
            yt = YouTube(url)
            title = yt.title
            related_videos = suggest_related_videos(title)
            st.write("Related Videos:")
            st.write(related_videos)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
