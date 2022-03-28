import streamlit as st
import pandas as pd
import plotly.express as px

def app():    
    st.title("Scatter Plot Visualisation")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    clist = df.columns.values.tolist()
    x = st.sidebar.selectbox("Select x-axis variable:",clist)
    y = st.sidebar.selectbox("Select y-axis variable:",clist)
    color = st.sidebar.selectbox("Select color:",clist)  
    st.subheader("Plot of " + y + ' vs. ' + x + ', color represents ' + color)
    with st.expander("change chart type for marginal x"):
        marginal_x = st.radio('', ('histogram','rug', 'box', 'violin' ))
    with st.expander("change chart type for marginal y"):        
        marginal_y = st.radio(':', ('histogram','rug', 'box', 'violin' ))

    fig = px.scatter(df, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig, use_container_width=True)

    
