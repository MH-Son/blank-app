import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
file_path = 'movies_2024.csv'
df = pd.read_csv(file_path)

# Streamlit app
st.title('Budget vs Revenue Relationship')

# Show data preview
st.subheader('Dataset Preview')
st.dataframe(df.head())

# Check if required columns are present
if 'budget' in df.columns and 'revenue' in df.columns:
    # Drop rows with missing values in budget or revenue
    df_filtered = df.dropna(subset=['budget', 'revenue'])

    # Plotting budget vs revenue
    st.subheader('Budget vs Revenue Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(df_filtered['budget'], df_filtered['revenue'], alpha=0.5)
    ax.set_xlabel('Budget')
    ax.set_ylabel('Revenue')
    ax.set_title('Budget vs Revenue')
    st.pyplot(fig)
else:
    st.error('The dataset does not contain required columns: "budget" and "revenue"')
