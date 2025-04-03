import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Car Sales Dashboard")

fig_hist = px.histogram(
    df, 
    x='price', 
    color='condition', 
    title='Price Distribution by Condition',
    barmode='overlay'
)

fig_scatter = px.scatter(
    df, 
    x='type', 
    y='price', 
    color='type', 
    title='Price vs. Type'
)

if st.checkbox('Show Price Distribution Histogram'):
    st.plotly_chart(fig_hist)

if st.checkbox('Show Price vs. Type Scatterplot'):
    st.plotly_chart(fig_scatter)

