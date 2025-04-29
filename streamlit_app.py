# Save this as streamlit_app.py

import streamlit as st

st.title("Hello Streamlit!")
st.write("This is my first web app, converted from Tkinter!")

if st.button('Click me!'):
    st.success('Button clicked!')
