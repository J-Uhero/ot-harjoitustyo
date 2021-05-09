from database_connection import database_connection
from entities.score import Score

def give_score_object(row):
    return Score(row["name"], row["time"], row["level"], row["date"])

class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_score(self, name, time, level, date):
        cursor = self._connection.cursor()
        cursor.execute("""
            INSERT INTO Scores (name, time, level, date) 
                VALUES (?, ?, ?, ?);
            """, [name, time, level, date])

        self._connection.commit()

    def find_score_by_name(self, name):
        cursor = self._connection.cursor()
        scores = cursor.execute("""
            SELECT * 
                FROM Scores WHERE nimi=? 
                GROUP BY id 
                ORDER BY date;
        """, [name]).fetchall()

        return list(map(give_score_object, scores))

    def find_high_scores_by_level(self, level, quantity):
        cursor = self._connection
        scores = cursor.execute("""
            SELECT *
                FROM Scores 
                WHERE level=? 
                GROUP BY id 
                ORDER BY time
                LIMIT ?
        """, [level, quantity]).fetchall()

        return list(map(give_score_object, scores))

    def check_ranking_of_a_score(self, time, level):
        cursor = self._connection
        ranking = cursor.execute("""
            SELECT COUNT(id)
                FROM Scores
                WHERE level=?
                AND time <= ?
        """, [level, time]).fetchone()

        return ranking


connection = database_connection()
score_repository = ScoreRepository(connection)
