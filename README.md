# car-price-prediction

mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns

curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
  "Brand": "Toyota",
  "Model": "Corolla",
  "Year": 2017,
  "Mileage": 65000,
  "Fuel_Type": "Petrol",
  "Transmission": "Automatic",
  "Condition": "Used"
}'