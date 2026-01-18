import os
import random
import streamlit as st

path = "icons"
files = os.listdir(path)
sounds = [os.path.join(path, f) for f in files if f.lower().endswith(".mp3")]
names = [
    os.path.splitext(os.path.basename(p))[0].replace("-", " ").replace("_", " ")
    for p in sounds
]

if "index" not in st.session_state:
    idx = random.randint(0, len(sounds) - 1)
    st.session_state.index = idx
    st.session_state.answer_name = names[idx]
    st.session_state.search = ""
    st.session_state.gave_up = False

idx = st.session_state.index
answer_name = st.session_state.answer_name
answer_path = sounds[idx]

st.title("Surviv.io Sound Effect")

if st.button("Play sound"):
    st.audio(answer_path)

if st.button("Give Up"):
    st.session_state.gave_up = True

if st.session_state.gave_up:
    st.info(answer_name)

search = st.text_input("Search & choose:", st.session_state.search)
st.session_state.search = search

if search == "":
    filtered_indices = list(range(len(names)))
else:
    filtered_indices = [
        i for i, n in enumerate(names) if search.lower() in n.lower()
    ]

if filtered_indices:
    filtered_names = [names[i] for i in filtered_indices]
    guess = st.selectbox("", filtered_names)
else:
    filtered_names = []
    guess = None
    st.write("No options to select")

if st.button("Submit Guess"):
    if guess is not None and guess == answer_name:
        st.success("Correct!")
        st.balloons()
        if st.button("Play Again"):
            st.session_state.clear()
            st.rerun()
    else:
        st.error("Incorrect")
