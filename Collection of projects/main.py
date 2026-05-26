# main.py

import pygame

from editor.editor import Editor  # Import the Editor class from editor.py
def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Visual Director")
    
    editor = Editor(screen)  # Create an instance of the Editor
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event received")
                running = False
            elif event.type == pygame.VIDEORESIZE:
                editor.resize(event.size)
        
        editor.update(dt)
        screen.fill((255, 255, 255))  # Clear the screen with white

        editor.render(screen)
        pygame.display.flip()
    
    print("Main loop ended")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()