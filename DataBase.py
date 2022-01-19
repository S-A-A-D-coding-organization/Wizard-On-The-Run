"""
reads and writes to game_info
"""

game_info = {'Jump': False, }




def call(id):  # This function will call the information by their id
    return game_info[id]


def save(id, value):  # This function will write the information to dictionary
    game_info[id] = value


