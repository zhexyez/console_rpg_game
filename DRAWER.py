import DATABASE as DB

class DRAWS:

    @staticmethod
    def map_analyzer (get_map, X_get_map, Y_get_map):
        analyzed = [[0 for x in range(Y_get_map)] for y in range(X_get_map)]
        for elem in range (0, len(get_map)):
            for item in range (0, len(get_map[elem])):
                if get_map[elem][item] == DB.DRAW.objects_draw_grid_map[1]:
                    analyzed[elem][item] = 1
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[2]:
                    analyzed[elem][item] = 2
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[3]:
                    analyzed[elem][item] = 3
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[4]:
                    analyzed[elem][item] = 4
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[5]:
                    analyzed[elem][item] = 5
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[6]:
                    analyzed[elem][item] = 6
                elif get_map[elem][item] == DB.DRAW.objects_draw_grid_map[7]:
                    analyzed[elem][item] = 7
        return(analyzed)

    @staticmethod
    def map_objects_analyze (get_map, X_get_map, Y_get_map):
        draw_array = []
        for elem in range (0, len(get_map)):
            wordTo = ""
            for item in range (0, len(get_map[elem])):
                wordTo += DB.DRAW.objects_draw_grid_map[get_map[elem][item]]

            draw_array.append(wordTo)

        return draw_array

    @staticmethod
    def final_draw (draw_map):
        for x in range (0, len(draw_map)):
            print(draw_map[x])
            
