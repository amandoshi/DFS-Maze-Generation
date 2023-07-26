import constants
import dfs
from gui import GUI

def main():
    table = setup_table()
    store_2d_arr(table, constants.CSV_TABLE_FILENAME)
    gui = GUI(constants.MAZE_WIDTH, constants.MAZE_HEIGHT, table)
    gui.run()

def setup_table():
    dmg = dfs.DFS_Maze_Generation(constants.MAZE_WIDTH, constants.MAZE_HEIGHT)
    print(dmg.maze_table, len(dmg.maze_table))
    return dmg.maze_table

def store_2d_arr(arr_2d, filename):
    print(arr_2d)
    with open(filename, "w") as file:
        for arr in arr_2d:
            arr_str = ",".join([str(x) for x in arr])
            file.write(arr_str + "\n")

if __name__ == "__main__":
    main()