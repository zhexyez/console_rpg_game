import DATABASE as DB
import DRAWER as DR
import GAMESTATUS as GSTAT
import MAPPING as MAPP
import FIGHTING as FIGH
import copy

class ITERACTS:

    @staticmethod
    def is_iteracted (player_current, object_current, current_X_position, flag):
        #print(player_current, object_current)
        if object_current == 8:
            # object is "o" coin/money
            GSTAT.GAMESTATS.player_stats["money"] += 10
            return player_current, 2, current_X_position, False
        
        elif object_current == 5:
            # object is ":" door
            Y_get_map_copy = copy.deepcopy(DB.DRAW.Y_get_map)
            is_odd_or_even = (Y_get_map_copy % 2)
            # if even
            if is_odd_or_even == 0:
                elth = (Y_get_map_copy / 2) - 1
                even_less_than_half = int(elth)
                emth = (Y_get_map_copy / 2) + 2
                even_more_than_half = int(emth)
                
                if current_X_position <= even_less_than_half:
                    DB.DRAW.current_map -= 1
                    set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
                    get_map = set_map
                    DB.DRAW.X_get_map = len(get_map)
                    DB.DRAW.Y_get_map = len(get_map[0])
                    DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
                    return player_current, 2, current_X_position, True
                
                elif current_X_position >= even_more_than_half:
                    DB.DRAW.current_map += 1
                    set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
                    get_map = set_map
                    DB.DRAW.X_get_map = len(get_map)
                    DB.DRAW.Y_get_map = len(get_map[0])
                    DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
                    return player_current, 2, current_X_position, True
            # if odd
            else:
                rounded_float = round(Y_get_map_copy/2)
                if current_X_position <= rounded_float:
                    DB.DRAW.current_map -= 1
                    set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
                    get_map = set_map
                    DB.DRAW.X_get_map = len(get_map)
                    DB.DRAW.Y_get_map = len(get_map[0])
                    DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
                    return player_current, 2, current_X_position, True
                elif current_X_position >= (rounded_float + 2):
                    DB.DRAW.current_map += 1
                    set_map = MAPP.MAPS.read_map(DB.DRAW.maps_db[DB.DRAW.current_map])
                    get_map = set_map
                    DB.DRAW.X_get_map = len(get_map)
                    DB.DRAW.Y_get_map = len(get_map[0])
                    DB.DRAW.get_map_points = DR.DRAWS.map_analyzer (get_map)
                    return player_current, 2, current_X_position, True
                
        elif object_current == 9:
            # object is "E" enemy
            if GSTAT.GAMESTATS.player_stats["hp"] > 0:
                enemy_hp_stat = 0
                enemy_power_stat = 0
                enemy_hp_stat = GSTAT.GAMESTATS.enemy_stats["hp"]
                enemy_power_stat = GSTAT.GAMESTATS.enemy_stats["power"]
                FIGH.FIGHTS.current_fight (object_current, enemy_hp_stat, enemy_power_stat)
            else:
                print("---PLEASE DONT CHEAT---")
                exit()
                
            return player_current, 2, current_X_position, False
        elif object_current == 10:
            # object is "B" boss
            if GSTAT.GAMESTATS.player_stats["hp"] > 0:
                enemy_hp_stat = 0
                enemy_power_stat = 0
                enemy_hp_stat = GSTAT.GAMESTATS.enemy_stats["hp_boss"]
                enemy_power_stat = GSTAT.GAMESTATS.enemy_stats["power_boss"]
                FIGH.FIGHTS.current_fight (object_current, enemy_hp_stat, enemy_power_stat)
            else:
                print("---PLEASE DONT CHEAT---")
                exit()
                
            return player_current, 2, current_X_position, False
        else:
            return player_current, object_current, current_X_position, False
