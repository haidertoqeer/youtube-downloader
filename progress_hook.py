import streamlit as st

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded_bytes = d.get('downloaded_bytes')
        if total_bytes and downloaded_bytes:
            percentage = downloaded_bytes / total_bytes
            st.session_state.download_percentage = percentage
    elif d['status'] == 'finished':
        st.session_state.download_percentage = 1.0
