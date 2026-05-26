# editor/grid.py

import pygame

class Grid:
    def __init__(self, cell_size=32, color=(200, 200, 200), background_color=(50, 50, 50)):
        self.cell_size = cell_size
        self.color = color
        self.background_color = background_color

    def draw(self, surface, camera_offset):
        # Calculate the bounds of the grid based on the screen size and camera offset
        screen_width, screen_height = surface.get_size()
        grid_x_min = int(camera_offset[0] / self.cell_size)
        grid_y_min = int(camera_offset[1] / self.cell_size)
        grid_x_max = int((camera_offset[0] + screen_width) / self.cell_size) + 1
        grid_y_max = int((camera_offset[1] + screen_height) / self.cell_size) + 1

        # Draw the background color
        surface.fill(self.background_color)

        # Draw the grid lines
        for x in range(grid_x_min, grid_x_max):
            line_x = x * self.cell_size - camera_offset[0]
            pygame.draw.line(surface, self.color, (line_x, 0), (line_x, screen_height))

        for y in range(grid_y_min, grid_y_max):
            line_y = y * self.cell_size - camera_offset[1]
            pygame.draw.line(surface, self.color, (0, line_y), (screen_width, line_y))
