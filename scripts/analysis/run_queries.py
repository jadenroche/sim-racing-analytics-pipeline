import sqlite3
from pathlib import Path

# Database path
DB_FILE = Path("database/sim_racing.db")

# SQL folder
SQL_FOLDER = Path("sql")

# Connect to database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Function to run SQL file
def run_sql_file(file_name, title):
    file_path = SQL_FOLDER / file_name

    with open(file_path, "r") as file:
        query = file.read()

    print(f"\n{title}")

    cursor.execute(query)
    
    results = cursor.fetchall()

    for row in results:
        print(row)


# Run queries
run_sql_file("average_finish.sql", "Average Finish")
run_sql_file("track_performance.sql", "Track Performance")
run_sql_file("incident_analysis.sql", "Incident Analysis")


# Close connection 
conn.close()