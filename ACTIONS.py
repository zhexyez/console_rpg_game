import DATABASE as DB
import DRAWER as DR
import os
import ITERACTIONS as ITER
import GAMESTATUS as GSTAT

class ACTS:

    @staticmethod
    def go_right (get_map_points, X_get_map, Y_get_map):
        for elem in range (0, X_get_map):
            for item in range (0, Y_get_map):
                if get_map_points[elem][item] == 7:
                    if get_map_points[elem][item+1] == 1 or get_map_points[elem][item+1] == 3 or get_map_points[elem][item+1] == 6:
                        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        print("---U CAN NOT GO RIGHT HERE---")
                        return None
                    else:
                        iteracted = ITER.ITERACTS.is_iteracted(get_map_points[elem][item], get_map_points[elem][item+1])
                        get_map_points[elem][item] = iteracted
                        get_map_points[elem][item+1] = 7
                        break

        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
        update_draw = DR.DRAWS.final_draw (update_map)

    @staticmethod
    def go_left (get_map_points, X_get_map, Y_get_map):
        for elem in range (0, X_get_map):
            for item in range (0, Y_get_map):
                if get_map_points[elem][item] == 7:
                    if get_map_points[elem][item-1] == 1 or get_map_points[elem][item-1] == 3 or get_map_points[elem][item-1] == 6:
                        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        print("---U CAN NOT GO LEFT HERE---")
                        return None
                    else:
                        iteracted = ITER.ITERACTS.is_iteracted(get_map_points[elem][item], get_map_points[elem][item-1])
                        get_map_points[elem][item] = iteracted
                        get_map_points[elem][item-1] = 7
                        break
        
        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
        update_draw = DR.DRAWS.final_draw (update_map)

    @staticmethod
    def go_down (get_map_points, X_get_map, Y_get_map):
        for elem in range (0, X_get_map):
            for item in range (0, Y_get_map):
                if get_map_points[elem][item] == 7:
                    try:
                        t = get_map_points[elem+1]
                        if get_map_points[elem+1][item] == 1 or get_map_points[elem+1][item] == 3 or get_map_points[elem+1][item] == 6:
                            update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            print("---U CAN NOT GO DOWN HERE---")
                            return None
                        else:
                            iteracted = ITER.ITERACTS.is_iteracted(get_map_points[elem][item], get_map_points[elem+1][item])
                            get_map_points[elem][item] = iteracted
                            get_map_points[elem+1][item] = 7        
                            update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            return None
                    except IndexError:
                        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        print("---U CAN NOT GO DOWN HERE---")
                        break

    @staticmethod
    def go_up (get_map_points, X_get_map, Y_get_map):
        for elem in range (0, X_get_map):
            for item in range (0, Y_get_map):
                if get_map_points[elem][item] == 7:
                    if elem == 0:
                        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                        update_draw = DR.DRAWS.final_draw (update_map)
                        print("---U CAN NOT GO UP HERE---")
                        return None
                    else:
                        if get_map_points[elem-1][item] == 1 or get_map_points[elem-1][item] == 3 or get_map_points[elem-1][item] == 6:
                            update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            print("---U CAN NOT GO UP HERE---")
                            return None
                        else:
                            iteracted = ITER.ITERACTS.is_iteracted(get_map_points[elem][item], get_map_points[elem-1][item])
                            get_map_points[elem][item] = iteracted
                            get_map_points[elem-1][item] = 7         
                            update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
                            update_draw = DR.DRAWS.final_draw (update_map)
                            return None

    @staticmethod
    def error_handling(get_map_points, X_get_map, Y_get_map):
        update_map = DR.DRAWS.map_objects_analyze (get_map_points, X_get_map, Y_get_map)
        update_draw = DR.DRAWS.final_draw (update_map)
        print("---TRY TO ENTER A VALID VALUE---")
