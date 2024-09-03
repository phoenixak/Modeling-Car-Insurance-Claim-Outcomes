import mlflow
import mlflow.statsmodels

def log_model_to_mlflow(model, best_feature_df):
    """Logs the model and the best feature to MLflow."""
    with mlflow.start_run():
        mlflow.statsmodels.log_model(model, "best_logistic_regression_model")
        mlflow.log_param("best_feature", best_feature_df["best_feature"].values[0])
        mlflow.log_metric("best_accuracy", best_feature_df["best_accuracy"].values[0])
