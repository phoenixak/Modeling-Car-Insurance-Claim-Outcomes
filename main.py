from data.data_loader import load_data
from data.data_cleaning import clean_data
from models.model_training import train_models
from models.model_evaluation import evaluate_models
from utils.logger import setup_logger
from utils.mlflow_tracking import log_model_to_mlflow

def main():
    logger = setup_logger()

    # Load data
    logger.info("Loading data...")
    file_path = "dataset\car_insurance.csv"
    cars = load_data(file_path)

    # Clean data
    logger.info("Cleaning data...")
    cars = clean_data(cars)

    # Define feature columns by dropping 'id' and 'outcome'
    features = cars.drop(columns=["id", "outcome"]).columns

    # Train models
    logger.info("Training models...")
    models = train_models(cars, features)

    # Evaluate models
    logger.info("Evaluating models...")
    best_feature_df = evaluate_models(models, features)
    logger.info(f"Best Feature: {best_feature_df['best_feature'].values[0]}, Best Accuracy: {best_feature_df['best_accuracy'].values[0]}")

    # Log best model to MLflow
    log_model_to_mlflow(models[best_feature_df.index[0]], best_feature_df)

if __name__ == "__main__":
    main()
