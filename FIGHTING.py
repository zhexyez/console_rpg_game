import DATABASE as DB
import GAMESTATUS as GSTAT
import os,time
import glob

class FIGHTS:

    def screen_clearing ():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system("clear")

        return None

    @staticmethod
    def current_fight (enemy, enemy_hp_stat, enemy_power_stat):
        while GSTAT.GAMESTATS.player_stats["hp"] > 0:
            if enemy_hp_stat <= 0:
                FIGHTS.screen_clearing()
                return None
            FIGHTS.screen_clearing()
            print("--- FIGHT YOUR ENEMY ---")
            print(DB.DRAW.objects_draw_grid_map[7] + ' _-= versus =-_ ' + DB.DRAW.objects_draw_grid_map[enemy])
            print(str(GSTAT.GAMESTATS.player_stats["hp"]) + ' ' + str(GSTAT.GAMESTATS.player_stats["power"]) + ' _-= powers =-_ ' + str(enemy_hp_stat) + ' ' + str(enemy_power_stat))
            user_input = input("What to choose? (attack/defence) a/d: ")
            if user_input == "a":
                print('attacked')
                GSTAT.GAMESTATS.player_stats["hp"] -= enemy_power_stat
                enemy_hp_stat -= GSTAT.GAMESTATS.player_stats["power"]
            elif user_input == "d":
                print('defenced')
                coefficient = enemy_power_stat - GSTAT.GAMESTATS.player_stats["power"]
                if coefficient < 0:
                    GSTAT.GAMESTATS.player_stats["hp"] -= GSTAT.GAMESTATS.player_stats["power"] - enemy_power_stat
            else:
                print('you can not exit through the battle')
            
        FIGHTS.screen_clearing()
        # when game Menu will exist, return to game Menu
        exit()
        return None
