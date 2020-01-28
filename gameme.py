""" Console variant of RPG Game """

import DATABASE as DB
import DRAWER as DR
import ACTIONS as ACT
import GAMESTATUS as GSTAT
import MAPPING as MAPP
import CHECKING as CH
import INVENTORY as IN
import os,time
import glob

# maps db init
DB.DRAW.maps_db = glob.glob('*.txt')
DB.DRAW.maps_names = MAPP.MAPS.read_name_space()

# frequently used functions
def screen_clearing ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

    return None

def print_stat ():
    print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])

# main initialization
set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
get_map = set_map
DB.DRAW.X_get_map = len(get_map)
DB.DRAW.Y_get_map = len(get_map[0])
DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
CH.CHECKS.check_objects()
draw_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
DR.DRAWS.final_draw (draw_map)
print_stat()
# wait for eternity or user input
#iterations = 0
while True:
    user_input = input("Next? u/d/r/l/i/e: ")
    if type(user_input) == str:
        if user_input == "u":
            screen_clearing ()
            ACT.ACTS.go_up()
            print_stat()
        elif user_input == "d":
            screen_clearing ()
            ACT.ACTS.go_down()
            print_stat()
        elif user_input == "r":
            screen_clearing ()
            ACT.ACTS.go_right()
            print_stat()
        elif user_input == "l":
            screen_clearing ()
            ACT.ACTS.go_left()
            print_stat()
        elif user_input == "e":
            screen_clearing ()
            print("---BYE---")
            exit()
        elif user_input == "i":
            screen_clearing ()
            IN.INVENTORIES.show_inventory()
            screen_clearing ()
            #CH.CHECKS.check_objects()
            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
            update_draw = DR.DRAWS.final_draw (update_map)
            print_stat()
        else:
            screen_clearing ()
            ACT.ACTS.error_handling()
            print_stat()
    else:
        screen_clearing ()
        ACT.ACTS.error_handling()
        print_stat()
