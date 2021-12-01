import pygame.time

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obs_list = []

    def draw(self, screen):
        for obs in self.obs_list:
            obs.draw(screen)

    def update(self, game):
        if len(self.obs_list) == 0:
            self.obs_list.append(Cactus(SMALL_CACTUS))

        for obst in self.obs_list:
            obst.update(game.game_speed, self.obs_list)

            if game.player.dino_rect.colliderect(obst.rect):
                pygame.time.delay(500)
                game.playing = False
                break
