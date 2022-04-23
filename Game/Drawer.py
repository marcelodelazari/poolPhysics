import pygame
from pygame import gfxdraw
from math import sqrt
class Drawer(object):
    def __init__(self, screen, balls, walls):
        self.screen = screen
        self.balls = balls
        self.walls = walls
        self.aiming = False

    def draw(self):
        self.draw_balls()
        self.draw_walls()
    def draw_balls(self):
        for ball in self.balls:
            self.draw_ball(ball)

    def draw_ball(self, ball):
        pos = self.converted_pos(ball.body.position)
        pygame.gfxdraw.filled_circle(self.screen, int(pos[0]), int(pos[1]), ball.size, ball.color)
        if ball.striped:
            pygame.gfxdraw.filled_circle(self.screen, int(pos[0]), int(pos[1]), int(ball.size*0.7), (255, 255, 255))
            pygame.gfxdraw.aacircle(self.screen, int(pos[0]), int(pos[1]), int(ball.size * 0.7), (0, 0 ,0))

    def draw_walls(self):
        for wall in self.walls:
            self.draw_wall(wall)
    def draw_wall(self, wall):

        converted_points = [self.converted_pos(pos) for pos in wall.points]
        pygame.gfxdraw.aapolygon(self.screen, converted_points, wall.color)
    def converted_pos(self, pos):
        return int(pos[0]), int(self.screen.get_height() - pos[1])

    def draw_vector(self, vector, pos,size):
        x1, y1, x2, y2 = pos[0], pos[1], pos[0] + vector[0]*size, pos[1] + vector[1]*size
        x1, y1 = self.converted_pos((x1, y1))
        x2, y2 = self.converted_pos((x2, y2))
        pygame.gfxdraw.line(self.screen, x1, y1, x2, y2, (0, 0, 0))