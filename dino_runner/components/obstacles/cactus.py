from dino_runner.components.obstacles.Obstacle import Obstacle
import random


class Cactus(Obstacle):

    def __init__(self, image, y_pos):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, y_pos)
