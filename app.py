import os
import random
import streamlit as st

# -----------------------------
# Load sounds (same as your code)
# -----------------------------
path = "sound_effects"
sounds1 = os.listdir(path)

sounds = []
for i in sounds1:
    sounds.append(f"{path}/{i}")

# -----------------------------
# Initialize game state
# -----------------------------
if "sound" not in st.session_state:
    num = random.randint(0, len(sounds) - 1)
    st.session_state.sound = sounds[num]
    st.session_state.sound_answer = st.session_state.sound.replace("-", " ").replace("_", " ")[32:-4]
    st.session_state.gave_up = False
    st.session_state.typed = ""

sound = st.session_state.sound
sound_answer = st.session_state.sound_answer

# -----------------------------
# UI (mirrors your Tkinter layout)
# -----------------------------
st.title("Surviv.io Sound Effect")

# Play sound button (replaces mixer)
if st.button("Play sound"):
    st.audio(sound)

# Give up button
if st.button("Give Up"):
    st.session_state.gave_up = True

if st.session_state.gave_up:
    st.info(f"Answer: {sound_answer}")

# -----------------------------
# Build cleaned names list (same as your code)
# -----------------------------
sounds2 = [i[32:-4].replace("-", " ").replace("_", " ") for i in sounds]

# -----------------------------
# Filtering logic (same as your code)
# -----------------------------
typed = st.text_input("Type to filter:", st.session_state.typed)
st.session_state.typed = typed

if typed == "":
    filtered = sounds2
else:
    filtered = [s for s in sounds2 if typed.lower() in s.lower()]

# Dropdown (replaces Combobox)
guess = st.selectbox("Choose a sound:", filtered)

# -----------------------------
# Guess checking (same logic)
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
