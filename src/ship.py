import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, game):
        """初始化飞船并设置初始位置"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # 加载飞船图像获取外接矩形
        # 通过外接矩形来处理游戏元素
        self.image = pygame.image.load('./src/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 放置于屏幕底部
        # rect.center.centerx,centery;top,bottom,left,right
        # midbottom,midtop,nmidleft,midright
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blit_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
