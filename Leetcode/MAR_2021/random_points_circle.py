import random
class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # x_point = random.uniform(self.x_center - radius, self.x_center + self.radius)
        # y_point = random.uniform(self.y_center - radius, self.y_center + self.radius)
        # while [x_point, y_point] in self.points:
        #     x_point = random.uniform(self.x_center - radius, self.x_center + self.radius)
        #     y_point = random.uniform(self.y_center - radius, self.y_center + self.radius)
        theta = random.uniform(0, 2*pi)
        R = self.radius * sqrt(random.uniform(0, 1))
        return [self.x_center + R*cos(theta), self.y_center + R*sin(theta)]

        