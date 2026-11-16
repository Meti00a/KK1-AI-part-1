import streamlit as st 
import pandas as pd 
import joblib 

model = joblib.load("car_price_model.pkl")
columns = joblib.load("car_price_columns.pkl")
df = pd.read_csv("car_price_dataset.csv", sep=";")
st.title("Car price prediciton")
st.write("Enter Car details to reveal the price")
brand = st.selectbox("Brand", sorted(df["Brand"].unique()))
model_name = st.selectbox("Model", sorted(df["Model"].unique()))
year = st.number_input(
  "Year",
  min_value=int(df["Year"].min()),
  max_value=int(df["Year"].max()),
  value = int(df["Year"].max())

)
engine_size = st.number_input("Engine Size", min_value=0.5, max_value=10.0, value=2.0)
fuel_type = st.selectbox("Fuel Type", sorted(df["Fuel_Type"].unique()))
transmission = st.selectbox("Transmission", sorted(df["Transmission"].unique()))
mileage = st.number_input("Mileage", min_value=0, max_value=500000, value=50000)
doors = st.selectbox("Doors", sorted(df["Doors"].unique()))
owner_count = st.number_input("Owner count", min_value=0, max_value=10, value=2)

if st.button("Predict Price"):
  car = pd.DataFrame([{
  "Brand": brand,
  "Model": model_name,
  "Year": year,
  "Engine_Size": engine_size,
  "Fuel_Type": fuel_type,
  "Transmission": transmission,
  "Mileage": mileage,
  "Doors": doors,
  "Owner_Count": owner_count
  
  
  
        }])

  car = pd.get_dummies(car)
  car = car.reindex(columns=columns, fill_value=0)
  price = model.predict(car)[0]

  st.success(f"Estimated car price: {price:.0f}")