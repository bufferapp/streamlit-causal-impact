import datetime

import pandas as pd
import streamlit as st
from causalimpact import CausalImpact

st.title("Causal Impact")

data = st.file_uploader("Upload", type="csv")

if data is not None:
    df = pd.read_csv(data)
    value_column = st.selectbox("Which column contains the values", df.columns)
    y = df[value_column]

    date_column = st.selectbox("Which column contains the dates", df.columns)
    dates = df[date_column]

    intervention = st.date_input(
        "When did the intervention took place?", datetime.date.today()
    )

    pre_period = [0, 20]
    post_period = [21, 29]

    if st.button("RUN"):
        ci = CausalImpact(y, pre_period, post_period)
        st.text(ci.summary(output="report"))
