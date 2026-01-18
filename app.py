import os
import random
import streamlit as st

path = "sound_effects"
sounds1 = os.listdir(path)
sounds = [f"{path}/{i}" for i in sounds1]

if "sound" not in st.session_state:
    num = random.randint(0, len(sounds) - 1)
    st.session_state.sound = sounds[num]
    st.session_state.sound_answer = st.session_state.sound.replace("-", " ").replace("_", " ")[32:-4]
    st.session_state.search = ""
    st.session_state.gave_up = False
    st.session_state.played = False

sound = st.session_state.sound
sound_answer = st.session_state.sound_answer

if st.session_state.played is False:
    st.audio(sound)
    st.session_state.played = True

st.title("Surviv.io Sound Effect")

if st.button("Give Up"):
    st.session_state.gave_up = True

if st.session_state.gave_up:
    st.info(sound_answer)

sounds2 = [i[32:-4].replace("-", " ").replace("_", " ") for i in sounds]

search = st.text_input("Search & Choose:", st.session_state.search)
st.session_state.search = search

if search == "":
    filtered = sounds2
else:
    filtered = [s for s in sounds2 if search.lower() in s.lower()]

guess = st.selectbox("", filtered)

if st.button("Submit Guess"):
    if guess == sound_answer:
        st.success("Correct!")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
    else:
        st.error(f"{guess} is incorrect")
