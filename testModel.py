import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,f1_score,recall_score
import pickle


def get_data():
    con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678'
        )
    cursor=con.cursor()
        
    cursor.execute('use Uber')

    query="SELECT * FROM UBER.UBER_DETAILS"

    cursor.execute(query)
    details=[]
    for data in cursor:
        details.append(data)
    #print(details)
    df=pd.DataFrame(details,columns=["Source","Destination","Car_Type","Capacity","Departing_time","Reaching_time","Waiting_time","Price"])  
    
    df['Car_Type'] = df["Car_Type"].replace("Uber Go","0")
    df['Car_Type'] = df["Car_Type"].replace("Go Sedan","1")
    df=pd.get_dummies(df, columns = ['Source','Destination'],dtype=int)

    X_starttime=df['Departing_time']
    starttime=[]
    for i in X_starttime:
        
        i=i.replace(":",".")
        starttime.append(i)

    X_Endtime=df['Reaching_time']
    endtime=[]
    for i in X_Endtime:
        
        i=i.replace(":",".")
        endtime.append(i)
    df['Departing_time']=starttime
    df['Reaching_time']=endtime

    return df


def train_model(X,Y,file_name):
    x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    
    models=[GradientBoostingClassifier(),DecisionTreeClassifier(),RandomForestClassifier()]
    for model in models:
        print(model)

        model.fit(x_train,y_train)
        
        train_predict=model.predict(x_train)

        model.fit(x_test,y_test)
        test_predict=model.predict(x_test)

        print("************* Train ************")
        
        print("Train accuracy_score",accuracy_score(y_train,train_predict))
        print("Train precision_score",precision_score(y_train,train_predict,average='micro'))
        print("Train Recall_Score",recall_score(y_train,train_predict,average='micro'))
        print("Train f1_score",f1_score(y_train,train_predict,average='micro'))
        
        print("************* Test ************")
        
        print("Test accuracy_score",accuracy_score(y_test,test_predict))
        print("Test precision_score",precision_score(y_test,test_predict,average='micro'))
        print("Test Recall_Score",recall_score(y_test,test_predict,average='micro'))
        print("Test f1_score",f1_score(y_test,test_predict,average='micro'))
        
        print("******************************")
    
    print(" If GradientBoostingClassifier -> 0")
    print(" If DecisionTreeClassifier -> 1")
    print(" If RandomForestClassifier -> 2")
    model_Selection=input("Which model is the best")
    
    if model_Selection != 0 and model_Selection != 1 and model_Selection != 2:
        model_Selection=1
    
    model=models[model_Selection]
    
    model.fit(X,Y)  
    train_predict=model.predict(X)
    
    with open(f'{file_name}.pkl', 'wb') as file:
        pickle.dump(model, file)

def page1_train_model():
    df=get_data()
    
    #Columns
    #Car_Type,Departing_time,Price,
    #Source_Kempegowda International Airport Bengaluru,Source_Majestic,Source_Mysore Bank Colony,Source_Nikoo Homes 2,Source_Sarjapura
    #Destination_Kempegowda International Airport Bengaluru,Destination_Majestic,Destination_Mysore Bank Colony,Destination_Nikoo Homes 2,
    #Destination_Sarjapura 
    X=df.drop(['Price','Reaching_time','Waiting_time','Capacity'],axis=1)
    Y=df["Price"]
    file_name="Page1_model"
    
    train_model(X,Y,file_name)

def page2_train_model():
    df=get_data()
    
    #Columns
    #Car_Type,Departing_time,Waiting_time
    #Source_Kempegowda International Airport Bengaluru,Source_Majestic,Source_Mysore Bank Colony,Source_Nikoo Homes 2,Source_Sarjapura
    #Destination_Kempegowda International Airport Bengaluru,Destination_Majestic,Destination_Mysore Bank Colony,Destination_Nikoo Homes 2,
    #Destination_Sarjapura 
    X=df.drop(['Price','Reaching_time','Waiting_time','Capacity'],axis=1)
    Y=df["Waiting_time"]
    file_name="Page2_model"
    train_model(X,Y,file_name)

value=input("Do you want to test Page1 model?")

if value=='Y' or value=="y":
    page1_train_model()
else:
    pass

value=input("Do you want to test Page2 model?")

if value=='Y' or value=="y":
    page2_train_model()
else:
    pass
