import pygame
from circleshape import CircleShape
from constants import *
from bullets import Shot

#Inherent hitbox from circle sprite
class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    #Changes the look of the player sprite to that of a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #Draw the player sprite
    def draw(self, screen):
        pygame.draw.polygon(screen, 'green', self.triangle(), width=2)

    #Ability for user to rotate player sprite
    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    #Ability for user to move player sprite
    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    #Ability for the user to shoot. Along with a cooldown between shots.
    def shoot(self):
        if self.shot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN
            
    #Tie rotation of player sprite to key input
    def update(self, delta_time):
        self.shot_cooldown -= delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(delta_time/-1)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(delta_time/-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
    