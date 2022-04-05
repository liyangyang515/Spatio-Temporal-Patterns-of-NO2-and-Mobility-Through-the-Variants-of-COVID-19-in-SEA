import streamlit as st
import plotly.express as px
import pandas as pd


def app():
    st.title("Pattern Visualisation")
    #this is a public token
    mapbox_token = 'pk.eyJ1IjoibGl5YW5neWFuZzUxNSIsImEiOiJjbDBuNmM3MjEwdGZjM2t0NHRqbmJidXFjIn0.8O9DnGkHPecl4jjk1ZqQUQ'
    px.set_mapbox_access_token(mapbox_token)
    # st.header("")
    # df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/Emerging_hot_spots/correlation.csv')
    # st.title("")
    df2 = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/Emerging_hot_spots/data.csv')
    
    fig1 = px.scatter_mapbox(df2, lat="lat", lon="lon", color = 'pattern', hover_data = ['country'], color_continuous_scale=px.colors.cyclical.IceFire, zoom = 2)
    st.plotly_chart(fig1, use_container_width=True)

    clist = df2['pattern'].unique().tolist()
    pattern = st.selectbox("Select interested pattern:",clist)
    df_filter = df2[(df2['pattern']== pattern)]   
    st.subheader("Plot of " + 'NO2' + ' with time for the selected ' + pattern + 'pattern, color represents country')
    with st.expander("change chart type for marginal y"):        
        marginal_y = st.radio(':', ('histogram','rug', 'box', 'violin' ))
    fig2 = px.scatter(df_filter, y="NO2", x="week_id", marginal_y  = marginal_y, color = 'country', hover_data = ['country'], color_continuous_scale=px.colors.cyclical.IceFire)
    st.plotly_chart(fig2, use_container_width=True)