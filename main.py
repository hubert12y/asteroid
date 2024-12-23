import pygame  
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants  import *
from player import Player, Shot    
from player import *
### DEFINITION MAIN

def main():
    pygame.init()
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (F"Screen heightwx: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = pygame.time.Clock() 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()   
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)  
    AsteroidField.containers = updatable
    Shot.containers = (updatable,drawable,shots)
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    asteroid_field = AsteroidField()
    player = Player(x , y)  
    while True:
        screen.fill(pygame.Color(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = p1.tick(60) / 1000
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.colisions(player):
                print("Game over!")
                return 
        for asteroid in asteroids:
    
            for shot in shots:
                if shot.colisions(asteroid):
                    asteroid.split()
                    shot.kill()
                    
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()       


        
        
        
### APPEL DE MAIN

if __name__ == "__main__":  
    main()