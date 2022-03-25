import streamlit as st

def app():
    st.title("Streamlit for Geospatial Applications")

    st.markdown(
        """
        This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io).
        This is an open-source project and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/issues) or 
        [pull requests](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/pulls) to the [GitHub repository](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA).
        """
    )

    st.info("Click on the left sidebar menu to navigate to the different apps.")

    st.subheader("Some Visualisaition Examples")
    st.markdown(
        """
        The following visualisaitions were created using this multi-page web app. 
    """
    )

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.image("https://github.com/liyangyang515/graphs/NO2_ncrisis_map.png")
        st.image("https://github.com/liyangyang515/graphs/NO2_ncrisis_map.png")

    with row1_col2:
        st.image("https://github.com/liyangyang515/graphs/NO2_ncrisis_map.png")
        st.image("https://github.com/liyangyang515/graphs/NO2_ncrisis_map.png")