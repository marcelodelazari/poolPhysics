import pymunk

class Ball(object):

    def __init__(self, space, pos, size, mass, momentum, density, elasticity, color, striped=False):
        self.body = pymunk.Body(mass, momentum)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, size)
        self.shape.density = density
        self.shape.elasticity = elasticity
        space.add(self.body, self.shape)

        self.size = size
        self.color = color
        self.striped = striped

