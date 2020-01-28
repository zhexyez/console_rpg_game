import DATABASE as DB
import GAMESTATUS as GSTAT
import pickle

class SAVESLOADS:

    @staticmethod
    def save ():
        main_list = []
        main_list.append(DB.DRAW.current_map)
        main_list.append(DB.DRAW.maps_db_masks)
        main_list.append(GSTAT.GAMESTATS.player_stats)
        main_list.append(GSTAT.GAMESTATS.inventory)
        """
        ### If it needed to remember player position - use lines below ###
        for elem in range (0, DB.DRAW.get_map_points):
            for item in range (0, DB.DRAW.get_map_points):
                if DB.DRAW.get_map_points[elem][item] == 7:
                    main_list.append([elem,item])
                    break
        """
        with open('save.txt', 'wb') as savefile:
            pickle.dump(main_list, savefile)
        return None        

    @staticmethod
    def load ():
        with open('save.txt', 'rb') as savefile:
            loaded_list = pickle.load(savefile)
            if len(loaded_list) == 0:
                return None
            DB.DRAW.current_map = loaded_list[0]
            DB.DRAW.maps_db_masks = loaded_list[1]
            GSTAT.GAMESTATS.player_stats = loaded_list[2]
            GSTAT.GAMESTATS.inventory = loaded_list[3]
        return None
