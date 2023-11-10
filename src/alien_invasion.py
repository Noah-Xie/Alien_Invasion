import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
            self.settings.alien_speed = 0.2
            self.settings.bullet_speed = 0.1
            self.settings.alien_drop_speed = 5
        pygame.display.set_caption("Alien Invasion")

        # 游戏资源
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()


    def run_full_screen(self):
        """在全屏模式下运行游戏"""
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    # 事件
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

    # 子弹
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
                
    # 外星人
    def _create_alien_fleet(self):
        """创建外星人舰队"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # 创建一行外星人，间距为一个外星人宽
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                             (3 * alien_width) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # 创建一行外星人
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        """创建一个外星人放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number  # 向右平移
        alien.rect.x = alien.x
        alien.rect.y = alien_height * (1 + 2 * row_number)
        self.aliens.add(alien)        
    
    def _check_fleet_edges(self):
        """检查是否有外星人触碰到边缘, 并做出反应"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将外星人下移，并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_aliens(self):
        """更新所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    # 游戏屏幕
    def _update_screen(self):
        """绘制并显示新的屏幕内容"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_ship()           # 画一艘船
        for bullet in self.bullets.sprites(): # 画所有的子弹
            bullet.draw_bullet()
        self.aliens.draw(self.screen)   # 依次画所有的外星人

        pygame.display.flip()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()    # 检查事件
            self.ship.update()      # 更新飞船
            self._update_bullets()  # 更新子弹
            self._update_aliens()
            self._update_screen()   # 刷新屏幕
            
if __name__ == "__main__":
    flag = False
    # flag = True
    game = AlienInvasion(flag)
    game.run_game()
