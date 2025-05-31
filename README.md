# 🧠 Retail Inventory Optimization with Predictive Analytics & Dashboarding

## 🔹 About

This is a comprehensive end-to-end data science and machine learning project focused on **retail inventory optimization**. The goal is to leverage data-driven techniques to enhance inventory management through intelligent forecasting, interactive dashboards, and model deployment. The project simulates a real-world pipeline from raw data ingestion to live model visualization.

---

## 📁 Project Structure

```text
├── CleanedDataSet.csv              # Preprocessed dataset ready for modeling
├── retail_store_inventory.csv      # Raw inventory dataset
├── Data Collection & Exploration.ipynb
├── Data Preprocessing & EDA.ipynb
├── Feature engineering & Data Visualization.ipynb
├── Dashboard - Plotly.ipynb        # Dash-based interactive dashboard
├── Model Selection.ipynb
├── ML flow.ipynb                   # Model tracking with MLflow
├── machinelearning flow.ipynb      # Additional modeling steps
├── streamlit_app.py                # Deployed app on local host
├── default_inputs.pkl, encoder.pkl, feature_info.pkl
├── xgb_profit_model.pkl            # Trained model for profit prediction
├── xgb_units_model.pkl             # Trained model for units forecast
├── README.md
```
## 🚀 Workflow Summary

### 1. Data Preprocessing & Cleaning
Loaded raw retail purchase data

Applied pandas and NumPy for wrangling

Treated missing values with advanced techniques

Feature transformations using:

Label Encoding

One-Hot Encoding

Removed or added features based on impact on model performance

### 2. Feature Engineering & EDA

Statistical analysis & correlation evaluation

Created derived variables for enhanced modeling

Visualized relationships using:

seaborn, matplotlib

Boxplots, pairplots, heatmaps, bar charts

### 3. Dashboarding

Interactive Dash & Plotly dashboard (Jupyter-based)

Power BI dashboard for business insights:

Sales trends

Store-specific performance

Product category profitability

Out-of-stock alerts

### 4. Modeling & Evaluation

Built and compared multiple models:

XGBoost (Best performer)

Prophet (Time series)

LSTM (Deep learning model for sequence prediction)

Tracked experiments and performance metrics using MLflow

### 5. Deployment
Deployed the best model (XGBoost) using Streamlit

Hosted a local web app to demonstrate:

Model input/output

Predictive analytics in real time

Default test inputs loaded from .pkl files

Demonstrated impact of the solution through real-time UI

## ✅ Features Delivered
✔️ Cleaned and production-ready datasets

✔️ Exploratory data analysis (EDA)

✔️ Advanced feature engineering

✔️ ML model training & tuning

✔️ Dashboarding (Plotly & Power BI)

✔️ Streamlit deployment for demo purposes

✔️ MLflow for experiment tracking

## 📊 Tools & Libraries
Python, Pandas, NumPy

Seaborn, Matplotlib, Plotly, Dash

Scikit-learn, XGBoost, Prophet, LSTM

MLflow, Streamlit, Power BI

## 🌟 Outcome
This project is a simulation of a real-world AI product cycle—from messy raw data to actionable business insight and user-ready app. It highlights Mariom's strengths in:

Data wrangling

Feature intuition

Model development

Deployment engineering

Insightful storytelling through dashboards

## 🧠 Author
Mariam Ibrahim

Electronics & Communication Engineering Student | Data Science Enthusiast | Aspiring Embedded + AI Engineer

📌 GitHub: [https://github.com/mariamibrahimzz/]

📌 LinkedIn: [https://www.linkedin.com/in/mariamibrahimmzz/]

📌 Email: mariam2309039@miuegypt.edu.eg

⭐ If you find this project insightful, feel free to give it a star and share feedback!





