CREATE DATABASE cognitive_db;

\c cognitive_db

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    instructions TEXT NOT NULL,
    materials TEXT NOT NULL,
    time_required TEXT NOT NULL,
    zone TEXT NOT NULL,
    objective TEXT NOT NULL
);
