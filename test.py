import json
import random

def movement_file():
    try:
        with open("easy_movement.json") as movement_file:
            movements=json.load(movement_file)
            print("Hej det gick!")
            return movements
            
    
    except:
        print("Tyvärr gick inte filen att öppna.")
        exit()



def random_func(dictio):

    random_thing=random.choice(list(dictio))
    return random_thing


def easy_movement():
    movement_dict=movement_file()
    random_movement=random_func(movement_dict)
    print(random_movement)
    random_movement_str=movement_dict[random_movement]["movement"]

    print(random_movement_str)

easy_movement()
