import streamlit as st
st.image("happy-or-sad.PNG", caption="Which one?")
st.set_page_config(page_title="Happy or Sad?", layout="centered")

st.title("Happy or Sad? ")

# Happy button
if st.button("Happy"):
    st.image("download.jpg", caption="သူနဲ့အတူတူဆောက်ခဲ့တဲ့လေထဲကအိမ်လေးရော?")
    st.audio("Wink - Ya Par Tal (Raw).mp3", loop=True)

# Sad button
if st.button("Sad"):
    st.video("IMG_2744.MP4")
