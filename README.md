# Uber-Price-and-Waiting-time-Prediction

Skills - MySQL,selenium,Python,SKlearn,Streamlit,ML.

createtable.py -> creates new database and the required columns in the table (MySQL).

Get_Data.py -> in this file
                #replace with ur driver path in the below line.
                service = Service( r'C:\chromedriver-win64\chromedriver.exe') 

                created new function to convert time into 24 format -> convert_to_24hr(input time)

                this method is the main method to get the data from the website
                getdata(path,source_details,destination_details,count)
                path-> it's a link with source & destination 
                source_details and destination_details -> pass the source details (it is taken from the list in the code)
                count -> if we are running, then first it will ask for login details so only for first run it requireds some time post that only 10 seconds of sleep is required.

                we call this getdata method to capture all the required details from the website. Once all the details are captured store it in MySql and commit and sleep for 15 minutes.
                Post 15 minutes wakeup and start to capture data again it's in a loop.

testModel.py -> with all the data stored in MySql. Read the data from Sql and Since ML can not understand any other data type apart from number.
                Convert all the staring into number (int/float) onehotcoding

                now split the data into train & test by taking randomstate =42 to keep the constant results.

                train the model and calculate the score.

                pick the proper model.

                once you select the model, we will be saving the model offline. (it will be stored in the folder level).
                
                



