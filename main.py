#python -m streamlit run main.py -> to run file
#https://icons.getbootstrap.com/ -> Icon details
import streamlit as st
from streamlit_option_menu import option_menu
import visualization,UBER_PAGE,TimeDetails

st.set_page_config(page_title="Plan your Uber journey")

class MultiApp:

    def __init__(self):
        self.apps=[]
    
    def add_app(self,title,function):
        self.apps.append(
            {
                "tilte":title,
                "function":function
            }
        )
    
    def run():

        with st.sidebar:
            app=option_menu(
                menu_title="Uber Application",
                options=["Home","Time Details","visualization"],
                menu_icon="car-front-fill",
                icons=['house-fill','hourglass-split','globe-central-south-asia'], #pin-map-fill/geo-alt-fill/globe-central-south-asia
                default_index=0
                
            )

        if app=="Home":
            UBER_PAGE.app()
        elif app=="Time Details":
            TimeDetails.app()
        elif app=="visualization":
            visualization.app()
        

    run()