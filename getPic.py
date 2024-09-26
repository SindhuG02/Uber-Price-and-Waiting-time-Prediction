from PIL import Image
import streamlit as st

def create_pic(From,To):
    if From=="Kempegowda International Airport Bengaluru" :
        if To=="Majestic":
            
            img = Image.open("airport_to_majestic.png")
            st.image(img, width=700)

        elif To=="Nikoo Homes 2":
            img = Image.open("airport_to_Nikoo.png")
            st.image(img, width=700)

        elif To=="Mysore Bank Colony":
            img = Image.open("airport_to_bankcolony.png")
            st.image(img, width=700)

        elif To=="Sarjapur Road":
            img = Image.open("airport_to_sarjapur.png")
            st.image(img, width=700)

    elif From=="Majestic":

        if To=="Kempegowda International Airport Bengaluru":
            
            img = Image.open("Majestic_To_airport.png")
            st.image(img, width=700)

        elif To=="Nikoo Homes 2":
            img = Image.open("majestic_to_nikoo.png")
            st.image(img, width=700)

        elif To=="Mysore Bank Colony":
            img = Image.open("Majestic_To_bankcolony.png")
            st.image(img, width=700)

        elif To=="Sarjapur Road":
            img = Image.open("majestic_to_sarjapur.png")
            st.image(img, width=700)

    elif From=="Nikoo Homes 2":

        if To=="Kempegowda International Airport Bengaluru":
            
            img = Image.open("Nikoo_To_airport.png")
            st.image(img, width=700)

        elif To=="Majestic":
            img = Image.open("nikoo_to_majestic.png")
            st.image(img, width=700)

        elif To=="Mysore Bank Colony":
            img = Image.open("Nikoo_To_bankcolony.png")
            st.image(img, width=700)

        elif To=="Sarjapur Road":
            img = Image.open("nikoo_to_sarjapur.png")
            st.image(img, width=700)

    elif From=="Mysore Bank Colony":

        if To=="Kempegowda International Airport Bengaluru":
            
            img = Image.open("BankColony_To_airport.png")
            st.image(img, width=700)

        elif To=="Majestic":
            img = Image.open("bankColony_to_majestic.png")
            st.image(img, width=700)

        elif To=="Nikoo Homes 2":
            img = Image.open("bankColony_to_nikoo.png")
            st.image(img, width=700)

        elif To=="Sarjapur Road":
            img = Image.open("bankcolony_to_sarjapur.png")
            st.image(img, width=700)
    
    elif From=="Sarjapur Road":

        if To=="Kempegowda International Airport Bengaluru":
            
            img = Image.open("sarjapur_To_airport.png")
            st.image(img, width=700)

        elif To=="Majestic":
            img = Image.open("sarjapur_to_majestic.png")
            st.image(img, width=700)

        elif To=="Nikoo Homes 2":
            img = Image.open("sarjapur_to_nikoo.png")
            st.image(img, width=700)

        elif To=="Mysore Bank Colony":
            img = Image.open("sarjapur_to_bankcolony.png")
            st.image(img, width=700)
    