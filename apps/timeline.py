import streamlit as st
import pandas as pd
import plotly.express as px

def app():    
    st.title("Timeline Visualisation")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month_all.csv', index_col = 0)
    clist1 = ['stringency_index', 'new_cases', 'facebook_movement', 'NO2', 'log_facebook_movement', 'log_NO2']
    # clist = df['country'].unique()
    y = st.sidebar.selectbox("Select y:",clist1, 4)
    # color = st.sidebar.selectbox("Select 2nd y:",clist)
    df_group = df.groupby(['date', 'country']).mean().reset_index()
    # df_group_melt = pd.melt(df_group, id_vars=['date', 'country'], value_vars= ['stringency_index', 'new_cases', 'log_facebook_movement', 'log_NO2'], var_name='var', value_name='value')
    fig = px.line(df_group[df_group['date']>'2021-04-02'], x="date", y= y, color = 'country')
    st.write('The variations in ' + y + ' with time') 
    st.plotly_chart(fig, use_container_width=True)
    color = st.selectbox("Select color:",clist1, 0)
    size = st.selectbox("Select size:",clist1, 5)
    fig1 = px.scatter(df[df['date']>'2021-04-02'], x='date', y = y, color = color, size = size, facet_col='country', facet_col_wrap=2, height = 800 )

    # st.subheader("Plot of " + y1 + ' and ' + y2 + ' with time, color represents country')
    # fig = px.scatter(df_melt, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig1, use_container_width=True)
    country = st.radio("You can select a country to take a full look:", ['Indonesia', 'Singapore'])
    
    fig2 = px.scatter(df[df['country']== country], x='date', y = y , color = color, hover_data = ['lon', 'lat'], size = size)
   
    st.plotly_chart(fig2, use_container_width=True)
# fig.show()