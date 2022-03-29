import streamlit as st

# Custom imports 
from multipage import MultiPage
from apps import home, timeline, map, scatter, map3D, MLP, pattern

st.set_page_config(layout="wide")

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.title("Visualisation of NO2 and its influential factors in South-East Asia (2020-2021)")

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Timeline", timeline.app)
app.add_page("Map", map.app)
app.add_page("Scatter", scatter.app)
app.add_page("3Dmap", map3D.app)
app.add_page("Train a model", MLP.app)
app.add_page("Pattern", pattern.app)

# The main app
app.run()