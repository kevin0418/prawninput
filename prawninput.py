
import streamlit as st
import pandas as pd

# 입력 폼 생성
#st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
#st.write ("Contact Agent,  more information ")

st.subheader("_Contact Agent_ :blue[more information] ")
with st.form("my_form"):
    name = st.text_input(":blue[Full Name]")
    phone = st.text_input("Phone Number")
    email= st.text_input("Your Email ")
    #message= st.text_input("Additional Message ", height=150)
    message= st.text_area("Additional Message ", height=100)
       
 #   age = st.number_input("나이", min_value=0, max_value=120)
    submit = st.form_submit_button("submit")

 # 제출 버튼이 클릭되면 TXT 파일에 저장
   
if submit:
    with open("inputdata.txt", "a") as file:
        file.write(f"key : prawn Farm, name: {name}, phone : {phone}, email : {email}, message : {message},  \n")
    st.success("success  updated!")

# **데이터 저장**: CSV 파일에 저장합니다
  
import csv

if submit:
       with open("inputdata.csv", "a", newline="") as file:
           writer = csv.writer(file)
           writer.writerow(["Frawn Farm ", name, phone, email, message])
       #st.success("데이터가 저장되었습니다.")

