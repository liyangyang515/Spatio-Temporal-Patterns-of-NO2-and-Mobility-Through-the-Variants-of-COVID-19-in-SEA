import streamlit as st
import pandas as pd

def app():
    st.markdown(
        """
        This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io), written purely in Python.
        This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/issues) or 
        [pull requests](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/pulls) to the [GitHub repository](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA).
        """
    )

    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    
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
    with st.expander("See explanations of each parameter"):
        st.markdown("""
         **mobility**
         * n_crisis: facebook mobility level
         * driving: apple mobility with driving mode
         * walking: apple mobility with walking mode
         **weather**
         * tp: rainfall
         * surface-p: surface air pressure
         * 2m-temp: air temperature
         * dew-pt: dew point
         **haze**
         **spatial information**
         * lon: longitude
         * lat: latitude
         **temporal information**
         * day: day number from the start (Apr 1, 2020)
         **NO2 level**
         """)
    
    st.header("Some Visualisaition Examples")
    st.markdown(
        """
        The following visualisaitions were created using this multi-page web app. 
    """
    )
    st.subheader("1. Example using map app:")
    st.write("NO2 Mapping")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graphs/map_NO2.png")
    st.write("Facebook Mobility Mapping")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graphs/map_n_crisis.png")
    st.write("Mapping facebook mobility in size and color in NO2 level")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graphs/NO2_ncrisis_map.png")
    st.subheader("2. Example using scatter app:")
    st.write("NO2 vs. facebook mobility; color represents country")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graphs/scatter_NO2_ncrisis.png")
    st.subheader("3. Example using 3Dmap app:")
    st.write("Elevation represents facebook mobility and color shows NO2 level")
    st.image("https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/graphs/map3d.png")
