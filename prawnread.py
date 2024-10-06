import streamlit as st

import os
file_path =  "inputdata.txt"  # Streamlit 서버가 실행되는 디렉토리에 생성됩니다.

with open("inputdata.txt", 'r') as file:
       content = file.read()
       st.text(content)


with open("inputdata.csv", 'r') as file:
       content = file.read()
       st.text(content)