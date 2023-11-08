import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self, full_scrren=False):
        """初始化游戏并创建资源"""
        pygame.init()
        self.settings = Settings()

        # surface 对象
        if full_scrren:
            self.run_full_screen()
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, 
                self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

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
        else:
            print(f"Unknown key: {event.key}:{event.unicode}")

    def _check_keyup_events(self,event):
        """响应松开键盘"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False                    
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False             


    def _update_screen(self):
        """绘制并显示新的屏幕内容"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_ship()
        
        pygame.display.flip()

if __name__ == "__main__":
    flag = False
    # flag = True
    game = AlienInvasion(flag)
    game.run_game()
