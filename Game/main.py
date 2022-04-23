import pygame
import pymunk

from InputHandler import InputHandler
from Ball import Ball
from Drawer import Drawer
from Wall import Wall

def global_friction(friction):
    global balls

    for ball in balls:
        a, b = ball.body.velocity
        a *= 1 - (friction/100)
        b *= 1 - (friction/100)
        ball.body.velocity = a, b

pygame.init()
WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pool")

# Space
space = pymunk.Space()

# Walls and balls
margin_x = WIDTH*0.04
margin_y = HEIGHT*0.04
top_left = margin_x, HEIGHT - margin_y
top_right = WIDTH - margin_x, HEIGHT - margin_y
bottom_left = margin_x, margin_y
bottom_right = WIDTH - margin_x, margin_y

outside_table_top = Wall(space, (top_left, top_left, top_right, top_right))
outside_table_bottom = Wall(space, (bottom_left, bottom_left, bottom_right, bottom_right))
outside_table_left = Wall(space, (top_left, top_left, bottom_left, bottom_left))
outside_table_right = Wall(space, (top_right, top_right, bottom_right, bottom_right))

white_ball = Ball(space, (WIDTH/4, HEIGHT/2), 20, 1 , 1, 1, 0.8, (255, 255, 255))
red_ball = Ball(space, (800, HEIGHT/2), 20, 1 , 1 , 1, 0.8, (255, 0, 0))
reds_ball = Ball(space, (800, HEIGHT/2), 20, 1 , 1 , 1, 0.8, (255, 0, 0), True)
orange_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (255, 140, 0))
oranges_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (255, 140, 0), True)
green_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (0, 255, 0))
greens_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (0, 255, 0), True)
blue_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (0, 0, 255))
blues_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (0, 0, 255), True)
brown_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (75, 54, 33))
browns_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (75, 54, 33), True)
purple_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (148, 0, 211))
purples_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (148, 0, 211), True)
yellow_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (255, 255, 0))
yellows_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (255, 255, 0), True)
black_ball = Ball(space, (800, HEIGHT/2 + 5), 20, 1 , 1 , 1, 0.8, (0, 0, 0))
# lower_wall = Wall(space, (60, 200), (1100, 0), 50)
balls = [white_ball, red_ball, reds_ball, orange_ball, oranges_ball, green_ball, greens_ball, blue_ball, brown_ball,
         blues_ball, purple_ball, yellow_ball, browns_ball, black_ball, yellows_ball, purples_ball]
walls = [outside_table_top,outside_table_bottom,outside_table_left,outside_table_right]
drawer = Drawer(screen, balls, walls)

# Input
inputHandler = InputHandler(screen, drawer, balls)

FPS = 144
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 130, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    global_friction(0.3)
    space.step(1 / FPS)
    drawer.draw()
    inputHandler.handle()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()