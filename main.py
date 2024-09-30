import pygame  
from constants  import *

### DEFINITION MAIN

def main():
    pygame.init()
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (F"Screen heightwx: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(pygame.Color(255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        
### APPEL DE MAIN

if __name__ == "__main__":  
    main()