import pygame
from pygame.sprite import Sprite  # 对游戏元素进行编组

class Bullet(Sprite):
    """管理飞船所发射出去的子弹的类"""

    def __init__(self, game):
        """创建子弹对象"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # 创建子弹矩形，并放置在飞船上
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # 小数值表示子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹（绘制矩形）"""
        pygame.draw.rect(self.screen, self.color, self.rect)