import sys
import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Game initialization
    pygame.init()

    # Game clock initialization
    clock = pygame.time.Clock()

    # Game screen initialization
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game objects groups initialization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player initialization
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteroid initialization
    Asteroid.containers = (asteroids, updatable, drawable)

    # AsteroidField initialization
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    # AsteroidField initialization
    Shot.containers = (shots, updatable, drawable)

    dt = 0

    # Running the game loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update all objects
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            # Check if an asteroid collides with the player
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split(shot)

        # Display filling
        screen.fill((0,0,0))

        # Iterate all objects
        for object in drawable:
            object.draw(screen)
        
        # Render display
        pygame.display.flip()
        
        # Managing FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
