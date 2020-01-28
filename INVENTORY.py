import DATABASE as DB
import GAMESTATUS as GSTAT
import os,time

class INVENTORIES:

    def screen_clearing ():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system("clear")

        return None

    @staticmethod
    def show_inventory ():
        while True:
            INVENTORIES.screen_clearing()
            invDB = DB.DRAW.items_for_player
            invGS = GSTAT.GAMESTATS.inventory
            ranged = []

            for elem in range(len(GSTAT.GAMESTATS.inventory)):
                if elem == 0:
                    print("-= HP providers =-")
                elif elem == 1:
                    print("\n-= POWER providers =-")
                for item in range(len(GSTAT.GAMESTATS.inventory[elem])):
                    if GSTAT.GAMESTATS.inventory[elem][item][1] >= 1:
                        ranged.append([elem, GSTAT.GAMESTATS.inventory[elem][item][0]])
                        print("~~~", DB.DRAW.items_for_player[elem][item][0], "in quantity of", GSTAT.GAMESTATS.inventory[elem][item][1], "crypted as", item)

            print("\n\tWhat to choose?")
            user_choose = input("0 or 1 for hp or power respectively (e for exit): ")
            if user_choose == "e":
                return None
            user_use = input("Now enter crypted state of item: ")
            if user_choose == "0":
                try:
                    numberChild = int(user_use)
                    numberLead = int(user_choose)
                    if GSTAT.GAMESTATS.inventory[numberLead][numberChild][1] > 0:
                        GSTAT.GAMESTATS.inventory[numberLead][numberChild][1] -= 1
                        GSTAT.GAMESTATS.player_stats["hp"] += DB.DRAW.items_for_player[numberLead][numberChild][1]
                        if GSTAT.GAMESTATS.player_stats["hp"] > 100:
                            GSTAT.GAMESTATS.player_stats["hp"] = 100
                except TypeError:
                    continue
            elif user_choose == "1":
                try:
                    numberChild = int(user_use)
                    numberLead = int(user_choose)
                    if GSTAT.GAMESTATS.inventory[numberLead][numberChild][1] > 0:
                        GSTAT.GAMESTATS.inventory[numberLead][numberChild][1] -= 1
                        GSTAT.GAMESTATS.player_stats["power"] += DB.DRAW.items_for_player[numberLead][numberChild][1]
                        if GSTAT.GAMESTATS.player_stats["power"] > 30:
                            GSTAT.GAMESTATS.player_stats["hp"] = 30
                except TypeError:
                    continue
            else:
                INVENTORIES.screen_clearing()
            
