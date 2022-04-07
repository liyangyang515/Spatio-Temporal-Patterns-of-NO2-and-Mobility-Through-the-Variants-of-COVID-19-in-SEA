# Spatio-Temporal Patterns of NO2 Level & Human Mobility Through the Variants of COVID-19 in South-East Asia

> This is an **open-source project** and you are very welcome to contribute your comments, questions, resources, and apps as [issues](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/issues) or 
> [pull requests](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/pulls) to the [GitHub repository](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA).
        
<br>

Feel free to go to our **[storymap](https://storymaps.arcgis.com/stories/28655bd2a29e4d2481feeccd47bc6575)**, our **[web app](https://share.streamlit.io/liyangyang515/spatio-temporal-patterns-of-no2-and-mobility-through-the-variants-of-covid-19-in-sea/main/app.py)** and our **web map layers** for more comprehensive information and references.

<br>

To run our web app locally:
```
streamlit run app.py
```
<br>
In this project, we aim to investigate the **Impact of Covid-19 on Spatial-Temporal Variation of NO2 Levels and Its Sensitivity to Mobility in South-East Asia**.

<br>

### Our objectives:
1. Identify the temporal changes of NO 2  and mobility throughout the three waves of COVID-19 (Mar 2020 - Feb 2022) in Indonesia

2. Evaluate the spatio-temporal patterns in NO 2  level and mobility in the entire SEA throughout Delta and Omicron (Jun 2021 - Feb 2022) using Space-time Cube (STC) and emerging hotspot analysis ​

3. Develop a machine learning model to predict NO 2  for SEA and assess the sensitivity of NO 2  to key influencing factors

<br>

**Code**
* [NO2 data pulled from Google Earth Engine using geemap](https://github.com/liyangyang515/NO2-in-South-East-Asia-_GE5219/blob/main/code/NO2_From_GEE_SEA.ipynb)  

* [Haze searches from Google Trends using pytrends](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/code/haze.ipynb)

* [Merge data before MLP](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/code/5219_data%20preprocessing_MLP.ipynb)

* [Data preprocessing, MLP and explainability](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/code/5219_MLP_Explainability.ipynb)


<br>

**App**
* The [app folder](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/tree/main/apps) collects all different apps written in pure python that were used in the [multi-page app](https://github.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/app.py)

<br>

**Python Packages/Libraries utilised**
Some of which are really impressive and can be used in most fields:
* Data pulling and pre-preprocessing: [pandas](https://pandas.pydata.org/docs/index.html), [Numpy](https://numpy.org/doc/stable/), [geemap](https://geemap.org/), [pytrends](https://pypi.org/project/pytrends/)

* Model and its explanabiltiy: [keras](https://keras.io/), [tensorflow](https://www.tensorflow.org/), [scikit-learn](https://scikit-learn.org/stable/), [shap](https://shap.readthedocs.io/en/latest/index.html)

* Visualisation: [matplotlib](https://matplotlib.org/), [plotly](https://plotly.com/), [pydeck](https://deckgl.readthedocs.io/en/latest/), [streamlit](https://streamlit.io/)
