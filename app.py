import datetime

import numpy as np
import pandas as pd
import streamlit as st
from causalimpact import CausalImpact

st.set_option("deprecation.showPyplotGlobalUse", False)

st.title("Causal Impact")

data = st.sidebar.file_uploader("Upload", type="csv")

if data is not None:
    df = pd.read_csv(data)
    value_column = st.sidebar.selectbox("Which column contains the values", df.columns)
    y = df[value_column]

    date_column = st.sidebar.selectbox("Which column contains the dates", df.columns)
    dates = df[date_column]

    intervention = st.sidebar.date_input(
        "When did the intervention took place?", datetime.date.today()
    )

    pre_period = [0, 20]
    post_period = [21, 29]

    if st.sidebar.button("RUN"):
        ci = CausalImpact(y, pre_period, post_period)
        st.text(ci.summary(output="report"))
        st.pyplot(ci.plot())
