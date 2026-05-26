import pygame
from editor.editor import Editor
from editor.grid import Grid

def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Grid System Example")
    clock = pygame.time.Clock()
    editor = Editor(screen)
    grid = Grid(cell_size=32, color=(255, 255, 255), background_color=(0, 0, 0))
    camera_offset = [0, 0]
    mouse_pos = (screen_width // 2, screen_height // 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    camera_offset[0] += 10
                elif event.key == pygame.K_RIGHT:
                    camera_offset[0] -= 10
                elif event.key == pygame.K_UP:
                    camera_offset[1] += 10
                elif event.key == pygame.K_DOWN:
                    camera_offset[1] -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                editor.add_mark(mouse_pos, grid.cell_size)
        screen.fill((0, 0, 0))  # Clear the screen with a black background
        grid.draw(screen, camera_offset)
        editor.draw(screen, cell_size=grid.cell_size, camera_offset=camera_offset)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()