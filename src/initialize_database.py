from database_connection import database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Scores")
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Scores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            time FLOAT,
            level TEXT,
            date TIMESTAMP);
    """)

    connection.commit()

def initialize_database():
    connection = database_connection()
    drop_tables(connection)
    create_tables(connection)

