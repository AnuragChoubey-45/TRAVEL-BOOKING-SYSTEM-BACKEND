import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='anurag12124',database='travel_booking')
c1=conn.cursor()
c1.execute('create table accounts(Phone_number bigint(13) primary key,name varchar(30),password  bigint(10));')
conn.commit()
print("Table  accounts created successfully")
