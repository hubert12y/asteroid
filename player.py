import pygame
import circleshape
import constants

class Player(circleshape.CircleShape):
    def __init__(self, x , y):
        super().__init__(x , y , constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(255,255,255), self.triangle(), 2)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)        
            # ?
        if keys[pygame.K_d]:    
            self.rotate(dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
            
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
                
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):    
        if self.timer >= 0:
            return
        shot = Shot(self.position.x,  self.position.y)
        self.timer = constants.PLAYER_SHOOT_COOLDOWN
        
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)* constants.PLAYER_SHOOT_SPEED
        
        
class Shot(circleshape.CircleShape):    
    def __init__(self, x, y):   
        
        super().__init__(x, y, constants.SHOT_RADIUS)  
        
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255),self.position, self.radius, 2 )   
    def update(self, dt):
       self.position += (self.velocity * dt)
    
        
   
        
    

    