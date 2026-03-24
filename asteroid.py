import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        
        spawn1 = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        spawn2 = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        
        spawn1.velocity = self.velocity.rotate(rand_angle) * 1.2
        spawn2.velocity = self.velocity.rotate(-rand_angle) * 1.2