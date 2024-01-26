import numpy as np
import databas
import random


class Yatzy:
    def __init__(self, player, player_score):
        self.player = np.array(player)
        self.player_score = np.array(player_score)

    def start(self):
        game_running = True
        rounds_played = 0
        players = []

        while game_running:
            rounds_played += 1
            print(f"you are in round: {rounds_played}")
            dic_rolls = np.array([])
            for i in range(5):
                cast_dice = random.randint(1, 6)
                dic_rolls = np.append(dic_rolls, cast_dice)
                answer = input("Do you want to save the score? y/n")
                if answer == "y":
                    self.player_score = np.sum(dic_rolls)
                    databas.save_player_info(player=self.player, player_score=self.player_score)
                    break
                elif answer.lower() == "n":
                    print(f"Roll again: {dic_rolls}")
        self.check_currecnt_status(players)
        play_again = input("Do you want to play again? y/n")
        if play_again.lower() != "y":
            game_running = False

    def check_currecnt_status(self, players):
        print("\nCurrent Standings:")
        for player_info in players:
            player, player_score = player_info
            print(f"Player: {player}, Total Score: {player_score}")

        # Determine last and first place
        sorted_players = sorted(players, key=lambda x: x[1])
        last_place, first_place = sorted_players[0], sorted_players[-1]

        print(f"\nLast Place: Player {last_place[0]} with score {last_place[1]}")
        print(f"First Place: Player {first_place[0]} with score {first_place[1]}")

    if __name__ == "__main__":
        players = []

        # Add players dynamically
        num_players = int(input("Enter the number of players: "))
        for _ in range(num_players):
            player_name = input("Enter player name: ")
            players.append((player_name, 0))


yatzy_instance = Yatzy(player="", player_score=0)
yatzy_instance.start()
