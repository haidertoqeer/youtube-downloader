from youtube_downloader import download_youtube_video

url = "https://www.youtube.com/watch?v=ogfY1wMMNEo&ab_channel=IrfanMalik"  # Replace with a valid URL
output_path = "./downloads"

try:
    download_youtube_video(url, output_path)
except Exception as e:
    print(f"Download failed: {e}")
