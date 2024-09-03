import pandas as pd
import numpy as np
from statsmodels.formula.api import logit
# Load the dataset
cars = pd.read_csv('car_insurance.csv')

# Examine the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Fill missing values with the mean
cars["credit_score"].fillna(cars["credit_score"].mean(), inplace=True)
cars["annual_mileage"].fillna(cars["annual_mileage"].mean(), inplace=True)

# Initialize an empty list to store model results
models = []

# Define feature columns by dropping the 'id' and 'outcome' columns
features = cars.drop(columns=["id", "outcome"]).columns

# Loop through each feature to create and fit a logistic regression model
for col in features:
    # Create a logistic regression model for the current feature
    model = logit(f"outcome ~ {col}", data=cars).fit()
    # Append the model to the list of models
    models.append(model)

# Initialize an empty list to store accuracies
accuracies = []

# Loop through each model to compute its accuracy
for model in models:
    # Compute the confusion matrix
    conf_matrix = model.pred_table()
    # Calculate accuracy using the confusion matrix
    acc = (conf_matrix[0,0] + conf_matrix[1,1]) / (conf_matrix[0,0] + conf_matrix[1,1] + conf_matrix[1,0] + conf_matrix[0,1])
    # Append the accuracy to the list of accuracies
    accuracies.append(acc)

# Find the index of the feature with the highest accuracy
best_feature_index = accuracies.index(max(accuracies))

# Retrieve the best feature name using the index
best_feature = features[best_feature_index]

# Create a DataFrame to store the best feature and its corresponding accuracy
best_feature_df = pd.DataFrame({"best_feature": [best_feature],
                                "best_accuracy": [max(accuracies)]},
                                index=[0])

# Print the DataFrame containing the best feature and its accuracy
print(best_feature_df)
