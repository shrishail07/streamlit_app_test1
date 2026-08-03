import streamlit as st

st.title("My first streamlit app")

name=st.text_input("Please enter your good name")

if st.button("Print")
  st.write(f"hello,{name}")
