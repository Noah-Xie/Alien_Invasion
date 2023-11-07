import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建资源"""
        pygame.init()
        self.settings = Settings()

        # surface 对象
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, 
             self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self._update_screen()
            

    def _check_events(self):
        """监听键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """绘制并显示新的屏幕内容"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_ship()
        
        pygame.display.flip()

if __name__ == "__main__":
    game = AlienInvasion()
    game.run_game()
