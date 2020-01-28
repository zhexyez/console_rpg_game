import DATABASE as DB

class GAMESTATS:

    player_stats = {
        "money": 0,
        "hp": 100,
        "power": 10
        }

    enemy_stats = {
        "hp": 50,
        "power": 5,
        "hp_boss": 300,
        "power_boss": 20
        }

    for_hp = [
        [0,1],
        [1,5],
        [2,2],
        [3,3]
    ]
    for_power = [
        [0,0],
        [1,1],
        [2,0],
        [3,0]
    ]

    inventory = [for_hp, for_power]
