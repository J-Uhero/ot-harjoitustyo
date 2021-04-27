from database_connection import database_connection

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE High_scores")
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE High_scores (id INTEGER PRIMARY KEY \
                    name TEXT, time FLOAT, hardness TEXT)")
    connection.commit()

def initialize_database():
    connection = database_connection()
    drop_tables()
    create_tables()

if __name__ == "__main__":
    initialize_database()
