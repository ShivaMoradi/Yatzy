import mysql.connector
db = mysql.connector.connect(

    host="localhost", user="root",
    password="mypassword", database="Yatzy"
)
cursor = db.cursor(dictionary=True)


def save_player_info(player, player_score):
    cursor.execute(f"INSERT INTO Scores (id, player, player_score)"
                   f"VALUES (NULL, '{player}', {player_score})")
    db.commit()
