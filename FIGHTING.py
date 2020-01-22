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
            print('   ' + DB.DRAW.objects_draw_grid_map[7] + ' _-= versus =-_ ' + DB.DRAW.objects_draw_grid_map[enemy] + '   ')
            print(str(GSTAT.GAMESTATS.player_stats["hp"]) + ' ' + str(GSTAT.GAMESTATS.player_stats["power"]) + ' _-= stats =-_ ' + str(enemy_hp_stat) + ' ' + str(enemy_power_stat))
            user_input = input("Attack! Or choose a power up from inventory. a/i: ")
            if user_input == "a":
                print('attacked')
                # d is less then 0 - i'm pucned
                coefficient_d = GSTAT.GAMESTATS.player_stats["power"] - enemy_power_stat
                # a is less then 0 - i punched
                coefficient_a = enemy_power_stat - GSTAT.GAMESTATS.player_stats["power"]
                if coefficient_a < 0:
                    enemy_hp_stat += coefficient_a
                    if coefficient_d < 0:
                        GSTAT.GAMESTATS.player_stats["hp"] += coefficient_d
                elif coefficient_a == 0:
                    enemy_hp_stat += coefficient_a
                    if coefficient_d < 0:
                        GSTAT.GAMESTATS.player_stats["hp"] += coefficient_d
                elif coefficient_a > 0:
                    enemy_hp_stat += 0
                    if coefficient_d < 0:
                        GSTAT.GAMESTATS.player_stats["hp"] += coefficient_d
                    
            elif user_input == "i":
                print("Nothing yet")
            else:
                print('you can not exit through the battle')
            
        FIGHTS.screen_clearing()
        # when game Menu will exist, return to game Menu
        exit()
        return None
