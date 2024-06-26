import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

#Reading Excel File
st.header('1. Excel Data')

# Define the path to the CSV file
file_path = 'DeptSales.csv'

# Read the CSV file, treating the first row as headers
df = pd.read_csv(file_path)

# Set the first row as the column names
df.columns = df.iloc[0]

# Drop the first row since it's now the header
df = df[1:]
date_column = df.columns[0]
df.drop(columns=[df.columns[1]], inplace=True)

# Set the first column (Date) as the index
df.set_index(date_column, inplace=True)
df.index = pd.to_datetime(df.index)  # Ensure the index is in datetime format

# Display the DataFrame
st.dataframe(df)

departments = df.columns.tolist()
selected_department = st.selectbox('Select a department', departments)

# Select a date range
start_date = st.date_input('Start date', df.index.min())
end_date = st.date_input('End date', df.index.max())

# Filter the data based on the selected department and date range
filtered_df = df.loc[start_date:end_date, selected_department]

# Sort the filtered data by the date index in ascending order
filtered_df = filtered_df.sort_index(ascending=True)
# Plot the data
st.header(f'3. Line Chart for {selected_department}')
fig = px.line(filtered_df, x=filtered_df.index, y=filtered_df.values, labels={'x': 'Date', 'y': selected_department})

st.plotly_chart(fig)
