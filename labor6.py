import sqlite3
import json

def convert_db_to_json(database_path, json_file_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    database_structure = {}

    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        table_structure = {}
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            table_structure[column_name] = column_type

        database_structure[table_name] = table_structure

    with open(json_file_path, 'w') as json_file:
        json.dump(database_structure, json_file, indent=4)
    conn.close()

convert_db_to_json("D:/py/lab1/Labspy/lab6.db", "D:/py/lab1/Labspy/labor6j.json")

