import streamlit as st
import pandas as pd
import plotly.express as px

def app():    
    st.title("Timeline Visualisation")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month_all.csv', index_col = 0)
    clist = ['stringency_index', 'new_cases', 'NO2', 'facebook_movement', 'log_NO2', 'log_facebook_movement']
    y1 = st.sidebar.radio("Select 1st variable:",clist)
    y2 = st.sidebar.radio("Select 2nd variable:",clist)
    df_melt = pd.melt(df, id_vars=['year','month','country'], value_vars=[y1,y2], var_name='variable', value_name='value')
    # st.subheader("Plot of " + y + ' vs. ' + x + ', color represents ' + color)
    fig = px.scatter(df_melt, x='month', y='value', color='variable', facet_col='year')
    # fig = px.scatter(df_melt, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig, use_container_width=True)
    # [merge_by_month_location['country']=='Malaysia']