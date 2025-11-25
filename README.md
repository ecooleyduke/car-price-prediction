# Car Price Predictor

## Project Overview

This project demonstrates a full-stack machine learning pipeline that predicts car prices based on features like brand, model, year, mileage, fuel type, transmission, and condition. The project emphasizes MLOps best practices, including reproducibility, cloud deployment, experiment tracking, and modular design.

The pipeline covers:

* Data ingestion from the cloud
* Preprocessing and feature engineering
* Model training and evaluation
* Experiment tracking using MLFlow
* API serving with FastAPI
* Front-end application with Streamlit deployed on Hugging Face Spaces

---

## Dataset

**Car Price Prediction Dataset (2025)**
Source: [Kaggle](https://www.kaggle.com/datasets/aliiihussain/car-price-prediction)

**Features:**

* `Car ID`: Unique identifier
* `Brand`: Car manufacturer (e.g., Toyota, Honda)
* `Model`: Car model
* `Year`: Manufacturing year
* `Mileage`: Distance driven (km)
* `Fuel Type`: Petrol, Diesel, Hybrid, Electric
* `Transmission`: Manual / Automatic
* `Condition`: New, Used, Excellent, etc.
* `Price`: Market price of the car (target variable)

---

## Model Architecture

* **Model Type:** Random Forest Regressor
* **Pipeline Steps:**

  1. Load data from cloud storage
  2. Preprocess features (e.g., OneHotEncode categorical variables)
  3. Train/test split
  4. Model training
  5. Evaluation using RMSE/MAE
* **Experiment Tracking:** MLFlow logs model parameters, metrics, and artifacts

---

## Cloud Services Used

* **Data Storage:** Public CSV hosted on google cloud
* **API Deployment:** Google Cloud Run
* **Front-End Hosting:** Hugging Face Spaces (Streamlit)
* **Experiment Tracking:** MLFlow local backend

---

## Project Structure

```
car-price-prediction/
├── src/
│   ├── data_ingest.py          # Data ingestion from cloud
│   ├── train.py           # Model training pipeline
│   ├── preprocess_data.py           # Model training pipeline
│   ├── api/
│   │   └── main.py            # FastAPI app with /predict endpoint
│   │   └── schemas.py         # Pydantic schema with CarInput validation
│   └── frontend/
│       └── app.py             # Streamlit front-end
├── Dockerfile                 # Container configuration
├── config.yaml                # Pipeline parameters (split ratio, learning rate, etc.)
├── requirements.txt           # Python dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/ecooleyduke/car-price-prediction.git
cd car-price-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the data
The data comes from Kaggle, but I hosted it publicly on google cloud. It can be found [here]("https://storage.googleapis.com/car-price-data/car_price_prediction_.csv").


```bash
python src/data_ingest.py
```

### 4. Train the Model Locally

```bash
python src/train.py --config config.yaml
```

* Trains the model and saves it in `models/`
* Logs experiments to MLFlow (`mlruns/`)
* Check out the MLFlow experiment runs by opening up the MLFlow server: `mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns` then opening up http://127.0.0.1:5000 in your web browser.

### 5. Run API Locally

```bash
uvicorn src.api.main:app --reload
```

Test locally using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "Brand": "Toyota",
  "Model": "Corolla",
  "Year": 2017,
  "Mileage": 65000,
  "Fuel Type": "Petrol",
  "Transmission": "Automatic",
  "Condition": "Used"
}'
```

## Public Access

This app was containerized using Docker by running

```
docker buildx build --platform linux/amd64 -t ethancooley/car-price-api-amd .  
```

It was then pushed to Docker Hub. The image can be found here [ethancooley/car-price-api-amd:latest](https://hub.docker.com/layers/ethancooley/car-price-api-amd/latest/images/sha256:b6d1f1eed3786c9e30ee6a207ac412b5e5e22c10c7c30e76be0bb479f537f8aa?uuid=4ed497af-ccaf-4648-8c99-a434d595c18c)

It was then deployed to a Google Cloud Run server.
The server can be accessed [here](https://car-price-api-amd-881281483784.europe-west1.run.app). Visit it and you should see the message: `Car Price Prediction API running`!
The endpoint to call for predictions is `/predict`



## Front-End Application

**Live App:** [Car Price Predictor](https://huggingface.co/spaces/ecooley/Car-Price-Predictor)

* Built with Streamlit on HuggingFace Spaces
* Collects user input (brand, model, year, mileage, fuel type, transmission, condition)
* Sends POST request to deployed Cloud Run API
* Displays predicted car price interactively

---

## Notes on Best Practices

* **Version Control:** GitHub with branches and pull requests
* **Reproducibility:** `config.yaml` controls pipeline parameters
* **Experiment Tracking:** MLFlow logs metrics, parameters, and artifacts
* **Modular Design:** Separate modules for data ingestion, model training, API, and front-end

---

## AI Usage
- AI was used to help generate this README.md.
- AI was also used to help generate the training parameters for the Random Forest Regressor model.
- Other than that, no AI was used.