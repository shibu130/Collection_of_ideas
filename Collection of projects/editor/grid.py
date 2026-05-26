import pygame

class Grid:
    def __init__(self, screen, cell_size=20):
        self.screen = screen
        self.cell_size = cell_size
        self.width = int(screen.get_width() / cell_size)
        self.height = int(screen.get_height() / cell_size)

    def render(self, camera_offset=(0, 0)):
        offset_x, offset_y = camera_offset
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.screen, (200, 200, 200), 
                                 ((x * self.cell_size) + offset_x,
                                  (y * self.cell_size) + offset_y,
                                  self.cell_size,
                                  self.cell_size),
                                 1)