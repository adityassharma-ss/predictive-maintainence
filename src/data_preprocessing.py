import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data_path):
    data = pd.read_csv(data_path)
    data = data.fillna(method='ffill')
    scaler = MinMaxScaler()
    data[['temp', 'vibration', 'pressure', 'rpm', 'load']] = scaler.fit_transform(data[['temp', 'vibration', 'pressure', 'rpm', 'load']])
    return data, scaler