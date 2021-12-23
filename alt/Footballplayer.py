# import numpy as np
import pickle


class Footballplayer(object):
    def __init__(self, footballplayer_id, footballplayer_name, wp_offense, wp_defense, fairness, salary, price):

        self.footballplayer_id = footballplayer_id
        self.footballplayer_name = footballplayer_name

        self.wp_offence = wp_offense
        self.wp_defense = wp_defense
        self.fairness = fairness
        self.salary = salary
        self.price = price

        self.health = True
        self.suspension_days = 0

        self.gamer_id = -1
        self.gamer_id_history = []

        self.transfer_price_history = []

        self.nr_games_career = 0
        self.nr_wins_career = 0
        self.nr_losses_career = 0
        self.nr_draws_career = 0
        self.nr_suspension_days_career = 0

    def update_player_transfer(self, gamer_id, transfer_price):
        self.gamer_id = gamer_id
        self.gamer_id_history.append(gamer_id)
        self.transfer_price_history.append(transfer_price)

    def set_suspension(self, suspension_days):
        if suspension_days > self.suspension_days:
            suspension_days_old = self.suspension_days  # tmp store old number of days

            self.health = False
            self.suspension_days += (suspension_days - suspension_days_old)
            self.nr_suspension_days_career += (suspension_days - suspension_days_old)

    def return_name(self):
        return self.footballplayer_name

    def update_player_matchday(self, result):
        # update play history

        if self.health:
            if result == 1:
                self.nr_wins_career += 1
            elif result == 0:
                self.nr_draws_career += 1
            elif result == -1:
                self.nr_losses_career += 1
            else:
                print("Todo fehlermeldung...")

            self.nr_games_career +=1

        # update health
        if self.suspension_days > 0:
            self.suspension_days -= 1

        if self.suspension_days == 0:
            self.health = True

    def write(self, save_point):

        filepath = "data/runtime_output/player/"+str(save_point)+"_pl"+str(self.footballplayer_id)+".pkl"

        with open(filepath, 'wb') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)


