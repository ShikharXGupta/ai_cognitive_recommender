import json
import pandas as pd # type: ignore

# Load Dataset
def load_data():
    with open('data/Dataset.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.DataFrame(data)

# Preprocess Data
def preprocess_data(data):
    data['text_features'] = data[['Activity name', 'Activity description']].apply(lambda x: ' '.join(x), axis=1)
    return data

if __name__ == "__main__":
    data = load_data()
    processed_data = preprocess_data(data)
    processed_data.to_csv("data/processed_data.csv", index=False)
    print("Data preprocessing complete! ✅")
