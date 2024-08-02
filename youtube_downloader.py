import yt_dlp
import os

def download_youtube_video(url, output_path, progress_hook):
    try:
        # Ensure the output path exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'format': 'best',
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed! Video saved to {output_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
