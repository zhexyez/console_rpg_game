class DRAW:
    # objects values
    objects_draw_grid_map = {
        1: ' ',
        2: '.',
        3: '|',
        4: '_',
        5: ':',
        6: '-',
        7: '&',
        8: 'o',
        9: 'E',
        10: 'B',
        11: 'T',
        12: '^'
    }

    # maps
    map_zero =[
         [' ','&','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','o','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' '],
         [' ','.','.','.','o','.','.','.',' ',' '],
         [' ','.','.','.','.','.','.','.',' ',' ']
        ]

    maps_db = []
    maps_names = []

    get_map_points = []
    X_get_map = 0
    Y_get_map = 0
    current_map = 0

    maps_db_masks = []

    for_hp = [
        ["Red Tea", 25, 15],
        ["Snickers", 50, 30],
        ["Bread", 75, 50],
        ["Tiny piece of Chocolate", 100, 80]
    ]
    for_power = [
        ["Pepsi", 2, 20],
        ["Red Bull", 4, 40],
        ["Rum", 6, 70],
        ["Water", 10, 110]
    ]

    items_for_player = [for_hp, for_power]

    story = [
        "There was a lie...",
        "...on the creation...",
        "...because no one had believed..."
        ]
