import os
import pickle
import pandas as pd
from models.kuma_model import KumaModel
from src.data_preprocessing import preprocess_data

def train_model(data_path, model_save_path):
    # Load processed data
    data = pd.read_csv(data_path)
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Initialize the Kuma model
    model = KumaModel()
    
    # Train the model
    model.fit(X, y)
    
    # Save the trained model
    with open(model_save_path, 'wb') as model_file:
        pickle.dump(model, model_file)
    
    print("Model training complete and saved to:", model_save_path)

if __name__ == "__main__":
    # Define paths
    processed_data_path = os.path.join('data', 'processed', 'processed_data.csv')
    model_save_path = os.path.join('models', 'kuma_model.pkl')
    
    # Train the model
    train_model(processed_data_path, model_save_path)