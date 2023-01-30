import pandas as pd
import os

PATH = 'Car_sales.csv'

def get_data():
    df = pd.read_csv(PATH)
    return df

