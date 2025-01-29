import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load Processed Data
data = pd.read_csv("data/processed_data.csv")

# Train Recommendation Model
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text_features'])

nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
nn_model.fit(X)

# Save Model & Vectorizer
with open("model/vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

with open("model/model.pkl", "wb") as model_file:
    pickle.dump(nn_model, model_file)

print("Model training complete! 🎯")
