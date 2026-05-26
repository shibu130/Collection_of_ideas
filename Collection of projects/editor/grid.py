# grid.py

import pygame

class Grid:
    def __init__(self, size=(200, 200), offset=(0, 0)):
        self.size = size
        self.offset = offset
        self.cell_size = 10

    def render(self, screen):
        left, top = self.offset
        right, bottom = left + self.size[0], top + self.size[1]

        for x in range(left, right, self.cell_size):
            pygame.draw.line(screen, (150, 150, 150), (x, top), (x, bottom))
        for y in range(top, bottom, self.cell_size):
            pygame.draw.line(screen, (150, 150, 150), (left, y), (right, y))

    def update_offset(self, dx, dy):
        self.offset = (self.offset[0] + dx, self.offset[1] + dy)