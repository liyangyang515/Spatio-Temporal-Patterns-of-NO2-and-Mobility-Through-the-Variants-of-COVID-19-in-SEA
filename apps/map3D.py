import streamlit as st
import pandas as pd

def app():
    st.header("")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    # st.title("")
    clist = df.columns.values.tolist()
    color = st.sidebar.selectbox("Select color:",clist)
    year = st.sidebar.selectbox('select year', [2020, 2021])
    month = st.sidebar.slider("select month", df[df['year']==year].values.tolist())
    st.header("Mapping color in " + color + ' and ' + ' size in ' + size)
    data = df[(df['year'] == year) & (df['month'] == month) ]
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=-23.901,
            longitude=-46.525,
            zoom=5,
            pitch=50
        ),
        layers=[
            pdk.Layer(
                'Log_n_crisis'
                data=data,
                get_position='[lon, lat]',
                get_elevation='[Log_n_crisis]',
                radius=20000,
                auto_highlight=True,
                elevation_scale=100,
                elevation_range=[0, 5000],
                pickable=True,
                extruded=True)]
    ))

