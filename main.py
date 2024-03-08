
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

# Radio button for key selection
key_type = st.radio(
    "Choose your key",
    ('Your Key', 'Free Key (capped)')
)

# Tabs for dataset topics
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Sci-fi Movies", "Animals", "Pop Songs", "POTUS's Twitter", "Blank"])

with tab1:
    # Inside the "Sci-fi Movies" tab
    st.header("Sci-fi Movies")
    
    # Input for dataset topic
    dataset_topic = st.text_input("What is the topic of your dataset?", "Sci-fi movies")
    
    # Columns for data specifications
    col1, col2, col3 = st.columns(3)
    with col1:
        title = st.text_input("1st column", "Title")
    with col2:
        year = st.text_input("2nd column", "Year")
    with col3:
        pg_rating = st.text_input("3rd column", "PG rating")
    
    # Number of rows selection
    num_rows = st.number_input("How many rows do you want?", min_value=1, value=5)
    
    # Button to build dataset
    if st.button("Build my dataset! ✨"):
        generate_dataset()

# Repeat similar structures for the other tabs...

# Using different functions for different dataset types might be required, 
# but for now, we're using the same placeholder for simplicity.

