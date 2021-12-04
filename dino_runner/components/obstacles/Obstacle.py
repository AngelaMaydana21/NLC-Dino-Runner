from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle(Sprite):

    def __init__(self, image, type,y_pos):
        self.image = image
        self.type = type
        self.step_index1 = 0
        self.step_index2 = 0
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y_pos

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

