import streamlit as st
import pandas as pd
import pydeck as pdk

def app():
    # st.header("")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    st.header("The color shows the NO2 level! ")
    clist = df.columns.values.tolist()
    year = st.sidebar.selectbox('select year', [2020, 2021])
    month = st.sidebar.slider("select month", 1, 12)
    elevation = st.sidebar.selectbox('select elevation', clist)
    scale = st.sidebar.slider("select scale", 0.5, 50000.5, 10000.0)
    # st.header("Mapping color in " + color + ' and ' + ' size in ' )
    data = df[(df['year'] == year) & (df['month'] == month)]

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',map_provider="mapbox",
        # map_provider="mapbox",
        # map_style=pdk.map_styles.SATELLITE,
        initial_view_state=pdk.ViewState(
            latitude=1,
            longitude=105,
            zoom=4,
            pitch=50
        ),
        layers=[
            pdk.Layer(
                'ColumnLayer',
                data=data,
                get_position='[lon, lat]',
                get_elevation= elevation,
                get_fill_color = '[500/log_NO2, 500/log_NO2, 255]',
                radius = 17500,
                auto_highlight = True,
                elevation_scale= scale,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
                coverage=1,
            ),
        ],
    ))

