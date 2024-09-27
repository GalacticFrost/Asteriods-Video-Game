import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):

    def __init__(self, position):
        self.position = position
        self.velocity = pygame.Vector2(0, 1)
        self.radius = SHOT_RADUIS

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius)

    def update(self, delta_time):
        self.position += self.velocity * delta_time