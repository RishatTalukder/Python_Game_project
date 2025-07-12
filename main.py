import pygame
from settings import Settings

class Ship:
    def __init__(self, screen):
        ship_image = pygame.image.load('./images/spaceship.png')
        # self.ship_image = pygame.transform.scale(ship_image, (40,200))
        self.ship_image = pygame.transform.scale_by(ship_image, .07)
        self.screen = screen
        
    def blitme(self):    
        self.screen.blit(self.ship_image, (100,200))


class Main:

    def __init__(self):

        #pygame is a wrapper for SDL
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(
            self.settings.width,
            self.settings.height
        ))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self.screen)




        #talk about this later
        self.clock = pygame.time.Clock()
        # Font for FPS
        self.font = pygame.font.SysFont("Arial", 24)

    def run_game(self):
        x=100
        y = 100
        while True:
            events = pygame.event.get()
            print(events)
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 
                
            self.screen.fill(self.settings.bg_color) #this is the backaground
            self.render_fps(self.screen, self.clock, self.font)
            self.ship.blitme()


            pygame.display.flip()


            #talk about this later
            self.clock.tick()

    
    #talk about this later
    def render_fps(self,screen, clock, font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"fps_rate: {fps}", True, (255, 0, 0))
        screen.blit(fps_text, (10, 10))  # Top-left corner





main = Main()
main.run_game()
