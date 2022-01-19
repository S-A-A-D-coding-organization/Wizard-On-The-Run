"""
reads and writes data from data\Data.db
"""

import sqlite3

connection = sqlite3.Connection('data/Data.db')
cursor = connection.cursor()

# To restart the game




def call(id):  # This function will call the information by their id
    cursor.execute("SELECT * FROM game_info WHERE info_id=?", (id,))
    return cursor.fetchall()[0][1]


def save(id, value):  # This function will write the information to dictionary
    command = "UPDATE game_info SET amount = %s WHERE info_id = '%s' " % (value, id)
    cursor.execute(command)


def db_prep():
    # create database
    command_1 = """CREATE TABLE IF NOT EXISTS
    game_info(info_id TEXT , amount INTEGER)"""
    cursor.execute(command_1)

    # form color black
    cursor.execute("""INSERT INTO game_info VALUES ( 'Black_1', 0)""")
    cursor.execute("""INSERT INTO game_info VALUES ( 'Black_2', 0)""")
    cursor.execute("""INSERT INTO game_info VALUES ( 'Black_3', 0)""")

    # form color white
    cursor.execute("""INSERT INTO game_info VALUES ( 'White_1', 255)""")
    cursor.execute("""INSERT INTO game_info VALUES ( 'White_2', 255)""")
    cursor.execute("""INSERT INTO game_info VALUES ( 'White_3', 255)""")

    # position value
    cursor.execute("""INSERT INTO game_info VALUES ( 'Position', 0)""")

