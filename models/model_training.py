from statsmodels.formula.api import logit

def train_models(df, features):
    """Trains logistic regression models for each feature."""
    models = []
    for col in features:
        model = logit(f"outcome ~ {col}", data=df).fit()
        models.append(model)
    return models
