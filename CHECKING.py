import DATABASE as DB

class CHECKS:

    @staticmethod
    def check_objects ():
        try:
            current_map_mask = DB.DRAW.maps_db_masks[DB.DRAW.current_map+1]
            cnt = 0
            for elem in range(0, DB.DRAW.X_get_map):
                for item in range(0, DB.DRAW.Y_get_map):
                    if DB.DRAW.get_map_points[elem][item] == 8 or DB.DRAW.get_map_points[elem][item] == 9 or DB.DRAW.get_map_points[elem][item] == 10:
                        for pointer in current_map_mask:
                            if pointer["x_coord"] == elem and pointer["y_coord"] == item and pointer["was_interacted"] == 1:
                                DB.DRAW.get_map_points[elem][item] = 2
        except IndexError:
            list_of_objects = []
            
            for elem in range(0, DB.DRAW.X_get_map):
                for item in range(0, DB.DRAW.Y_get_map):
                    if DB.DRAW.get_map_points[elem][item] == 8 or DB.DRAW.get_map_points[elem][item] == 9 or DB.DRAW.get_map_points[elem][item] == 10:
                        new_objective = {
                            "x_coord": elem,
                            "y_coord": item,
                            "value": DB.DRAW.get_map_points[elem][item],
                            "was_interacted": 0
                        }
                        list_of_objects.append(new_objective)

            DB.DRAW.maps_db_masks.append(list_of_objects)
            return None

CHECKS.check_objects()
