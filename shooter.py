import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x,y,SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        print(self.position)
        self.velocity = pygame.Vector2(0,1).rotate(rotation)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt * PLAYER_SHOOT_SPEED