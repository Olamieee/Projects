import streamlit as st
import joblib


model = joblib.load("emotion_detection")
st.title("Emotion Detection using Text")
st.markdown("Enter text describing the way how you feel and we will detect your emotion")

user_input = st.text_area("Describe how you feel.")

if st.button("Detect Emotion"):
    if user_input:
        emotion = model.predict([user_input])

        if emotion == 0:
            st.write("Anger")
        elif emotion == 1:
            st.write("Joy")
        else:
            st.write("Fear")
    else:
        st.warning("Please enter text to dectect emotion")

st.sidebar.title("Customize Style")
bg_color = st.sidebar.color_picker("Background Color", "#ffffff")

text_color = st.sidebar.color_picker("text color","#000000")

st.markdown(
    f'<style>body{{background-color:{bg_color}; color: {text_color}}}</style>',
    unsafe_allow_html=True)