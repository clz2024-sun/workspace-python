#0.import
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="phonebook",
        password="phonebook",
        database="phonebook_db"
    )

    #2.커서생성
    cursor = conn.cursor()

    #3.SQL문준비/바인딩/실행
    #--SQL문
    query = """
        insert into person             
        values(null, %s, %s, %s)
    """

    #--바인딩(튜플)
    data = ("유재석", "010-1111-1111", "02-1111-1111")

    #--실행
    cursor.execute(query, data)     #임시반영
    conn.commit()                   #최종반영    


    #4.결과처리
    print(cursor.rowcount)

except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
    #5.자원정리
    conn.close()
    cursor.close()



