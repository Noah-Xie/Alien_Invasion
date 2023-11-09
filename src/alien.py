import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示外星人的类"""

    def __init__(self, game):
        """初始化一个外星人"""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        
        # 加载外星人图像并获得外接矩形
        self.image = pygame.image.load('./src/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 设置外星人初始位置, 为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人精确水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """检查是否触碰到了边缘"""
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """移动外星人"""
        self.x += self.settings.alien_speed * \
                    self.settings.fleet_direction
        self.rect.x = self.x
