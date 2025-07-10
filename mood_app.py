# import streamlit as st
# st.title("🎧 Mood Playlist App")
# moods = ["Happy", "Sad", "Relaxed", "Energetic", "Romantic"]
# playlists = {
#     "Happy": "https://open.spotify.com/playlist/3iDiMSVkGIXm8yCWcIomdY?si=-cn3w1NgTtaT5aWSF1Qdlg&pi=6PF9nj9pSXOxA",
#     "Sad": "https://open.spotify.com/playlist/5QMgdPH8QvUOxcmX4bVs5d?si=tDJNF_qOT9GE93CO-bLGxw&pi=bQix83QLQtuQ1",
#     "Relaxed": "https://open.spotify.com/playlist/4m2R6xXf67zlHqf5kdT0mf?si=CaMMcN8aSMeePImky6-eKw",
#     "Energetic": "https://open.spotify.com/playlist/2iwCRchSeIocvoUcyQ77l7?si=67QWlKFPQnG2IQ-JClDGBQ",
#     "Romantic": "https://open.spotify.com/playlist/0G8PGDiBwv8k8GCJHXSMzS?si=yi-FXevGQ6mgb5yxIO0Q2Q"
# }
# mood = st.selectbox("How are you feeling today?", moods)
# if mood:
#     st.subheader(f"Playlist for your mood: {mood}")
#     st.components.v1.iframe(playlists[mood], height=400)

import streamlit as st

st.title("🎧 Mood Playlist App")

moods = ["Happy", "Sad", "Relaxed", "Energetic", "Romantic"]

# ✅ Use EMBED links here
playlists = {
    "Happy": "https://open.spotify.com/embed/playlist/3iDiMSVkGIXm8yCWcIomdY",
    "Sad": "https://open.spotify.com/embed/playlist/5QMgdPH8QvUOxcmX4bVs5d",
    "Relaxed": "https://open.spotify.com/embed/playlist/4m2R6xXf67zlHqf5kdT0mf",
    "Energetic": "https://open.spotify.com/embed/playlist/2iwCRchSeIocvoUcyQ77l7",
    "Romantic": "https://open.spotify.com/embed/playlist/0G8PGDiBwv8k8GCJHXSMzS",
    "ashiqui2": "https://open.spotify.com/embed/album/0Rkv5iqjF2uenfL0OVB8hg"
}

mood = st.selectbox("How are you feeling today?", moods)

if mood:
    st.subheader(f"Playlist for your mood: {mood}")
    st.components.v1.iframe(playlists[mood], height=400)
