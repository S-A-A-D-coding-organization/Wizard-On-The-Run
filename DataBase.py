"""
reads and writes to game_info
"""

game_info = {
    'running': True,
    'Jump': False,
    'spider_1': 1280,
    'spider_2': 1800,
    'ground_1': 0,
    'ground_2': 1280,
    'ground_3': 2560,
    'total_score': 0,
    'pos': 370,

             }




def call(id):  # This function will call the information by their id
    return game_info[id]


def save(id, value):  # This function will write the information to dictionary
    game_info[id] = value


