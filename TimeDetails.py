import streamlit as st
import time
import getPic,predictData
from datetime import datetime
import pandas as pd

def convert_to_24hr(time_str):
    
    time_obj = datetime.strptime(time_str, "%I:%M %p")
    # Format the datetime object to 24-hour format
    return time_obj.strftime("%H:%M")

def app():
    
    st.header("Get a ride")
    Source=["Kempegowda International Airport Bengaluru","Majestic","Nikoo Homes 2","Mysore Bank Colony","Sarjapur Road"]
    Destination=["Kempegowda International Airport Bengaluru","Majestic","Nikoo Homes 2","Mysore Bank Colony","Sarjapur Road"]
    StartTime=['Now','12:00 AM','01:00 AM','02:00 AM','03:00 AM','04:00 AM','05:00 AM','06:00 AM','07:00 AM','08:00 AM','09:00 AM','10:00 AM','11:00 AM','12:00 PM','01:00 PM','02:00 PM','03:00 PM','04:00 PM','05:00 PM','06:00 PM','07:00 PM','08:00 PM','09:00 PM','10:00 PM','11:00 PM']
    with st.form("From-To"):
		
        From=st.selectbox("Pickup Location",Source)
        To=st.selectbox("Drop Location",Destination)
        start_time=st.selectbox("Pickup Time",StartTime)
		
        
        if start_time == 'Now':
            start_time = time.strftime("%H:%M")
        else:
            start_time=  convert_to_24hr(start_time)

        Submitted = st.form_submit_button("Search")

    if Submitted:
        if From == To:
            st.error("Pickup and Drop should not be same")
            st.stop()
        
        predicted_UberGo=predictData.get_prediction('Page2_model','Uber Go',start_time,From,To)
        st.header("Choose a ride")
        getPic.create_pic(From,To)
        st.subheader("Uber Go")
        col1, col2 = st.columns([1,2])  
        # Display an image in the first column
        with col1:
            st.image("UberGo.png", width=140)
        
        # Display text in the second column
        with col2:
            if int(predicted_UberGo[0])==1:
                st.subheader(f"Waiting Time :{predicted_UberGo[0]} min Away")
            else:
                st.subheader(f"Waiting Time :{predicted_UberGo[0]} mins Away")
            
        predicted_GoSedan=predictData.get_prediction('Page2_model','Go Sedan',start_time,From,To)
        st.subheader("Go Sedan")
        col1, col2 = st.columns([1,2])  

        # Display an image in the first column
        with col1:
            st.image("Uber_X.png", width=140)
        
        # Display text in the second column
        with col2:
            if int(predicted_GoSedan[0]) == 1:
                st.subheader(f"Waiting Time :{predicted_GoSedan[0]} min Away")
            else:
                st.subheader(f"Waiting Time :{predicted_GoSedan[0]} mins Away")
        
        
        st.header("Suggestion")
        
        start_digit=int(start_time[:2])
        
        if (start_digit)<9:
            
            start_time1=start_digit+1
            start_time1=str(start_time1)
            start_time1="0"+str(start_time1)+start_time[-3:]
            
            start_time2=int(start_time1[:2])
            start_time2=str(start_time2+1)
            start_time2="0"+str(start_time2)+start_time[-3:]
            
        else:
            
            if start_digit!=23:

                start_time1=start_digit+ 1
                start_time1=str(start_time1)+start_time[-3:]
                
                if int(start_time1[:2])!=23:
                    start_time2=int(start_time1[:2])+1
                    start_time2=str(start_time2)+start_time1[-3:]
                    
                else:
                    start_time2="00:"+start_time1[-2:]
        
        predicted_UberGo2=predictData.get_prediction('Page2_model','Uber Go',start_time1,From,To)
        predicted_UberGo3=predictData.get_prediction('Page2_model','Uber Go',start_time2,From,To)
        predicted_GoSedan2=predictData.get_prediction('Page2_model','Go Sedan',start_time1,From,To)
        predicted_GoSedan3=predictData.get_prediction('Page2_model','Go Sedan',start_time2,From,To)

        differenceUberGo=(float(predicted_UberGo[0])-float(predicted_UberGo[0]))
        differenceUberGo1=(float(predicted_UberGo2[0])-float(predicted_UberGo[0]))
        if differenceUberGo1==0:
            UberGOsign1="Same"
        elif differenceUberGo1>0:
            UberGOsign1="↑"
        else:
            UberGOsign1='↓'
        
        differenceUberGo2=(float(predicted_UberGo3[0])-float(predicted_UberGo[0]))
        if differenceUberGo2==0:
            UberGOsign2="Same"
        elif differenceUberGo2>0:
            UberGOsign2="↑"
        else:
            UberGOsign2='↓'

        differenceGoSedan=(float(predicted_GoSedan[0])-float(predicted_GoSedan[0]))
        differenceGoSedan1=(float(predicted_GoSedan2[0])-float(predicted_GoSedan[0]))
        if differenceGoSedan1==0:
            GoSedansign1="Same"
        elif differenceGoSedan1>0:
            GoSedansign1="↑"
        else:
            GoSedansign1='↓'
        differenceGoSedan2=(float(predicted_GoSedan3[0])-float(predicted_GoSedan[0]))
        if differenceGoSedan2==0:
            GoSedansign2="Same"
        elif differenceGoSedan2>0:
            GoSedansign2="↑"
        else:
            GoSedansign2='↓'
        details=[[start_time,"Uber Go",predicted_UberGo[0],differenceUberGo,''],
                 [start_time1,"Uber Go",predicted_UberGo2[0],differenceUberGo1,UberGOsign1],
                 [start_time2,"Uber Go",predicted_UberGo3[0],differenceUberGo2,UberGOsign2],
                 [start_time,"Go Sedan",predicted_GoSedan[0],differenceGoSedan,''],
                 [start_time1,"Go Sedan",predicted_GoSedan2[0],differenceGoSedan1,GoSedansign1],
                 [start_time2,"Go Sedan",predicted_GoSedan3[0],differenceGoSedan2,GoSedansign2]
                 ]
        df=pd.DataFrame(details,columns=["Time","Car_Type","Waiting Time","Waiting Time_Difference_of","Increased/Decreased"])  
        st.dataframe(df)