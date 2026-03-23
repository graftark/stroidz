import pygame
import sys
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event


def main():
    pygame.init()
    print("Starting Asteroids with pygame version: %s" % pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        shots.update(dt)

        for thing in drawable:
            thing.draw(screen)       
        
        for stroid in asteroids:
            if stroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if stroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    stroid.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()