```markdown
# Cognitive Recommender System

This project is an AI-powered cognitive recommender system that suggests activities based on various criteria. The system involves data preprocessing, machine learning model training, database setup, and a Flask API that serves activity recommendations. Below are the details on how to set up, run, and interact with the system.

## Project Structure

- **/data**: Contains raw and processed datasets.
- **/model**: Contains preprocessing, training scripts, and saved models.
- **/api**: Contains API logic and database interactions.
- **/database**: Contains the SQL database initialization script.

## Steps to Set Up

### 1. Install Dependencies

First, create a `requirements.txt` file with the following contents:

```
flask
pandas
scikit-learn
psycopg2
gunicorn
```

Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

### 2. Run PostgreSQL Setup

Start PostgreSQL:

```bash
sudo service postgresql start
```

Run the SQL script to set up the database schema:

```bash
psql -U postgres -f database/init_db.sql
```

### 3. Run Data Preprocessing

Run the `preprocess_data.py` script to load and process the dataset.

```bash
python model/preprocess_data.py
```

This will load the dataset from `data/Dataset.json`, preprocess the data, and save the processed data as `data/processed_data.csv`.

### 4. Train the Machine Learning Model

Run the `train_model.py` script to train the recommendation model using TF-IDF and Nearest Neighbors.

```bash
python model/train_model.py
```

This will train the model and save the vectorizer and trained model to the `model` folder.

### 5. Run the Flask API

Run the Flask API server using the following command:

```bash
python api/app.py
```

The API will be accessible at `http://127.0.0.1:5000/`.

### 6. Use the API

- **Get Recommendations**: 
  Send a GET request to `/recommend` with the following optional query parameters:
  - `category`: Category filter (e.g., `Yes` or `No` for different categories).
  - `zone`: Zone filter (e.g., `Zone A`, `Zone B`, etc.).
  - `age_range`: Age range filter (e.g., `10-15`, `16-20`, etc.).

  Example:

  ```bash
  curl "http://127.0.0.1:5000/recommend?category=Yes&zone=Zone A&age_range=10-15"
  ```

- **Health Check**: 
  To check if the API is running, send a GET request to `/health`.

  Example:

  ```bash
  curl "http://127.0.0.1:5000/health"
  ```

  The API will return `{"status": "API is running"}` if everything is working fine.

## Project Overview

### 1️⃣ **Data Preprocessing** (`preprocess_data.py`)

- Loads and processes the dataset.
- Combines the `Activity name` and `Activity description` columns to create text features for the model.
- Saves the processed data as a CSV file.

### 2️⃣ **Train Machine Learning Model** (`train_model.py`)

- Trains a recommendation model using TF-IDF and Nearest Neighbors.
- Saves the trained model and vectorizer for later use in the Flask API.

### 3️⃣ **PostgreSQL Database Setup** (`init_db.sql`)

- Creates a PostgreSQL database (`cognitive_db`) and the `activities` table to store activity information.

### 4️⃣ **Database Handler** (`database.py`)

- Handles database connections and inserting activities into the PostgreSQL database.

### 5️⃣ **Flask API** (`app.py`)

- Exposes a REST API to recommend activities based on user queries.
- Provides a health check endpoint for ensuring the API is running.

## Deployment Instructions

1. Install dependencies using `pip install -r requirements.txt`.
2. Set up PostgreSQL and run the database initialization script.
3. Preprocess the data and train the machine learning model.
4. Run the Flask API server to serve recommendations.
