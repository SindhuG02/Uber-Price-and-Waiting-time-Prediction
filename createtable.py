import mysql.connector
#pip install mysql-connector-python if any error related to password
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678'
)
cursor=con.cursor()

query="create database if not exists Uber"
cursor.execute(query)

query='use Uber'
cursor.execute(query)

query='''create table uber_details(
                
                source varchar(50),
                destination varchar(50),
                car_type varchar(10),
                capacity varchar(3),
                currenttime varchar(10),
                drop_off_time varchar(10),
                waiting_time varchar(10),
                Price varchar(10))'''

cursor.execute(query)