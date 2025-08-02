import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='anurag12124',database='travel_booking')
c1=conn.cursor()

c1.execute('create table customer_bookings(Phone_number bigint(13) ,FOREIGN KEY(Phone_number) REFERENCES accounts(Phone_number),Your_location varchar(30),Your_destination varchar(30),time varchar(30),Driver varchar(60),Urgency  varchar(30),date_booked varchar(90));')
conn.commit()
print("table  customer_bookings created successfully")


    
