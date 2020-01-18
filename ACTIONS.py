import DATABASE as DB
import DRAWER as DR
import os
import ITERACTIONS as ITER
import GAMESTATUS as GSTAT

class ACTS:

    @staticmethod
    def go_right ():
        for elem in range (0, DB.DRAW.X_get_map):
            for item in range (0, DB.DRAW.Y_get_map):
                if DB.DRAW.get_map_points[elem][item] == 7:
                    if DB.DRAW.get_map_points[elem][item+1] == 1 or DB.DRAW.get_map_points[elem][item+1] == 3 or DB.DRAW.get_map_points[elem][item+1] == 6:
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        #print("---U CAN NOT GO RIGHT HERE---")
                        return None
                    else:
                        isit = True
                        pl_current, iteracted, flag = ITER.ITERACTS.is_iteracted(DB.DRAW.get_map_points[elem][item], DB.DRAW.get_map_points[elem][item+1], isit)
                        if flag == False:
                            DB.DRAW.get_map_points[elem][item] = iteracted
                            DB.DRAW.get_map_points[elem][item+1] = 7
                        
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        return None

    @staticmethod
    def go_left ():
        for elem in range (0, DB.DRAW.X_get_map):
            for item in range (0, DB.DRAW.Y_get_map):
                if DB.DRAW.get_map_points[elem][item] == 7:
                    if DB.DRAW.get_map_points[elem][item-1] == 1 or DB.DRAW.get_map_points[elem][item-1] == 3 or DB.DRAW.get_map_points[elem][item-1] == 6:
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        #print("---U CAN NOT GO LEFT HERE---")
                        return None
                    else:
                        isit = True
                        pl_current, iteracted, flag = ITER.ITERACTS.is_iteracted(DB.DRAW.get_map_points[elem][item], DB.DRAW.get_map_points[elem][item-1], isit)
                        if flag == False:
                            DB.DRAW.get_map_points[elem][item] = iteracted
                            DB.DRAW.get_map_points[elem][item-1] = 7
                            
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        return None
        

    @staticmethod
    def go_down ():
        for elem in range (0, DB.DRAW.X_get_map):
            for item in range (0, DB.DRAW.Y_get_map):
                if DB.DRAW.get_map_points[elem][item] == 7:
                    try:
                        t = DB.DRAW.get_map_points[elem+1]
                        if DB.DRAW.get_map_points[elem+1][item] == 1 or DB.DRAW.get_map_points[elem+1][item] == 3 or DB.DRAW.get_map_points[elem+1][item] == 6:
                            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            #print("---U CAN NOT GO DOWN HERE---")
                            return None
                        else:
                            isit = True
                            pl_current, iteracted, flag = ITER.ITERACTS.is_iteracted(DB.DRAW.get_map_points[elem][item], DB.DRAW.get_map_points[elem+1][item], isit)
                            if flag == False:
                                DB.DRAW.get_map_points[elem][item] = iteracted
                                DB.DRAW.get_map_points[elem+1][item] = 7
                                
                            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            return None
                    except IndexError:
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        #print("---U CAN NOT GO DOWN HERE---")
                        return None

    @staticmethod
    def go_up ():
        for elem in range (0, DB.DRAW.X_get_map):
            for item in range (0, DB.DRAW.Y_get_map):
                if DB.DRAW.get_map_points[elem][item] == 7:
                    if elem == 0:
                        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        #print("---U CAN NOT GO UP HERE---")
                        return None
                    else:
                        if DB.DRAW.get_map_points[elem-1][item] == 1 or DB.DRAW.get_map_points[elem-1][item] == 3 or DB.DRAW.get_map_points[elem-1][item] == 6:
                            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            #print("---U CAN NOT GO UP HERE---")
                            return None
                        else:
                            isit = True
                            pl_current, iteracted, flag = ITER.ITERACTS.is_iteracted(DB.DRAW.get_map_points[elem][item], DB.DRAW.get_map_points[elem-1][item], isit)
                            if flag == False:
                                DB.DRAW.get_map_points[elem][item] = iteracted
                                DB.DRAW.get_map_points[elem-1][item] = 7
                                
                            update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            return None

    @staticmethod
    def error_handling():
        update_map = DR.DRAWS.map_objects_analyze (DB.DRAW.get_map_points)
        update_draw = DR.DRAWS.final_draw (update_map)
        #print("---TRY TO ENTER A VALID VALUE---")
        return None
