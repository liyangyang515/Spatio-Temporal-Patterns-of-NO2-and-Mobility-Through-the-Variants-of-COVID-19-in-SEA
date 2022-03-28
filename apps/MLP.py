import streamlit as st
from streamlit import caching
import streamlit.components.v1 as components
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import shap
import matplotlib

def app():    
    st.title("Train and explain a model by visualising the impacts of influential factors on NO2 levels")
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    layer_number = st.sidebar.number_input("Enter number of dense layers", min_value = 1, step =1)
    layer_node = st.sidebar.number_input("Enter number of nodes in each dense layer",  min_value = 1, step =1)
    batch_size = st.sidebar.number_input("Enter batch_size:",  min_value = 0, step =100)
    epoch = st.sidebar.number_input("Enter number of epoches:",  min_value = 0, step =10)
    before_normalized_X = df[['lon','lat','day', 'rainfall','u-wind', 'v-wind', 'wind_speed', 'surface-p', 'dew-pt', '2m-temp', 'facebook_movement', 'log_facebook_movement', 'apple_driving', 'apple_walking', 'haze']]
    sc = StandardScaler()
    sc_X = sc.fit(before_normalized_X)
    after_normalized_X = sc_X.transform(before_normalized_X)
    y = df[['log_NO2']]
    X_train, X_test, y_train, y_test = train_test_split(after_normalized_X, y, test_size=0.3, random_state=0)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.Input(shape=(15,)))
    for i in range(layer_number):
        model.add(tf.keras.layers.Dense(layer_node, activation='relu'))
    model.add(tf.keras.layers.Dense(1))
    model.compile(optimizer='adam', loss='mae',)

    st.write('Try first with a large batch size (eg, 1000) and a small epoch number (eg, 10)!')
    if st.button('Start Training!'):
        st.info('Training with ' + str(epoch) + ' epoches! Just wait for the graphs')
        history = model.fit(
            X_train, y_train,
            validation_data = (X_test, y_test),
            batch_size = batch_size,
            epochs = epoch,
        #    callbacks=[early_stopping], # put your callbacks in a list
        #    verbose=0,  # turn off training log
        )
        st.balloons()
        st.success('Success! You can take a look how your train model can be explained or click clear histories and restart to train a new model!')
        history_df = pd.DataFrame(history.history)
        st.line_chart(history_df.loc[:, ['loss', 'val_loss']], use_container_width=True);
        st.write("Minimum validation loss: {}".format(history_df['val_loss'].min()))
        if st.button('Clear histories'):
            caching.clear_cache()
    # model = load_model('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/model/MLP_all_mobility.h5') 
    agree = st.sidebar.checkbox('I also want to see how to explain the model')
    if agree:
    # if st.button('Let us see how to explain the model!'):
        number = st.number_input("How many data records you want to use for explanation (eg, start with 1000)", min_value = 100, step =100)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        shap.initjs()
        feature_names = before_normalized_X.columns
        explainer = shap.DeepExplainer(model, X_train[:2000])
        shap_values = explainer.shap_values(X_test[:number])
            # init the JS visualization code
            # The summary plot shows the most important features and the magnitude of their impact on the model. 
            # It is the global interpretation.
        with st.expander("See the summary plot of various parameters' impacts"):
            st.markdown(""" **summary plot** """)
            fig1 = shap.summary_plot(shap_values[0], feature_names = feature_names)
            st.pyplot(fig1, bbox_inches='tight')
        with st.expander("See the dependence plot of facebook mobility's impacts and how the apple driving mobility interactes with it"):
            st.markdown(""" **dependence plot** """)
            fig2 = shap.dependence_plot('log_facebook_movement', shap_values[0], X_test[:number], interaction_index = 'apple_driving', feature_names = feature_names)
            st.pyplot(fig2, bbox_inches='tight') 

                    
                
               
            
        






    
