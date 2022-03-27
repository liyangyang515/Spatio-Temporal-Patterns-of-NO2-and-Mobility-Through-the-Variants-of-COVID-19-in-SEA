import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model
import numpy as np
import shap

# model_path = st.file_uploader('Choose a h5 file', type = 'h5')
model = load_model('https://raw.githubusercontent.com/liyangyang515/Spatio-Temporal-Patterns-of-NO2-and-Mobility-Through-the-Variants-of-COVID-19-in-SEA/blob/main/model/MLP_all_mobility.h5') 
explainer = shap.DeepExplainer(model, X_train[:5000])
