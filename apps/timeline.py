import streamlit as st
import pandas as pd
import plotly.express as px

def app():    
    st.title("Timeline Visualisation")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month_all.csv', index_col = 0)
    clist1 = ['stringency_index', 'new_cases', 'log_facebook_movement', 'log_NO2']
    clist = df['country'].unique()
    y = st.sidebar.selectbox("Select y:",clist1)
    year = st.sidebar.radio("Select year:",(2020,2021))
    # color = st.sidebar.selectbox("Select 2nd y:",clist)
    size = st.sidebar.selectbox("Select size:",clist1)
    color = st.sidebar.selectbox("Select color:",clist1)
    country = st.sidebar.selectbox("Select country:",clist)

    # df_melt = pd.melt(df, id_vars=['year','month','country'], value_vars=[y1,y2], var_name='variable', value_name='value')
    # st.subheader("Plot of " + y1 + ' and ' + y2 + ' with time, color represents country')
    fig1 = px.scatter(df[df['year']==year], x='month', y = y, color = color, size = size, facet_col='country', facet_col_wrap=4 )
    # fig = px.scatter(df_melt, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig1, use_container_width=True)
    fig2 = px.scatter(df[df['country']== country], x='month', y = y , color = color, size = size, facet_col='year')
    st.plotly_chart(fig2, use_container_width=True)
# fig.show()