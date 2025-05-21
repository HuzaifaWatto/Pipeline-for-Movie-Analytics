# Step 4: Streamlit Dashboard
import streamlit as st
import sqlite3
import pandas as pd

st.title("🎬 IMDB Movie Data Dashboard")

# Connect to DB
conn = sqlite3.connect('movies.db')

# Filters
genre = st.selectbox("Select Genre", options=["All"] + ['Drama', 'Comedy', 'Action', 'Horror'])
year = st.slider("Select Release Year Range", 1980, 2024, (2000, 2023))
rating = st.slider("Minimum Rating", 0.0, 10.0, 5.0)

# Build SQL query
query = "SELECT * FROM Movies WHERE 1=1"
if genre != "All":
    query += f" AND Genre = '{genre}'"
query += f" AND ReleaseYear BETWEEN {year[0]} AND {year[1]}"
query += f" AND Rating >= {rating}"

# Load data
df = pd.read_sql_query(query, conn)

st.write(f"Showing {len(df)} movies")
st.dataframe(df)

# Visualizations
st.subheader("📊 Rating Distribution")
st.bar_chart(df['Rating'].value_counts().sort_index())

st.subheader("💵 Revenue vs Rating")
st.scatter_chart(df[['Rating', 'RevenueMillions']])

