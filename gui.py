import constants
import pygame

class GUI:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, grid_width, grid_height, table):
        pygame.init()

        # screen properties
        screen_width = grid_width * constants.TILE_SIZE + 1 * constants.TILE_BORDER_SIZE
        screen_height = grid_height * constants.TILE_SIZE + 1 * constants.TILE_BORDER_SIZE

        self.__screen = pygame.display.set_mode((screen_width, screen_height))
        self.__clock = pygame.time.Clock()
        self.__running = True
        self.__table = table

    def run(self):
        while self.__running:
            # setup
            self.__process_event()

            self.__screen.fill(GUI.BLACK)

            # render
            self.__render_tiles()

            #reset
            pygame.display.flip()
            self.__clock.tick(60)

        pygame.quit()

    def __process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

    # render tiles

    def __render_tiles(self):
        y_coord = 0
        for y in range(len(self.__table)):
            x_coord = 0
            for x in range(len(self.__table[0])):
                rect_color = self.__tile_colors(self.__table[y][x])
                rect_shape = (x_coord + constants.TILE_BORDER_SIZE, y_coord + constants.TILE_BORDER_SIZE, 
                              constants.TILE_SIZE - constants.TILE_BORDER_SIZE, constants.TILE_SIZE - constants.TILE_BORDER_SIZE)
                pygame.draw.rect(self.__screen, rect_color, rect_shape)
                x_coord += constants.TILE_SIZE
            y_coord += constants.TILE_SIZE
    
    def __tile_colors(self, value):
        match value:
            case 0: # path
                return GUI.WHITE
            case 1: # wall
                return GUI.BLACK