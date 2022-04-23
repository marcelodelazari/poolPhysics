import pygame
from win32api import GetKeyState
from math import sqrt

class InputHandler(object):

    def __init__(self, screen, drawer, balls):
        self.screen = screen
        self.drawer = drawer
        self.balls = balls
        self.holding = False
        self.max_shoot_strength = 4000.0
        self.white_ball = balls[0]

    def handle(self):
        self.handle_mouse()

    def handle_mouse(self):
        if not self.holding:
            if GetKeyState(0x01) < 0:
                self.holding = True
        else:
            starting_pos = self.white_ball.body.position
            release_pos = self.get_mouse_pos()
            if release_pos == starting_pos:
                return

            vx, vy = starting_pos[0] - release_pos[0], starting_pos[1] - release_pos[1]
            norm = sqrt(sum(e ** 2 for e in (vx, vy)))
            strength = min(self.max_shoot_strength, norm * 20)
            vx /= norm
            vy /= norm
            unitary = vx, vy

            self.draw_aim(unitary, strength)

            if not GetKeyState(0x01) < 0:
                self.shoot_white_ball(unitary, strength)
                self.holding = False

    def shoot_white_ball(self, unitary, strength):

        self.white_ball.body.velocity = (0, 0)
        vx, vy = unitary
        x = vx * strength
        y = vy * strength
        self.white_ball.body.velocity = x, y

    def get_mouse_pos(self):
        return self.pymunk_coordinates(pygame.mouse.get_pos())

    def pymunk_coordinates(self, pos):
        return pos[0], self.screen.get_height() - pos[1]

    def draw_aim(self, unitary, strength):
        self.drawer.draw_vector(unitary, self.white_ball.body.position, int(strength / self.max_shoot_strength * 100))