import DATABASE as DB
import DRAWER as DR
import ACTIONS as ACT
import GAMESTATUS as GSTAT
import MAPPING as MAPP
import os,time

def screen_clearing ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")

    return None

set_map = MAPP.MAPS.read_map("lvl_second.txt")
get_map = set_map
X_get_map = len(get_map)
Y_get_map = len(get_map[0])
get_map_points = DR.DRAWS.map_analyzer (get_map, X_get_map, Y_get_map)
#print(get_map_points)
draw_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
#print(draw_map)
DR.DRAWS.final_draw (draw_map)
print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
i = 0
while i < 100000:
    user_input = input("Next? u/d/r/l/e: ")
    if type(user_input) == str:
        if user_input == "u":
            screen_clearing ()
            print("---UPDATE---")
            ACT.ACTS.go_up(get_map_points, X_get_map, Y_get_map)
            print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
        elif user_input == "d":
            screen_clearing ()
            print("---UPDATE---")
            ACT.ACTS.go_down(get_map_points, X_get_map, Y_get_map)
            print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
        elif user_input == "r":
            screen_clearing ()
            print("---UPDATE---")
            ACT.ACTS.go_right(get_map_points, X_get_map, Y_get_map)
            print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
        elif user_input == "l":
            screen_clearing ()
            print("---UPDATE---")
            ACT.ACTS.go_left(get_map_points, X_get_map, Y_get_map)
            print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
        elif user_input == "e":
            screen_clearing ()
            print("---BYE---")
            exit()
        else:
            screen_clearing ()
            print("---UPDATE---")
            ACT.ACTS.error_handling(get_map_points, X_get_map, Y_get_map)
            print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
    else:
        screen_clearing ()
        print("---UPDATE---")
        ACT.ACTS.error_handling(get_map_points, X_get_map, Y_get_map)
        print("money: ", GSTAT.GAMESTATS.player_stats["money"], " hp: ", GSTAT.GAMESTATS.player_stats["hp"], " power ", GSTAT.GAMESTATS.player_stats["power"])
