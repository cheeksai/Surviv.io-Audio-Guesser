import os
import random
import streamlit as st

# Load sounds
path = "sound_effects"
sounds1 = os.listdir(path)

# Build full paths
sounds = [f"{path}/{i}" for i in sounds1]

# Initialize game state
if "sound" not in st.session_state:
    num = random.randint(0, len(sounds) - 1)
    st.session_state.sound = sounds[num]
    st.session_state.sound_answer = st.session_state.sound.replace("-", " ").replace("_", " ")[32:-4]
    st.session_state.gave_up = False
    st.session_state.typed = ""

sound = st.session_state.sound
sound_answer = st.session_state.sound_answer

st.title("Surviv.io Sound Effect Guesser")

# --- PLAY SOUND BUTTON ---
if st.button("Play Sound"):
    st.audio(sound)

# --- GIVE UP BUTTON ---
if st.button("Give Up"):
    st.session_state.gave_up = True

if st.session_state.gave_up:
    st.info(f"Answer: {sound_answer}")

# --- BUILD CLEANED NAMES LIST ---
sounds2 = [i[32:-4].replace("-", " ").replace("_", " ") for i in sounds]

# --- FILTERING BEHAVIOR (same as your Tkinter version) ---
typed = st.text_input("Type to filter sounds:", st.session_state.typed)
st.session_state.typed = typed

if typed == "":
    filtered = sounds2
else:
    filtered = [s for s in sounds2 if typed.lower() in s.lower()]

# Dropdown of filtered results
guess = st.selectbox("Choose a sound:", filtered)

# --- CHECK GUESS ---
if st.button("Submit Guess"):
    if guess == sound_answer:
        st.success("Correct!")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
    else:
        st.error(f"{guess} is incorrect")
