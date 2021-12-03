import random
import pygame.time

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obs_list = []

    def draw(self, screen):
        for obs in self.obs_list:
            obs.draw(screen)

    def update(self, game):
        if len(self.obs_list) == 0:
            if random.randint(1, 2) == 1:
                self.obs_list.append(Cactus(SMALL_CACTUS, 330))
            else:
                self.obs_list.append(Cactus(LARGE_CACTUS, 308))

        for obst in self.obs_list:
            obst.update(game.game_speed, self.obs_list)

            if game.player.dino_rect.colliderect(obst.rect):
                if not game.player.shield:
                    if game.life_manager.life_counter() == 1:
                        game.death_acount += 1
                        pygame.time.delay(500)
                        game.playing = False
                        break
                    else:
                        game.life_manager.delete_life()
                self.obs_list.remove(obst)

    def reset_obstacles(self):
        self.obs_list = []