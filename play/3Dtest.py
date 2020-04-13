import pygame
from pygame.locals import *
from random import randint


def draw_grid(self, screen_surf):
        """
        画网格
        """
        for x in range(self.w):
            for y in range(self.h):
                if self[x][y] == 0:  # 不是障碍，画空心的矩形
                    pygame.draw.rect(screen_surf, (255, 255, 255), (self.x + x * 32, self.y + y * 32, 32, 32), 1)
                else:  # 是障碍，画黑色实心的矩形
                    pygame.draw.rect(screen_surf, (0, 0, 0), (self.x + x * 32 + 1, self.y + y * 32 + 1, 30, 30), 0)

#
# def update(self):
#     while True:
#         self.clock.tick(self.fps)
#         # TODO:逻辑更新
#         self.event_handler()
#         # TODO:画面更新
#         self.game_map.draw_bottom(self.screen_surf)
#         Sprite.draw(self.screen_surf, self.hero, 100, 100, 0, 0)
#         Sprite.draw(self.screen_surf, self.hero, 210, 120, 1, 1)
#         Sprite.draw(self.screen_surf, self.hero, 300, 100, 2, 2)
#         self.game_map.draw_top(self.screen_surf)
#         self.game_map.draw_grid(self.screen_surf)
#         pygame.display.update()


if __name__ == '__main__':
    draw_grid()