import streamlit as st
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

def app():
    st.header("Uber Go")
    
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678'
        )
    cursor=con.cursor()
        
    cursor.execute('use Uber')

    query="SELECT * FROM UBER.UBER_DETAILS WHERE Car_Type='Uber Go'"

    cursor.execute(query)
    details=[]
    for data in cursor:
        details.append(data)
    #print(details)
    df=pd.DataFrame(details,columns=["Source","Destination","Car_Type","Capacity","Departing_time","Reaching_time","Waiting_time","Price"])  
    
    st.subheader("Bar Graph - Departing time vs Waiting Time")
    st.bar_chart(df,x="Departing_time",y="Waiting_time")

    st.subheader("Line Graph - Departing time vs Price")
    st.line_chart(df,x="Departing_time",y="Price")

    st.header("Go Sedan")
    query="SELECT * FROM UBER.UBER_DETAILS WHERE Car_Type='Go Sedan'"

    cursor.execute(query)
    details=[]
    for data in cursor:
        details.append(data)
    #print(details)
    df=pd.DataFrame(details,columns=["Source","Destination","Car_Type","Capacity","Departing_time","Reaching_time","Waiting_time","Price"])  
    
    st.subheader("Bar Graph - Departing time vs Waiting Time")
    st.bar_chart(df,x="Departing_time",y="Waiting_time")

    st.subheader("Line Graph - Departing time vs Price")
    st.line_chart(df,x="Departing_time",y="Price")

    