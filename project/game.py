import pygame
import sys




class Cube:
    def __init__(self, screen, x, y, cube_size, cube_color):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = cube_size
        self.color = cube_color

    def move(self):
        pass






    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y), self.radius)





def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("World's Hardest Game")
    screen = pygame.display.set_mode((640, 650))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        Cube.draw()
        screen.fill((255, 255, 255))




        pygame.display.update()


main()
