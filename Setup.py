import json
import Footballplayer



# creates a dictionary with all player objects
# access with player_obj_dict[0].footballplayer_name, player_obj_dict[0].update_player_matchday(1), etc
def create_footballplayer_class_objs(filename="data/database/player_database.json"):
    with open(filename) as json_file:
        data = json.load(json_file)

    player_obj_dict = {}

    for i in data:
        curr_footballplayer_id = int(i)
        curr_footballplayer_name = data[i]['footballplayer_name']
        curr_offence_pts = data[i]['offence_pts']
        curr_defence_pts = data[i]['defence_pts']
        curr_fairness = data[i]['fairness']
        curr_salary = data[i]['salary']
        curr_price = data[i]['price']

        curr_player_obj = Footballplayer.Footballplayer(curr_footballplayer_id, curr_footballplayer_name,
                                                        curr_offence_pts, curr_defence_pts,
                                                        curr_fairness, curr_salary, curr_price)

        player_obj_dict[curr_footballplayer_id] = curr_player_obj

    return player_obj_dict





# setup footballplayer
