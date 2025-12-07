# 🍽️ Zomato Restaurants EDA Dashboard

An interactive exploratory data analysis (EDA) dashboard built using **Python, Pandas, Plotly and Streamlit** on the Zomato Restaurants dataset.

🔗 **Live App:** https://vinay-zomato.streamlit.app/  
💻 **Tech Stack:** Python, Pandas, Plotly, Streamlit

---

## 📊 Project Overview

This project analyzes **9,500+ restaurant records** from Zomato across multiple cities and provides insights into:

- City-wise restaurant distribution  
- Most popular cuisines  
- Cost categories (Budget / Midrange / Premium)  
- Online delivery availability  
- Relationship between cost and ratings  
- Top highly-rated restaurants

The goal is to demonstrate **real-world data cleaning, feature engineering, visualization and dashboard building** skills for data science roles.

---

## 🧹 Data Cleaning & Feature Engineering

Key steps performed in the notebook:

- Removed unnecessary columns (ID, coordinates, etc.)
- Dropped duplicate restaurant entries  
- Handled missing values in `Cuisines` and other columns  
- Standardized text columns (city, locality, cuisines, rating text)  
- Converted Yes/No fields to binary (0/1)  
- Filtered out restaurants with `Aggregate rating == 0`  
- Created:
  - `Primary Cuisine` → first cuisine from the list  
  - `Cost_for_Two` → cleaned and renamed  
  - `Cost Category` → Budget / Midrange / Premium based on cost  

Cleaned data is stored in: **`zomato_cleaned.csv`**

---

## 🖥️ Dashboard Features

The Streamlit app (`app.py`) provides:

### 🔍 Filters (Sidebar)
- Filter by **City**
- Filter by **Cost Category**
- Filter by **Online delivery** (Yes / No)

### 📈 Visualizations

- **Top 10 Cities by restaurant count**
- **Top 10 Primary Cuisines**
- **Cost Category distribution (pie chart)**
- **Online delivery availability (pie chart)**
- **Cost vs Rating scatter plot**
- **Table of Top 20 highly rated restaurants (rating ≥ 4.5)**

---

## 🚀 How to Run Locally

```bash
# clone the repo
git clone https://github.com/vinaypratapsinghrathore/zomato-eda-dashboard.git
cd zomato-eda-dashboard

# install dependencies
pip install -r requirements.txt

# run the app
streamlit run app.py
