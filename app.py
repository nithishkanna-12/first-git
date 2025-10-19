import pandas as pd
import plotly.express as px
import streamlit as st

# 1. Load preprocessed dataset from Milestone 1
df = pd.read_csv('processed_global_weather.csv')

st.title("🌦 ClimateScope: Global Weather Dashboard")

# 2. Sidebar filters
regions = st.sidebar.multiselect("Select Regions", df['region'].unique())
variables = st.sidebar.selectbox("Select Variable", ['temperature', 'humidity', 'precipitation'])

filtered_df = df[df['region'].isin(regions)] if regions else df

# 3. Choropleth map
st.subheader(f"Global {variables.title()} Distribution")
fig_map = px.choropleth(
    filtered_df,
    locations="country_code",
    color=variables,
    hover_name="country",
    projection="natural earth",
    title=f"{variables.title()} by Country"
)
st.plotly_chart(fig_map)

# 4. Time series line chart
st.subheader(f"{variables.title()} Trends Over Time")
fig_line = px.line(
    filtered_df.groupby(['year', 'region'])[variables].mean().reset_index(),
    x='year', y=variables, color='region',
    title=f"{variables.title()} Trends"
)
st.plotly_chart(fig_line)
