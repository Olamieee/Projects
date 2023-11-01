import streamlit as st
import joblib

st.title("News Detection")

model = joblib.load('model.joblib')
user_input = st.text_area(label='input news text here')

if st.button("Get Status"):
    if user_input:
        output = model.predict([user_input])

        if output == 0:
            st.write("This is a Fake news")
        else:
            st.write("This is a Real news")
    else:
        st.warning('Please enter news text to detect its credibility')

