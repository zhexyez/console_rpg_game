import DATABASE as DB
import DRAWER as DR
import GAMESTATUS as GSTAT
import MAPPING as MAPP
import FIGHTING as FIGH

class ITERACTS:

    @staticmethod
    def is_iteracted (player_current, object_current, flag):
        #print(player_current, object_current)
        if object_current == 8:
            GSTAT.GAMESTATS.player_stats["money"] += 10
            return player_current, 2, False
        elif object_current == 5:
            DB.DRAW.current_map += 1
            set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
            get_map = set_map
            DB.DRAW.X_get_map = len(get_map)
            DB.DRAW.Y_get_map = len(get_map[0])
            DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
            for elem in range (0, DB.DRAW.X_get_map):
                for item in range (0, DB.DRAW.Y_get_map):
                    if DB.DRAW.get_map_points[elem][item] == 7:
                        player_current = [elem, item]
            return player_current, 2, True
        elif object_current == 9:
            if GSTAT.GAMESTATS.player_stats["hp"] > 0:
                enemy_hp_stat = 0
                enemy_power_stat = 0
                enemy_hp_stat = GSTAT.GAMESTATS.enemy_stats["hp"]
                enemy_power_stat = GSTAT.GAMESTATS.enemy_stats["power"]
                FIGH.FIGHTS.current_fight (object_current, enemy_hp_stat, enemy_power_stat)
            else:
                print("---PLEASE DONT CHEAT---")
                exit()
                
            return player_current, 2, False
        elif object_current == 10:
            if GSTAT.GAMESTATS.player_stats["hp"] > 0:
                enemy_hp_stat = 0
                enemy_power_stat = 0
                enemy_hp_stat = GSTAT.GAMESTATS.enemy_stats["hp_boss"]
                enemy_power_stat = GSTAT.GAMESTATS.enemy_stats["power_boss"]
                FIGH.FIGHTS.current_fight (object_current, enemy_hp_stat, enemy_power_stat)
            else:
                print("---PLEASE DONT CHEAT---")
                exit()
                
            return player_current, 2, False
        else:
            return player_current, object_current, False
