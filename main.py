
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

import streamlit as st

# Placeholder functions
def generate_dataset():
    pass

# Title
st.title("Build your dataset")


# Tabs for dataset topics
tab1, tab2, tab3, tab4, tab5 = st.tabs(["High Correlation", "Low Correlation", "High Data Sparsity", "Low Data Sparsity", "High Feature Noise"])

with tab1:
    # Inside the "Sci-fi Movies" tab
    st.header("High Correlation")
    
    # Input for dataset topic
    dataset_topic = st.text_input("What is the title of your dataset?", "High Correlation")

    # Columns for data specifications with sliders
    col1, col2, col3 = st.columns(3)
    with col1:
        title_slider = st.slider("Feature Correlation", min_value=0.0, max_value=1.0, value=0.9, step=0.05)
    with col2:
        year_slider = st.slider("Data Sparsity", min_value=0, max_value=100, value=50, step=10)
    with col3:
        pg_rating_slider = st.slider("Feature Noise", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    
    # with col1:
    #     title = st.text_input("1st column", "Title")
    # with col2:
    #     year = st.text_input("2nd column", "Year")
    # with col3:
    #     pg_rating = st.text_input("3rd column", "PG rating")
    
    # Number of rows selection
    num_rows = st.number_input("How many data instances do you want?", min_value=1, value=5)
    
    # Button to build dataset
    if st.button("Build my dataset! ✨"):
        generate_dataset()

# Repeat similar structures for the other tabs...

# Using different functions for different dataset types might be required, 
# but for now, we're using the same placeholder for simplicity.

