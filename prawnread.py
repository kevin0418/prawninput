import streamlit as st

with open("inputdata.txt", 'r') as file:
       content = file.read()
       st.text(content)


with open("inputdata.csv", 'r') as file:
       content = file.read()
       st.text(content)