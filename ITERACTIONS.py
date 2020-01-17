import DATABASE as DB
import DRAWER as DR
import GAMESTATUS as GSTAT

class ITERACTS:

    @staticmethod
    def is_iteracted (player_current, object_current):
        #print(player_current, object_current)
        if object_current == 8:
            GSTAT.GAMESTATS.player_stats["money"] += 10
            return 2
        else:
            return object_current
