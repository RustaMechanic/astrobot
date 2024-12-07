import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player

def main():
    # Game initialization
    pygame.init()

    # Game clock initialization
    clock = pygame.time.Clock()

    # Game screen initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game objects groups initialization
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Player initialization
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Running the game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Display filling
        screen.fill((0,0,0))
        
        # Update all objects
        for object in updateable:
            object.update(dt)

        # Iterate all objects
        for object in drawable:
            object.draw(screen)
        
        # Render display
        pygame.display.flip()
        
        # Managing FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
