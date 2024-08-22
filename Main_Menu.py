import streamlit as st

st.header('NBA Machine Learning Predictions Dashboard :basketball:', divider=True)


st.page_link("pages/1_Historic_Game_Data.py", label="Historic Predictions", icon="1️⃣")
st.write('A collection of games from previous seasons and the predictions from different \
    machine learning models.')
st.divider()

st.page_link("pages/2_Custom_Game_Predictor.py", label="Custom Game Predictor", icon="2️⃣")
st.write('A custom game predictor that allows you to input a custom set of stats \
     to see how different inputs affect the predictions of models.')
st.divider()

st.page_link("pages/3_Glossary.py", label="Glossary", icon="3️⃣")
st.write('A glossary of terms describing the various basketball-related abbreviations.')
st.divider()

st.markdown("Data was sourced from the [NBA Database](https://www.kaggle.com/datasets/wyattowalsh/basketball) uploaded \
to Kaggle by Wyatt Walsh, and from [sportsdatabase.com](https://sportsdatabase.com).")