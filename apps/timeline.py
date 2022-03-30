import streamlit as st
import pandas as pd
import plotly.express as px

def app():    
    st.title("Timeline Visualisation")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month_all.csv', index_col = 0)
    df['day'] = '01'
    df['date']=pd.to_datetime(df[['year','month', 'day']])
    clist1 = ['stringency_index', 'new_cases', 'log_facebook_movement', 'log_NO2']
    clist = df['country'].unique()
    y = st.sidebar.selectbox("Select y:",clist1, 2)
    # color = st.sidebar.selectbox("Select 2nd y:",clist)
    color = st.sidebar.selectbox("Select color:",clist1, 0)
    df_group = df.groupby(['date', 'country']).mean().reset_index()
    # df_group_melt = pd.melt(df_group, id_vars=['date', 'country'], value_vars= ['stringency_index', 'new_cases', 'log_facebook_movement', 'log_NO2'], var_name='var', value_name='value')
    fig = px.bar(df_group, x="date", y= y, facet_col = 'country', color = color, facet_col_wrap = 2, height = 800)
    st.write('The variations in ' + y + ' with time, with color represents the ' + color) 
    st.plotly_chart(fig, use_container_width=True)

    agree = st.checkbox('I do not want to set size as a variable')
    if agree:
        fig1 = px.scatter(df, x='date', y = y, color = color, facet_col='country', facet_col_wrap=2, height = 800 )
    else: 
        size = st.selectbox("Select size:",clist1, 3)
        fig1 = px.scatter(df, x='date', y = y, color = color, size = size, facet_col='country', facet_col_wrap=2, height = 800 )

    # st.subheader("Plot of " + y1 + ' and ' + y2 + ' with time, color represents country')
    # fig = px.scatter(df_melt, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig1, use_container_width=True)
    country = st.selectbox("You can select a country to take a close look:",clist)
    if agree:
        fig2 = px.scatter(df[df['country']== country], x='date', y = y , color = color)
    else: 
        fig2 = px.scatter(df[df['country']== country], x='date', y = y , color = color, size = size)
   
    st.plotly_chart(fig2, use_container_width=True)
# fig.show()