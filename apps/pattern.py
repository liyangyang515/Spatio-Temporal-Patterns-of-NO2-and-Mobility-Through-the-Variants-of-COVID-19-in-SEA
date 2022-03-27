import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title("Pattern Visualisation")
    #this is a public token
    mapbox_token = 'pk.eyJ1IjoibGl5YW5neWFuZzUxNSIsImEiOiJjbDBuNmM3MjEwdGZjM2t0NHRqbmJidXFjIn0.8O9DnGkHPecl4jjk1ZqQUQ'
    px.set_mapbox_access_token(mapbox_token)
    # st.header("")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/Emerging_hot_spots/correlation.csv')
    # st.title("")
    row1_col1, row1_col2 = st.columns([2, 1])
    width = 950
    height = 600

    with row1_col1:

        fig = px.scatter_mapbox(df, lat="lat", lon="lon", color = 'pearson', size = '100/p', color_continuous_scale=px.colors.cyclical.IceFire, size_max = maximum_size, zoom = 3, width=800, height=600)
        st.plotly_chart(fig, use_container_width=True)




#   clist = df.columns.values.tolist()
#   color = st.sidebar.selectbox("Select color:",clist)
#   month_s, month_e = st.sidebar.slider('range of month' , 1, 12, (1, 12))
#   df_filter = df[(df['month']>= month_s)&(df['month']<= month_e)]
#   # size_B = st.sidebar.radio("Do you want to set size as variable:",['Yes', 'No'])
#   agree = st.sidebar.checkbox('I also want to set size as a variable')
#   if agree:
#     size = st.sidebar.selectbox("Select size:",clist)
#     maximum_size = st.sidebar.slider('maximum size' , 1, 15)
#     st.header("Mapping color in " + color + ' and ' + ' size in ' + size)
#     fig = px.scatter_mapbox(df_filter, lat="lat", lon="lon", color = color, size = size, color_continuous_scale=px.colors.cyclical.IceFire, size_max = maximum_size, zoom = 3, width=800, height=600)
#   else:
#     fig = px.scatter_mapbox(df_filter, lat="lat", lon="lon", color = color, color_continuous_scale=px.colors.cyclical.IceFire, zoom = 3, width=800, height=600)
#     st.header("Mapping color in " + color)

#   st.plotly_chart(fig, use_container_width=True)

