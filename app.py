import os
import random
import streamlit as st

# -----------------------------
# Load sounds (same as your code)
# -----------------------------
path = "icons"
sounds1 = os.listdir(path)

sounds = [f"{path}/{i}" for i in sounds1]

# -----------------------------
# Initialize game state
# -----------------------------
if "sound" not in st.session_state:
    num = random.randint(0, len(sounds) - 1)
    st.session_state.sound = sounds[num]
    st.session_state.sound_answer = st.session_state.sound.replace("-", " ").replace("_", " ")[32:-4]
    st.session_state.typed = ""
    st.session_state.gave_up = False
    st.session_state.played_once = False

sound = st.session_state.sound
sound_answer = st.session_state.sound_answer

# -----------------------------
# Play sound automatically ONCE
# -----------------------------
if not st.session_state.played_once:
    st.audio(sound)
    st.session_state.played_once = True

st.title("Surviv.io Sound Effect")

# -----------------------------
# Give Up button
# -----------------------------
if st.button("Give Up"):
    st.session_state.gave_up = True

if st.session_state.gave_up:
    st.info(f"Answer: {sound_answer}")

# -----------------------------
# Build cleaned names list
# -----------------------------
sounds2 = [i[32:-4].replace("-", " ").replace("_", " ") for i in sounds]

# -----------------------------
# FILTER BUILT INTO DROPDOWN
# (exactly like your Tkinter Combobox)
# -----------------------------
typed = st.text_input("Search:", st.session_state.typed)
st.session_state.typed = typed

if typed == "":
    filtered = sounds2
else:
    filtered = [s for s in sounds2 if typed.lower() in s.lower()]

# Dropdown with filtered results
guess = st.selectbox("Choose a sound:", filtered)

# -----------------------------
# Guess checking
# -----------------------------
if st.button("Submit Guess"):
    if guess == sound_answer:
        st.success("Correct!")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
    else:
        st.error(f"{guess} is incorrect")
