import mysql.connector

db = mysql.connector.connect(

    host="localhost", user="root",
    password="mypassword", database="E-handelSystem"
)
cursor = db.cursor(dictionary=True)


def save_player_info(player, player_score):
    cursor.execute(f"INSERT INTO players (player, player_score)"
                   f"VALUES ('{player}', '{player_score}')")
    db.commit()
