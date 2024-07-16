import streamlit as st
from ai import *

st.title("Image Generator")

with st.form('My form'):
  msg = st.text_input("What would you like to generate?")
  submitted = st.form_submit_button("Submit")
  if submitted:
    image_link = generate_story(msg)
    st.image(image_link)


