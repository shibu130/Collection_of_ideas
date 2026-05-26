import pygame
from editor.editor import Editor
def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Visual Director")
    
    # Create an instance of the Editor class
    editor = Editor(screen)
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event received")
                running = False
            elif event.type == pygame.VIDEORESIZE:
                editor.resize(event.size)
        
        # Update the editor
        editor.update(dt)
        
        # Render the editor
        screen.fill((255, 255, 255))  # Clear the screen with white
        editor.render(screen)
        
        pygame.display.flip()
    
    print("Main loop ended")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()