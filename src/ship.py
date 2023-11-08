import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, game):
        """初始化飞船并设置初始位置"""
        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = game.screen.get_rect()
    
        # 加载飞船图像获取外接矩形
        # 通过外接矩形来处理游戏元素
        self.image = pygame.image.load('./src/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 放置于屏幕底部
        # rect.center.centerx,centery;top,bottom,left,right
        # midbottom,midtop,nmidleft,midright
        self.rect.midbottom = self.screen_rect.midbottom

        # 小数值的飞船属性
        self.x = float(self.rect.x)
    
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 利用小数值的x来更新rect值
        self.rect.x = self.x


    def blit_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
