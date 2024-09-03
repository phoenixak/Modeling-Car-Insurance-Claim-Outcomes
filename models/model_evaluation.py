import numpy as np
import pandas as pd

def evaluate_models(models, features):
    """Evaluates the accuracy of each logistic regression model."""
    accuracies = []
    for model in models:
        conf_matrix = model.pred_table()
        acc = (conf_matrix[0, 0] + conf_matrix[1, 1]) / np.sum(conf_matrix)
        accuracies.append(acc)

    best_feature_index = accuracies.index(max(accuracies))
    best_feature = features[best_feature_index]

    best_feature_df = pd.DataFrame({"best_feature": [best_feature],
                                    "best_accuracy": [max(accuracies)]},
                                    index=[0])
    return best_feature_df
