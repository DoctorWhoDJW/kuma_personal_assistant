def load_data(file_path):
    # Load data from a specified file path
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(data):
    # Clean the data by handling missing values and duplicates
    data = data.dropna()  # Remove missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    return data

def normalize_data(data):
    # Normalize the data to a range of [0, 1]
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return normalized_data

def preprocess_data(file_path):
    # Load, clean, and normalize the data
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    normalized_data = normalize_data(cleaned_data)
    return normalized_data