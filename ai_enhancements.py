from transformers import pipeline

def suggest_related_videos(video_title):
    summarizer = pipeline("summarization")
    summary = summarizer(video_title, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']
