# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroids import Asteroid
from constants import *
from player import Player
from asteroid_field import AsteroidField
from shooter import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shots)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updates in updatable:
            updates.update(dt)
            if player.timeout > 0:
                player.timeout -= dt
                print(player.timeout)
        for asteroid in asteroids:
            for shot in shots:
                collision = asteroid.collide(shot)
                if collision:
                    asteroid.split()
                    pygame.sprite.Sprite.kill(shot)
            collision = asteroid.collide(player)
            if collision:
                player.kill()
        #
        pygame.Surface.fill(screen, (0, 0, 0))
        for draws in drawable:
            draws.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()