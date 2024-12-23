import random 
from constants import *
import pygame
import circleshape
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255),self.position, self.radius, 2 )   
    def update(self, dt):
       self.position += (self.velocity * dt)    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
           
        random_angle = random.uniform(20, 50)   
        first = self.velocity.rotate(random_angle)
        second = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x ,self.position.y, radius)
        
        second_asteroid = Asteroid(self.position.x ,self.position.y, radius)
        first_asteroid.velocity =  (first * 1.2)
        second_asteroid.velocity = (second * 1.2)