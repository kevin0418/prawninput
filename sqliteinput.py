import streamlit as st
import pandas as pd

import os
file_path =  "inputdata.txt"  # Streamlit 서버가 실행되는 디렉토리에 생성됩니다.

# 입력 폼 생성
#st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
#st.write ("Contact Agent,  more information ")

st.subheader("_Contact Agent_ :blue[more information] ")
with st.form("my_form"):
    iname = st.text_input(":blue[Full Name]")
    iphone = st.text_input("Phone Number")
    iemail= st.text_input("Your Email ")
    #message= st.text_input("Additional Message ", height=150)
    imessage= st.text_area("Additional Message ", height=100)
       
 #   age = st.number_input("나이", min_value=0, max_value=120)
    submit = st.form_submit_button("submit")

 
 
# Sqlite3 연결

import sqlite3
import datetime
now = datetime.datetime.now()

# 데이터베이스 연결 (없으면 생성됨)
conn = sqlite3.connect('kevin.db')

# 커서 생성
c = conn.cursor()


# 데이터 삽입
userList = (
    ('prawn',iname,iphone,iemail,imessage,now,'call area'),   
)

# **데이터 저장**
if submit:
   c.execute("INSERT INTO buyer (location, name, phone,  email, message, inputdate, callarea) VALUES(?,?,?,?,?,?,?)",('prawn',iname,iphone,iemail,imessage,now,'call area'))

   # 변경사항 저장
   conn.commit()
    
   # 연결 종료
   conn.close()
   st.success("success  inserted!")

