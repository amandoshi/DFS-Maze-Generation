import random

class DFS_Maze_Generation:
    class Tile:
        def __init__(self, x, y, pt):
            self.x = x
            self.y = y
            self.border = {"N": True, "S": True, "E": True, "W": True}
            self.prev_tile = pt
        
        def get_neighbors(self):
            return [
                DFS_Maze_Generation.Tile(self.x, self.y - 1, self),
                DFS_Maze_Generation.Tile(self.x, self.y + 1, self),
                DFS_Maze_Generation.Tile(self.x + 1, self.y, self),
                DFS_Maze_Generation.Tile(self.x - 1, self.y, self)
            ]
        
        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.x == other.x and self.y == other.y
            return False

        def __ne__(self, other):
            return not self.__eq__(other)
        
        def __hash__(self):
            return self.x * 128 + self.y
        
        def __repr__(self):
            return f"Tile({self.x}, {self.y}, {str(self.border)}"

    def __init__(self, width, height):
        assert width % 2 == 1, "Grid width must be odd."
        assert height % 2 == 1, "Grid height must be odd."

        self.__width = int((width + 1) / 2)
        self.__height = int((height + 1) / 2)
        self.__visited = set()
        
        self.__generate_maze()
        self.maze_table = self.__get_table()

    def __generate_maze(self):
        next_tile = [DFS_Maze_Generation.Tile(0, 0, None)]
        self.__visited = set()

        while len(next_tile):
            curr_tile = next_tile.pop()

            if self.__valid_tile(curr_tile):
                self.__visited.add(curr_tile)
                self.__open_wall(curr_tile, curr_tile.prev_tile)

                # push valid neighbor tiles to stack
                # neighbors = curr_tile.get_neighbors()
                neighbors = [x for x in curr_tile.get_neighbors() if self.__valid_tile(x)]
                random.shuffle(neighbors)
                for tile in neighbors:
                    next_tile.append(tile)

    def __valid_tile(self, tile):
        return tile not in self.__visited and 0 <= tile.x < self.__width and 0 <= tile.y < self.__height

    def __open_wall(self, t1, t2):
        if not t1 or not t2:
            return

        if t1.x < t2.x:
            t1.border["E"] = False
            t2.border["W"] = False
        elif t2.x < t1.x:
            t2.border["E"] = False
            t1.border["W"] = False
        elif t1.y < t2.y:
            t1.border["S"] = False
            t2.border["N"] = False
        elif t2.y < t1.y:
            t2.border["S"] = False
            t1.border["N"] = False

        # print(f"({t1.x}, {t1.y}) ({t2.x}, {t2.y})", t1.__repr__(), t2.__repr__())

    def __get_table(self):
        table = [[1] * (self.__width * 2 + 1) for _ in range(self.__height * 2 + 1)]
        for tile in self.__visited:
            table[tile.x * 2][tile.y * 2] = 0
            if not tile.border["N"]:
                table[tile.x * 2][tile.y * 2 - 1] = 0
            if not tile.border["S"]:
                table[tile.x * 2][tile.y * 2 + 1] = 0
            if not tile.border["E"]:
                table[tile.x * 2 + 1][tile.y * 2] = 0
            if not tile.border["W"]:
                table[tile.x * 2 - 1][tile.y * 2] = 0
        # print(self.__visited)
        return table
