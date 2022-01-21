"""
reads and writes to game_info
"""

game_info = {'running': True, }




def call(id):  # This function will call the information by their id
    return game_info[id]


def save(id, value):  # This function will write the information to dictionary
    game_info[id] = value

def game_prep():
    save('Jump', False)
    save('background', 0)
    save('spider_1', 1280)
    save('spider_2', 1800)
    save('ground_1', 0)
    save('ground_2', 1280)
    save('ground_3', 2560)
    save('total_score', 0)
    save('pos', 370)
