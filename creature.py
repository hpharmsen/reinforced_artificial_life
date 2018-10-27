import math
import random


MIN_RADIUS = 15
MAX_RADIUS = 25
MAX_SPEED = 7


class Creature:
    """Creature class representing one bouncing ball for now."""
    id_count = 0

    def __init__(self, x, y, dx, dy, color, radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.radius = radius
        self.id = Creature.id_count
        Creature.id_count += 1

    def step(self, world, overlapping):
        self.x += self.dx
        self.y += self.dy

        ddx = random.random() * 0.3 - 0.15
        ddy = random.random() * 0.3 - 0.15

        # Bounce off walls:
        dist = self.distance(0, 0)
        if dist > world.size - self.radius:
            ddx -= 0.05 * self.x / dist
            ddy -= 0.05 * self.y / dist

        for other in overlapping:
            dist = self.distance(other.x, other.y)
            if dist:
                ddx -= 3 * (other.x - self.x) / dist
                ddy -= 3 * (other.y - self.y) / dist

        self.dx += ddx
        self.dy += ddy

        # Maximum speed:
        if abs(self.dx) > MAX_SPEED:
            self.dx *= MAX_SPEED / abs(self.dx)
        if abs(self.dy) > MAX_SPEED:
            self.dy *= MAX_SPEED / abs(self.dy)

    def draw(self, display):
        display.circle(self.color, self.x, self.y, int(self.radius))

    def box(self):
        """Return the bounding box for this creature"""
        r2 = self.radius
        res = [self.x - r2, self.y - r2, self.x + r2, self.y + r2]
        return res

    def distance(self, x1, y1):
        dx = self.x - x1
        dy = self.y - y1
        return math.sqrt(dx * dx + dy * dy)
