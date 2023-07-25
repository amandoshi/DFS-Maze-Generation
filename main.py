import constants
import dfs
from gui import GUI

def main():
    table = setup_table()
    gui = GUI(constants.MAZE_WIDTH, constants.MAZE_HEIGHT, table)
    gui.run()

def setup_table():
    dmg = dfs.DFS_Maze_Generation(constants.MAZE_WIDTH, constants.MAZE_HEIGHT)
    return dmg.maze_table
    # table = [[0] * constants.MAZE_WIDTH for _ in range(constants.MAZE_HEIGHT)]
    # return table

if __name__ == "__main__":
    main()