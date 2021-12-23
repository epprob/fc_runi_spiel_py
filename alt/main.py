# This is a sample Python script.
import Footballplayer
import Setup

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


player_obj_dict = Setup.create_footballplayer_class_objs()

print(player_obj_dict[0].footballplayer_name)

player_obj_dict[0].update_player_matchday(1)


# import pickle
# with open('company_data.pkl', 'rb') as input:
#     company1 = pickle.load(input)
#     print(company1.footballplayer_id)
#     print(company1.footballplayer_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
