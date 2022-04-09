import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Visualisation of NO2 and its influential factors in South-East Asia (2020-2021)")
    st.markdown(
        """
        This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io), written purely in Python. Here is the [storymap](https://storymaps.arcgis.com/stories/28655bd2a29e4d2481feeccd47bc6575) if you want to know more about our study.
        This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/issues) or 
        [pull requests](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/pulls) to the [GitHub repository](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA).
        """
    )

    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month_all.csv', index_col = 0)
    
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(df)
    st.info("You can download data, take a look at the parameters and some visualisation examples before clicking on the left sidebar menu to navigate to the different apps.")
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='monthly_merge.csv',
    )
    st.dataframe(df.head(50))
    with st.expander("See explanations of each parameter"):
        st.markdown("""
         **mobility**
         * facebook_movement: facebook mobility level
         * apple_driving: apple mobility with driving mode
         * apple_walking: apple mobility with walking mode
         **weather**
         * rainfall: hourly rainfall
         * surface-p: surface air pressure
         * 2m-temp: air temperature
         * dew-pt: dew point
         * wind speed: calculated from u-wind and v-wind vectors
         **haze**
         **spatial information**
         * lon: longitude
         * lat: latitude
         **temporal information**
         * day: day number from the start (Apr 1, 2020)
         **stringency_index: government policy restriction level (max 100); not in MLP model
         **case_number: number of newly confirmed cases; not in MLP model
         """)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/demo_scatter.gif")
        st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/demo_timeline.gif")

    with row1_col2:
        st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/demo_map3d.gif")
        st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/demo_map.gif")
    
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/demo_model.gif")

    st.header("Some Visualisaition Examples")
    st.markdown(
        """
        The following visualisaitions were created using this multi-page web app. 
    """
    )
    mapbox_token = 'pk.eyJ1IjoibGl5YW5neWFuZzUxNSIsImEiOiJjbDBuNmM3MjEwdGZjM2t0NHRqbmJidXFjIn0.8O9DnGkHPecl4jjk1ZqQUQ'
    px.set_mapbox_access_token(mapbox_token)
    st.subheader("1. Example using timeline app:")
    st.write("See how facebook mobility and NO2 (in color) change with time.")   
    fig0 = px.scatter(df[df['country']=='Indonesia'], x='date', y = 'log_facebook_movement', color = 'log_NO2', size = 'log_NO2')
    # fig = px.scatter(df_melt, x , y , color = color, marginal_x = marginal_x, marginal_y  = marginal_y, height = 600)
    st.plotly_chart(fig0, use_container_width=True)
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/facebook_SI_Timeline.png")
    st.subheader("2. Example using map app:")
    st.write("NO2 Mapping")
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/map_NO2.png")
    fig1 = px.scatter_mapbox(df, lat="lat", lon="lon", color = 'log_NO2', size = 'log_NO2', hover_data = ['country'], size_max= 3, color_continuous_scale=px.colors.cyclical.IceFire, zoom = 3, width=800, height=600)
    st.plotly_chart(fig1, use_container_width=True)
    st.write("Facebook Mobility Mapping")
    fig2 = px.scatter_mapbox(df, lat="lat", lon="lon", color = 'log_facebook_movement', size = 'log_facebook_movement', hover_data = ['country'], size_max = 4, color_continuous_scale=px.colors.cyclical.IceFire, zoom = 3, width=800, height=600)
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/map_n_crisis.png")
    st.plotly_chart(fig2, use_container_width=True) 
    st.write("Mapping facebook mobility in size and color in NO2 level")
    fig3 = px.scatter_mapbox(df, lat="lat", lon="lon", color = 'log_NO2', size ='facebook_movement', hover_data = ['country'], size_max = 15, color_continuous_scale=px.colors.cyclical.IceFire, zoom = 3, width=800, height=600)
    st.plotly_chart(fig3, use_container_width=True) 
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/NO2_ncrisis_map.png")
    st.subheader("3. Example using scatter app:")
    st.write("NO2 vs. facebook mobility; color represents country")
    fig4 = px.scatter(df[df['date']>'2021-04-02'], x = 'log_NO2' , y = 'log_facebook_movement' , color = 'country', marginal_x = 'histogram', marginal_y = 'rug', height = 600)
    st.plotly_chart(fig4, use_container_width=True)
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/scatter_NO2_ncrisis.png")
    st.subheader("4. Example using 3Dmap app:")
    st.write("Elevation represents facebook mobility and color shows NO2 level")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/map3d.png")
    st.subheader("5. Example using Train a model app:")
    st.write("After training a model, we can take a look at the impacts of different parameters on NO2")
    st.markdown(""" ### Summary plot """)
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/summary_bar.png")
    # st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/Summary_shap.png")
    st.markdown(""" ### Dependence plot """)
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graph/log_n_crisis_shap.png")