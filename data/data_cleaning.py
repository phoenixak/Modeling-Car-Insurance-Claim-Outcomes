def clean_data(df):
    """Cleans the dataset by filling missing values."""
    df["credit_score"].fillna(df["credit_score"].mean(), inplace=True)
    df["annual_mileage"].fillna(df["annual_mileage"].mean(), inplace=True)
    return df
