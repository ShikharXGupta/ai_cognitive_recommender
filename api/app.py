import pickle
import pandas as pd # type: ignore
from flask import Flask, request, jsonify # type: ignore

# Load Model and Vectorizer
with open("model/vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

with open("model/model.pkl", "rb") as model_file:
    nn_model = pickle.load(model_file)

# Load Data
data = pd.read_csv("data/processed_data.csv")

# Flask App
app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend_activity():
    category = request.args.get('category', None)
    zone = request.args.get('zone', None)
    age_range = request.args.get('age_range', None)

    # Filter Data
    filtered_data = data.copy()

    # Check if category exists in dataset columns before filtering
    if category:
        if category in filtered_data.columns:
            filtered_data = filtered_data[filtered_data[category] == 'Yes']
        else:
            return jsonify({"error": f"Category '{category}' not found in dataset"}), 400

    if zone:
        filtered_data = filtered_data[filtered_data['Zone'].str.lower() == zone.lower()]
    if age_range:
        filtered_data = filtered_data[filtered_data['Age'] == age_range]

    if filtered_data.empty:
        return jsonify({"message": "No activities found matching criteria."}), 404

    random_activity = filtered_data.sample(n=1).iloc[0]

    return jsonify({
        "name": random_activity['Activity name'],
        "description": random_activity['Activity description'],
        "instructions": "Follow the activity as described.",
        "materials_required": "None",
        "time_required": random_activity['Time'],
        "zone": random_activity['Zone'],
        "objective": "Enhance cognitive abilities."
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"})

if __name__ == '__main__':
    app.run(debug=True)
