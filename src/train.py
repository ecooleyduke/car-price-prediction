import mlflow
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

from utils import load_config
from preprocess_data import load_raw_data, preprocess, split


def main():

    cfg = load_config()
    raw_path = f"{cfg['data']['output_dir']}/{cfg['data']['output_file']}"
    df = load_raw_data(raw_path)
    df = preprocess(df, cfg)

    X_train, X_test, y_train, y_test = split(df, cfg)

    preprocess_steps = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cfg["preprocessing"]["categorical_features"]),
            ("num", "passthrough", cfg["preprocessing"]["numeric_features"])
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocess_steps),
            ("rf", RandomForestRegressor(
                n_estimators=cfg["training"]["model"]["n_estimators"],
                max_depth=cfg["training"]["model"]["max_depth"],
                random_state=cfg["training"]["random_state"]
            ))
        ]
    )

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("car-price-random-forest")
    with mlflow.start_run():

        model.fit(X_train, y_train)

        r2 = model.score(X_test, y_test)

        mlflow.log_param("n_estimators", cfg["training"]["model"]["n_estimators"])
        mlflow.log_param("max_depth", cfg["training"]["model"]["max_depth"])
        mlflow.log_metric("r2", r2)

        joblib.dump(model, "src/models/model.pkl")
        mlflow.log_artifact("src/models/model.pkl")

        print(f"Model trained. R2: {r2}")

if __name__ == "__main__":
    main()
