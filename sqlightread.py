import streamlit as st
import sqlite3
import pandas as pd

# 데이터베이스 연결 (없으면 생성됨)
conn = sqlite3.connect('kevin.db')

# 커서 생성
c = conn.cursor()

#  **데이터 읽기:**
#c.execute('SELECT * FROM buyer')
#rows = c.fetchall()
#for row in rows:
#    print(row)


# SQL 쿼리 실행
query = "SELECT * FROM buyer"
df = pd.read_sql_query(query, conn)

# 데이터프레임을 Streamlit으로 표시
st.title('Customer Request Data')
st.write(df)

# 연결 종료
conn.close()

