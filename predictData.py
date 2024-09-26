import pickle
import pandas as pd

def get_prediction(file_name,Car_Type,Departing_time,source,destination):

    #Car_Type,Departing_time,Price,
    #Source_Kempegowda International Airport Bengaluru,Source_Majestic,Source_Mysore Bank Colony,Source_Nikoo Homes 2,Source_Sarjapura
    #Destination_Kempegowda International Airport Bengaluru,Destination_Majestic,Destination_Mysore Bank Colony,Destination_Nikoo Homes 2,
    #Destination_Sarjapura 
    details=pd.DataFrame()
    if Car_Type=='Uber Go':
        details["Car_Type"]=[0]
    else:
        details["Car_Type"]=[1]

    time=[]
    time.append(Departing_time.replace(":","."))
    details['Departing_time']=time

    details["Source_Kempegowda International Airport Bengaluru"]=[0]
    details["Source_Majestic"]=[0]
    details["Source_Mysore Bank Colony"]=[0]
    details["Source_Nikoo Homes 2"]=[0]
    details["Source_Sarjapura"]=[0]

    details["Destination_Kempegowda International Airport Bengaluru"]=[0]
    details["Destination_Majestic"]=[0]
    details["Destination_Mysore Bank Colony"]=[0]
    details["Destination_Nikoo Homes 2"]=[0]
    details["Destination_Sarjapura"]=[0]

    
    if source=='Kempegowda International Airport Bengaluru':
        details["Source_Kempegowda International Airport Bengaluru"]=[1]
    elif source=='Majestic':
        details["Source_Majestic"]=[1]
    elif source=='Mysore Bank Colony':
        details["Source_Mysore Bank Colony"]=[1]
    elif source=='Nikoo Homes 2':
        details["Source_Nikoo Homes 2"]=[1]
    else:
        details["Source_Sarjapura"]=[1]

    if destination=='Kempegowda International Airport Bengaluru':
        details["Destination_Kempegowda International Airport Bengaluru"]=[1]
    elif destination == "Majestic":
        details["Destination_Majestic"]=[1]
    elif destination=='Mysore Bank Colony':
        details["Destination_Mysore Bank Colony"]=[1]
    elif destination=='Nikoo Homes 2':
        details["Destination_Nikoo Homes 2"]=[1]
    else:
        details["Destination_Sarjapura"]=[1]

    
    with open(f'{file_name}.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    
    y_pred = loaded_model.predict(details)
    print(y_pred)
    return y_pred

