import streamlit as st

st.title("🎧 Mood Playlist App")

moods = ["Happy", "Sad", "Relaxed", "Energetic", "Romantic", "Ashiqui 2"]

# ✅ Use EMBED links here
playlists = {
    "ashiqui2": "https://open.spotify.com/embed/album/0Rkv5iqjF2uenfL0OVB8hg",
    "Happy": "https://open.spotify.com/embed/playlist/3iDiMSVkGIXm8yCWcIomdY",
    "Sad": "https://open.spotify.com/embed/playlist/5QMgdPH8QvUOxcmX4bVs5d",
    "Relaxed": "https://open.spotify.com/embed/playlist/4m2R6xXf67zlHqf5kdT0mf",
    "Energetic": "https://open.spotify.com/embed/playlist/2iwCRchSeIocvoUcyQ77l7",
    "Romantic": "https://open.spotify.com/embed/playlist/0G8PGDiBwv8k8GCJHXSMzS",
    "ashiqui2": "https://open.spotify.com/embed/album/0Rkv5iqjF2uenfL0OVB8hg",
}

mood = st.selectbox("How are you feeling today?", moods)

if mood:
    st.subheader(f"Playlist for your mood: {mood}")
    st.components.v1.iframe(playlists[mood])
