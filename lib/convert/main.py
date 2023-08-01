
import pandas as pd

def load_data():
    df = pd.read_csv('dataset/predicted.csv')
    return df

if(__name__ == "__main__"):
    data = load_data()
    print(data)