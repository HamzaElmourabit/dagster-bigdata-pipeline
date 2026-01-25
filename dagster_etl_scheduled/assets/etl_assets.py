import pandas as pd
from dagster import asset

@asset
def load_data():
    df = pd.read_csv("input.csv")
    print("Data loaded:\n", df.head())
    return df

@asset
def transform_data(load_data):
    df = load_data.copy()
    df["total"] = df["quantity"] * df["price"]
    print("Data transformed:\n", df.head())
    return df

@asset
def save_data(transform_data):
    df = transform_data
    df.to_csv("output.csv", index=False)
    print("Data saved to output.csv")
    return "Success"

