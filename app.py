import streamlit as st

# Custom imports 
from multipage import MultiPage
from apps import home, scatter, map

st.set_page_config(layout="wide")

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Visualisation of NO2 and its influential factors in South-East Asia (2020-2021)")

# Add all your applications (pages) here
app.add_page("home", home.app)
app.add_page("scatter", scatter.app)
app.add_page("map", map.app)
# app.add_page("Machine Learning", machine_learning.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()