import pymunk

class Wall(object):

    def __init__(self, space, points):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Poly(self.body, points, radius=2)
        self.shape.elasticity = 0.99
        space.add(self.body, self.shape)

        self.color = (0, 0, 0)
        self.points = points