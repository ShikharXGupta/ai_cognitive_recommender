import psycopg2 # type: ignore

DB_CONFIG = {
    "dbname": "cognitive_db",
    "user": "[username]",
    "password": "[Password]",
    "host": "localhost",
    "port": "[Postgresql port]"
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def insert_activity(activity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activities (name, description, instructions, materials, time_required, zone, objective)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (activity['name'], activity['description'], "Follow the activity as described.", "None", activity['time_required'], activity['zone'], "Enhance cognitive abilities."))
    
    conn.commit()
    cursor.close()
    conn.close()
