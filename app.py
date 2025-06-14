import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import streamlit as st
import pandas as pd
import pickle
from src.features import extract_url_features

model = pickle.load(open("saved_models/phishing_model.pkl", "rb"))

st.title("🔍 Phishing URL Detector")

url = st.text_input("Enter URL:")
if url:
    feats = extract_url_features(url)
    df_ = pd.DataFrame([feats])
    pred = model.predict(df_)[0]
    if pred == 1:
        st.success("✅ Legitimate")
    else:
        st.error("⚠️ Phishing!")
