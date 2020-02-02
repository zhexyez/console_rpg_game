""" Console variant of RPG Game """

import DATABASE as DB
import DRAWER as DR
import ACTIONS as ACT
import GAMESTATUS as GSTAT
import MAPPING as MAPP
import CHECKING as CH
import INVENTORY as IN
import SAVELOAD as SL
import os,time
import glob
import keyboard

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
    print("lvl: ", GSTAT.GAMESTATS.player_stats["lvl"], " exp: ", GSTAT.GAMESTATS.player_stats["exp"])
    print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
    
# menu
def menu ():
    screen_clearing()
    print("\t-= RPG GAME =-")
    print("\n")
    print("-= New Game (n) or Load Game (l) =-")
    print("\n")
    menu_input = input("-> ")
    if menu_input == "n":
        GSTAT.GAMESTATS.player_stats["money"] = 0
        GSTAT.GAMESTATS.player_stats["hp"] = 100
        GSTAT.GAMESTATS.player_stats["exp"] = 0
        GSTAT.GAMESTATS.player_stats["lvl"] = 1
        GSTAT.GAMESTATS.player_stats["power"] = 10
        GSTAT.GAMESTATS.enemy_stats["hp"] = 50
        GSTAT.GAMESTATS.enemy_stats["power"] = 5
        GSTAT.GAMESTATS.enemy_stats["hp_boss"] = 300
        GSTAT.GAMESTATS.enemy_stats["power_boss"] = 20
        screen_clearing()
        return None
    elif menu_input == "l":
        screen_clearing()
        SL.SAVESLOADS.load()
        return None
    else:
        menu()

menu()
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
# main loop
while True:
    user_input = input("Next? w-a-s-d/i-inventory/q-save/e-exit: ")
    if type(user_input) == str:
        if user_input == "w":
            screen_clearing ()
            ACT.ACTS.go_up()
            print_stat()
        elif user_input == "s":
            screen_clearing ()
            ACT.ACTS.go_down()
            print_stat()
        elif user_input == "d":
            screen_clearing ()
            ACT.ACTS.go_right()
            print_stat()
        elif user_input == "a":
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
            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
            update_draw = DR.DRAWS.final_draw (update_map)
            print_stat()
        elif user_input == "q":
            SL.SAVESLOADS.save()
            screen_clearing ()
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
