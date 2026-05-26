# editor/editor.py

import pygame

class Editor:
    def __init__(self, screen):
        self.screen = screen
        self.marks = []

    def add_mark(self, position, cell_size):
        # Convert mouse position to grid coordinates
        grid_x, grid_y = position[0] // cell_size, position[1] // cell_size
        self.marks.append((grid_x, grid_y))

    def draw(self, surface, cell_size, camera_offset):
        for mark in self.marks:
            x = (mark[0] * cell_size) - camera_offset[0]
            y = (mark[1] * cell_size) - camera_offset[1]
            pygame.draw.rect(surface, (255, 0, 0), (x, y, cell_size, cell_size))