import numpy as np
import databas
import random

Player_scores = {'player': '<player>', 'player_score': '<player_score>'}


class Yatzy:
    def __init__(self, player, player_score):
        self.player = np.array(player)
        self.player_score = np.array(player_score)

    def start(self):
        game_running = True
        while game_running:
            self.player = input("Enter player name: ")
            self.player_score = 0
            print("current score for the player is: ", self.player_score)
            dic_rolls = np.array([])
            for i in range(5):
                cast_dice = random.randint(1, 6)
                dic_rolls.append(cast_dice)
                answer = input("Do you want to save the score? y/n")
                if answer == "y":
                    self.player_score = np.sum(dic_rolls)
                    databas.save_player_info(player=self.player, player_score=self.player_score)
                    break
                elif answer.lower() == "n":
                    print("Roll again:", dic_rolls)
            game_running = False


yatzy_instance = Yatzy(player=Player_scores['player'], player_score=Player_scores['player_score'])
yatzy_instance.start()
