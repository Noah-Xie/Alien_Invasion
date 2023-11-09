import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示外星人的类"""

    def __init__(self, game):
        """初始化一个外星人"""
        super().__init__()
        self.screen = game.screen
        
        # 加载外星人图像并获得外接矩形
        self.image = pygame.image.load('./src/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人初始位置, 为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人精确水平位置
        self.x = float(self.rect.x)
