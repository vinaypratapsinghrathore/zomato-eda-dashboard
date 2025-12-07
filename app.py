# app.py
# Zomato EDA Dashboard using Streamlit + Plotly

import pandas as pd
import plotly.express as px
import streamlit as st

# -----------------------
# 1. PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Zomato EDA Dashboard",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Zomato Restaurants EDA Dashboard")
st.markdown("A data exploration dashboard built with **Streamlit + Plotly**")

# -----------------------
# 2. LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("zomato_cleaned.csv")
    return df

df = load_data()

# -----------------------
# 3. SIDEBAR FILTERS
# -----------------------
st.sidebar.header("🔍 Filters")

# City filter
cities = ["All"] + sorted(df["City"].unique().tolist())
selected_city = st.sidebar.selectbox("Select City", cities)

# Cost Category filter
cost_cats = ["All"] + sorted(df["Cost Category"].unique().tolist())
selected_cost = st.sidebar.selectbox("Select Cost Category", cost_cats)

# Online Delivery filter
delivery_option = st.sidebar.selectbox("Online Delivery", ["All", "Yes Only", "No Only"])

# Apply filters on dataframe
filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[filtered_df["City"] == selected_city]

if selected_cost != "All":
    filtered_df = filtered_df[filtered_df["Cost Category"] == selected_cost]

if delivery_option == "Yes Only":
    filtered_df = filtered_df[filtered_df["Has Online delivery"] == 1]
elif delivery_option == "No Only":
    filtered_df = filtered_df[filtered_df["Has Online delivery"] == 0]

st.write(f"### Total Restaurants after filters: {filtered_df.shape[0]}")

# -----------------------
# 4. TOP METRICS
# -----------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Unique Cities", filtered_df["City"].nunique())
with col2:
    st.metric("Unique Cuisines", filtered_df["Primary Cuisine"].nunique())
with col3:
    st.metric("Avg Rating", round(filtered_df["Aggregate rating"].mean(), 2))
with col4:
    st.metric("Avg Cost for Two", int(filtered_df["Cost_for_Two"].mean()))

st.markdown("---")

# -----------------------
# 5. PLOTS ROW 1
# -----------------------
colA, colB = st.columns(2)

# Top Cities
with colA:
    st.subheader("🏙️ Top 10 Cities by Restaurant Count")
    city_counts = filtered_df["City"].value_counts().head(10)
    fig_city = px.bar(
        city_counts,
        x=city_counts.index,
        y=city_counts.values,
        labels={'x': 'City', 'y': 'Restaurant Count'},
    )
    st.plotly_chart(fig_city, use_container_width=True)

# Top Cuisines
with colB:
    st.subheader("🍜 Top 10 Primary Cuisines")
    cuisine_counts = filtered_df["Primary Cuisine"].value_counts().head(10)
    fig_cuisine = px.bar(
        cuisine_counts,
        x=cuisine_counts.index,
        y=cuisine_counts.values,
        labels={'x': 'Cuisine', 'y': 'Restaurant Count'},
    )
    st.plotly_chart(fig_cuisine, use_container_width=True)

st.markdown("---")

# -----------------------
# 6. PLOTS ROW 2
# -----------------------
colC, colD = st.columns(2)

# Cost Category Pie
with colC:
    st.subheader("💰 Cost Category Distribution")
    fig_cost = px.pie(
        filtered_df,
        names="Cost Category",
        hole=0.3
    )
    st.plotly_chart(fig_cost, use_container_width=True)

# Online Delivery Pie
with colD:
    st.subheader("📦 Online Delivery Availability")
    filtered_df["Online Delivery Label"] = filtered_df["Has Online delivery"].map({1: "Yes", 0: "No"})
    fig_delivery = px.pie(
        filtered_df,
        names="Online Delivery Label",
        hole=0.3
    )
    st.plotly_chart(fig_delivery, use_container_width=True)

st.markdown("---")

# -----------------------
# 7. COST vs RATING SCATTER
# -----------------------
st.subheader("⭐ Cost vs Rating")

fig_scatter = px.scatter(
    filtered_df,
    x="Cost_for_Two",
    y="Aggregate rating",
    color="Cost Category",
    hover_data=["Restaurant Name", "City", "Primary Cuisine"],
)
st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------
# 8. TOP HIGH RATED RESTAURANTS
# -----------------------
st.subheader("🏆 Top 20 Highly Rated Restaurants (Rating ≥ 4.5)")

top_rated = filtered_df[filtered_df["Aggregate rating"] >= 4.5].sort_values(
    by="Aggregate rating", ascending=False
).head(20)

st.dataframe(
    top_rated[["Restaurant Name", "City", "Primary Cuisine", "Aggregate rating", "Cost_for_Two", "Votes"]]
)
