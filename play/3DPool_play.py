import pygame
from pygame.locals import *
from sys import exit
from random import randint


class Star(object):  # 类
    def __init__(self, x, y, speed):  # 重载
        self.x = x
        self.y = y
        self.speed = speed


def run():  # 函数
    pygame.init()  # pygame初始化
    width, height = 1920, 1080  # 设置屏幕分辨率
    screen = pygame.display.set_mode((width, height), 0, 32)
    Fullscreen = False
    stars = []
    for n in range(700):  # 在第一帧画上一些星星
        x = float(randint(0, 1919))
        y = float(randint(0, 1079))
        speed = float(randint(30, 300))
        stars.append(Star(x, y, speed))

    clock = pygame.time.Clock()  # Clock对象
    white = (255, 255, 255)
    # # 设置背景音效
    # pygame.mixer.music.load("starbg.wav")
    # pygame.mixer.music.play(-1, 0.0)

    color = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (160, 32, 240)]
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_f:  # F键控制是否全屏
                    Fullscreen = not Fullscreen
                    if Fullscreen:
                        # 创建一个硬件加速的全屏窗口，FULLSCREEN(全屏窗口)， HWSURFACE(硬件加速，必须和FULLSCREEN一起使用)
                        screen = pygame.display.set_mode((width, height), FULLSCREEN | HWSURFACE, 32)  # 全屏+硬件加速
                    else:
                        screen = pygame.display.set_mode((width, height), 0, 32)

        x = float(randint(0, 1919))  # 增加一颗新的星星
        speed = float(randint(10, 300))
        star = Star(x, 0, speed)
        stars.append(star)
        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000  # 单位毫秒,需转换

        screen.fill((0, 0, 0))
        for star in stars:  # 绘制所有星星
            new_y = star.y + time_passed_seconds * star.speed
            pygame.draw.aaline(screen, color[count], (star.x, new_y), (star.x, star.y + 5))
            star.y = new_y
            count += 1
            if count > 6:
                count = 0

        def on_screen(star):
            return star.y > 0

        stars = list(filter(on_screen, stars))  # 星星跑出画面就删除
        pygame.display.update()


if __name__ == "__main__":
    run()
