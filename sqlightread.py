import sqlite3

# 데이터베이스 연결 (없으면 생성됨)
conn = sqlite3.connect('kevin.db')

# 커서 생성
c = conn.cursor()

#  **데이터 읽기:**
c.execute('SELECT * FROM buyer')
rows = c.fetchall()

for row in rows:
    print(row)

# 연결 종료
conn.close()

