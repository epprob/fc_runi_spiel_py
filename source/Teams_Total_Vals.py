

class Teams_Total_Vals(object):

    def __init__(self):

        self.wp = 0.
        self.nd = 0.
        self.team_name = "None"

        self.punkte = 0
        self.tore_geschossen = 0
        self.tore_erhalten = 0

    def update_wp(self, wp):

        self.wp = wp

    def update_nd(self, nd):

        self.nd = nd

    def update_team_name(self, name):

        self.team_name = name

    def reset_season_stats(self):
        self.punkte = 0
        self.tore_geschossen = 0
        self.tore_erhalten = 0

    def update_season_stats(self, goals_scored, goals_received):

        if goals_scored > goals_received:
            self.punkte += 3
        elif goals_scored < goals_received:
            pass
        else:
            self.punkte += 1