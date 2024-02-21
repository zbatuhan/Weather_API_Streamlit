import streamlit as st
import plotly.express as px
from main_backend import getData

#Setting title for streamlit GUI
st.title("Weather Forecast")

#Setting another input fields
Location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=10,
                 help="You can arrange the number of forecasted days")

option = st.selectbox("Select data",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {Location}")

#------- GRAPH PART -------

if Location:
    #Get the temperature and sky data
    
    try:
        
        filtered_data = getData(Location, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Line chart, Bar chart etc.
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            #matching the data and images
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_data = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[data] for data in sky_data]
            #Create image part
            st.image(image_paths, width=115)
            
    except KeyError:
        st.write("That location does not exist.")