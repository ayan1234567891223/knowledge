import streamlit as st
import pandas as pd
import numpy as np
st.title("Population")

DATE_COLUMN = 'Capital/Population'
DATA_URL = ('C:/Users/Acer/Desktop/streamlit/pages/world_population.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "population_2022": data["2022 Population"],
            "country": data["Country/Territory"]
        }
    )
    st.bar_chart(data=chart_data, x="country", y="population_2022")
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")