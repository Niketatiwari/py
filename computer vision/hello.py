# streamlit run aap1/hello.py
from PIL import Image
import streamlit as st

st.title("Sample App")

image = st.camera_input("Take a picture")
if image:
    im = Image.open(image)

    color = st.color_picker("Pick a color","")
    im2 = Image.new("RGB", im.)