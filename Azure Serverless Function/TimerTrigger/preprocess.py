import pandas as pd
def preprocess_data(df):
    df["timestamp"] = pd.to_datetime(df["time"])
    df['Time'] = pd.to_datetime(df["time"])
    df['Date'] = df['timestamp'].dt.date
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d-%m-%Y').astype(str)
    df['Day'] = df['timestamp'].dt.day_name()
    df["Hour"] = df["timestamp"].dt.hour
    return df