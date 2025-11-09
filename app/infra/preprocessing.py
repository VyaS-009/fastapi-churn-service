import pandas as pd

NUM_COLS = ["tenure", "MonthlyCharges", "TotalCharges"]
CAT_COLS = ["Contract", "InternetService", "OnlineSecurity", "TechSupport", "PaymentMethod"]

def preprocess_single(payload: dict, x_columns, scaler):
    df = pd.DataFrame([payload])
    # One-hot encode using train-time structure:
    df_num = df[NUM_COLS]
    df_cat = pd.get_dummies(df[CAT_COLS], drop_first=True)
    X = pd.concat([df_num, df_cat], axis=1)
    X = X.reindex(columns=x_columns, fill_value=0)
    X_scaled = scaler.transform(X)
    return X_scaled

def preprocess_batch(df: pd.DataFrame, x_columns, scaler):
    df_num = df[NUM_COLS]
    df_cat = pd.get_dummies(df[CAT_COLS], drop_first=True)
    X = pd.concat([df_num, df_cat], axis=1)
    X = X.reindex(columns=x_columns, fill_value=0)
    X_scaled = scaler.transform(X)
    return X_scaled
