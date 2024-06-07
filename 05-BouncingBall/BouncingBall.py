import pygame
import sys
import random

balls = []

# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.\
class Ball:
    def __init__(self, screen, x, y, x_speed, y_speed, ball_size, color):
        self.radius = ball_size
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.screen = screen
        self.ball_color = color
        self.x = x
        self.y = y
    def move(self):
        self.y = self.y + self.y_speed
        self.x = self.x + self.x_speed
        if self.x >= self.screen.get_width() or self.x <= 0:
            self.x_speed = -self.x_speed
        if self.y >= self.screen.get_height() or self.y <= 0:
            self.y_speed = -self.y_speed
# dTODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
    def draw(self):
        pygame.draw.circle(self.screen, self.ball_color, (self.x, self.y), radius = self.radius)

# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()


    # TODO: Create an instance of the Ball class called ball1

    balls = []
    for ball_number in range(0,20):
        ball_x_speed = random.randint(1, 20)
        ball_y_speed = random.randint(1, 20)
        ball_size = random.randint(1, 10)
        ball_color1 = random.randint (1,255)
        ball_color2 = random.randint(1, 255)
        ball_color3 = random.randint(1, 255)
        b = Ball(screen, 50, 51, ball_x_speed, ball_y_speed, ball_size,(ball_color1, ball_color2, ball_color3))
        balls.append(b)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        # dTODO: Move the ball

        # dTODO: Draw the ball
        for ball in balls:
            ball.move()
            ball.draw()
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
