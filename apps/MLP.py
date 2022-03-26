import streamlit as st
from streamlit import caching
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae

def app():    
    df = pd.read_csv('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/main/data/merge_by_month.csv', index_col = 0)
    clist = df.columns.values.tolist()
    layer_number = int(st.sidebar.number_input("Enter number of dense layers"))
    layer_node = int(st.sidebar.number_input("Enter number of nodes in each dense layer"))
    batch_size = int(st.sidebar.number_input("Enter batch_size:"))
    epoch = int(st.sidebar.number_input("Enter number of epoches:"))
    before_normalized_X = df[['lon','lat','day', 'tp','u-wind', 'v-wind', 'wind_speed', 'surface-p', 'dew-pt', '2m-temp', 'n_crisis', 'log_n_crisis', 'driving', 'walking', 'haze']]
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

    st.write('Try with a large batch size (eg, 100) and a small epoch number (eg, 20)!')
    if st.button('Start Training!'):
        st.info('Starting training with ' + str(epoch) + ' epoches! Just wait for the graphs')
        history = model.fit(
            X_train, y_train,
            validation_data = (X_test, y_test),
            batch_size = batch_size,
            epochs = epoch,
        #    callbacks=[early_stopping], # put your callbacks in a list
        #    verbose=0,  # turn off training log
        )
        st.success('Success! Click clear histories below the graph and restart with new model!')
        history_df = pd.DataFrame(history.history)
        st.line_chart(history_df.loc[:, ['loss', 'val_loss']], use_container_width=True);
        st.write("Minimum validation loss: {}".format(history_df['val_loss'].min()))
        if st.button('Clear histories'):
            caching.clear_cache()







    
