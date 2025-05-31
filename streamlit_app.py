
import streamlit as st
import pandas as pd
import pickle

# === Load models and preprocessing artifacts ===
with open('xgb_units_model.pkl', 'rb') as f:
    units_model = pickle.load(f)

with open('xgb_profit_model.pkl', 'rb') as f:
    profit_model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

with open('default_inputs.pkl', 'rb') as f:
    default_inputs = pickle.load(f)

with open('feature_info.pkl', 'rb') as f:
    feature_info = pickle.load(f)

# === Streamlit UI ===
st.title("🛍️ Sales Predictor")

category = st.selectbox("Select Category", options=["Furniture","Clothing","Toys","Electronics"])
region = st.selectbox("Select Region", options=["East", "West", "North", "South"])
weather = st.selectbox("Select Weather Condition", options=["Sunny", "Cloudy", "Rainy", "Snowy"])
holiday = st.selectbox("Holiday/Promotion", options=["No", "Yes"])
date = st.date_input("Select Date")

if st.button("Predict"):
    # === Prepare Input ===
    input_data = default_inputs.copy()
    input_data['Category'] = category
    input_data['Region'] = region
    input_data['Weather Condition'] = weather
    input_data['Holiday/Promotion'] = 1.0 if holiday == "Yes" else 0.0

    date_parsed = pd.to_datetime(date)
    input_data['Day'] = date_parsed.day
    input_data['DayOfYear'] = date_parsed.dayofyear
    input_data['WeekOfYear'] = date_parsed.isocalendar().week

    input_df = pd.DataFrame([input_data])
    
    categorical_features = feature_info['categorical_features']
    encoded_cats = encoder.transform(input_df[categorical_features])
    encoded_cat_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_features))

    numerical_features = feature_info['numerical_features']
    X_input = pd.concat([input_df[numerical_features], encoded_cat_df], axis=1)

    # === Predict ===
    units_pred = units_model.predict(X_input)[0]
    profit_pred = profit_model.predict(X_input)[0]

    # === Display ===
    st.success("✅ Prediction Complete")
    st.metric("📦 Units Sold", f"{units_pred:.2f}")
    st.metric("💰 Profit", f"${profit_pred:.2f}")
