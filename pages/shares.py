import streamlit as st
import pandas as pd
import numpy as np
st.title("Shares Price")


















DATA_URL = ('./ADANIPORTS.csv')

@st.cache_data
def load_data(nrows):
    st.header("Adani Ports")
    data = pd.read_csv(DATA_URL, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")















DATA_URL2 = ('./ASIANPAINT.csv')

@st.cache_data
def load_data2(nrows):
    st.header("Asian Paint")
    data = pd.read_csv(DATA_URL2, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data2(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")
















DATA_URL3 = ('./AXISBANK.csv')

@st.cache_data
def load_data2(nrows):
    st.header("Axis Bank")
    data = pd.read_csv(DATA_URL3, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data2(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")









DATA_URL4 = ('./BAJAJFINSV.csv')

@st.cache_data
def load_data2(nrows):
    st.header("Bajaj Finsv")
    data = pd.read_csv(DATA_URL4, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data2(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")















DATA_URL5 = ('./BAJAJ-AUTO.csv')

@st.cache_data
def load_data2(nrows):
    st.header("Bajaj Auto")
    data = pd.read_csv(DATA_URL5, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data2(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")

















DATA_URL6 = ('./SUNPHARMA.csv')

@st.cache_data
def load_data2(nrows):
    st.header("Sun Pharma")
    data = pd.read_csv(DATA_URL6, nrows=nrows)
    chart_data = pd.DataFrame(
        {
            "price": data["High"]
        }
    )
    st.bar_chart(data=chart_data)
    st.write(data)

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data2(10000)
# Notify the reader that the data was successfully loaded.

data_load_state.text("Done! (using st.cache_data)")
