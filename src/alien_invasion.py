import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self, full_scrren=False):
        """初始化游戏并创建资源"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        
        self.settings = Settings(full_scrren)

        # 游戏屏幕：surface 对象
        if full_scrren:
            self.run_full_screen()
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, 
                self.settings.screen_height))
            self.settings.bullet_speed = 0.1
            self.settings.ship_speed = 0.2
            
        # 游戏资源
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_full_screen(self):
        """在全屏模式下运行游戏"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()    # 检查事件
            self.ship.update()      # 更新飞船
            self._update_bullets()  # 更新子弹
            self._update_screen()   # 刷新屏幕
            
    def _check_events(self):
        """监听键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """响应按下键盘"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        else:
            print(f"Unknown key: {event.key}:{event.unicode}")

    def _check_keyup_events(self,event):
        """响应松开键盘"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False                    
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False             

    def _fire_bullet(self):
        """创建子弹, 加入bullets编组"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新所有子弹状态"""
        self.bullets.update()   
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """绘制并显示新的屏幕内容"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__ == "__main__":
    flag = False
    # flag = True
    game = AlienInvasion(flag)
    game.run_game()
