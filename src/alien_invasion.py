import sys
import time

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stat import GameStats
from button import Button
from score_board import ScoreBoard

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self, full_screen=False):
        """初始化游戏并创建资源"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        
        self.settings = Settings()

        # 游戏屏幕：surface 对象
        if full_screen:
            self.run_full_screen()
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, 
                self.settings.screen_height))
            # self.settings.alien_speed = 1.0
            # self.settings.alien_drop_speed = 10
            self.settings.bullet_speed = 1.0
            self.settings.bullet_width = 600
        pygame.display.set_caption("Alien Invasion")
        self.screen_rect = self.screen.get_rect()

        # 游戏统计信息
        self.stats = GameStats(self)
        self.scoreBoard = ScoreBoard(self)

        # 游戏资源
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_alien_fleet()

        # Play 按钮
        self.play_button = Button(self, "Play")

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
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击事件
                mouse_pos = pygame.mouse.get_pos()  # 获取鼠标位置
                self._check_play_button(mouse_pos)

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
    
    def _check_play_button(self, mouse_pos):
        """点击play按钮, 开始新的游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # 仅当游戏未开始时，才可以触发click button的效果
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()

            # 重置游戏状态
            self.stats.game_active = True
            self.stats.reset_stats()
            self.scoreBoard.prep_score()
            
            # 清空场上游戏元素
            self.aliens.empty()
            self.bullets.empty()

            # 重新创建外星人群和飞船
            self._create_alien_fleet()
            self.ship.center_ship()

            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)

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
            
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """检查是否有子弹碰撞到外星人，并删除他们"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        # 击杀外星人获得分数
        if collisions:
            # 碰撞字典: 子弹:击中的外星人列表
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreBoard.prep_score()  # 重新渲染（绘制）分数
        
        if not self.aliens:
            # 清除所有子弹并重新生成外星人
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.increase_game_speed()  # 并且游戏提速
                
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
        
    def _check_aliens_bottom(self):
        """检查是否有外星人到达底部"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_hit()  # 等同于撞到飞船
                break

    def _update_aliens(self):
        """更新所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # 检测飞船与外星人碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # 检测外星人抵达屏幕底端
        self._check_aliens_bottom()

    # 飞船
    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        # 扣除生命值
        self.stats.ships_left -= 1

        if self.stats.ships_left > 0:
            # 清空屏幕
            self.aliens.empty()
            self.bullets.empty()
            # 重置游戏元素
            self._create_alien_fleet()
            self.ship.center_ship()
            # 暂停游戏，给出反应事件
            time.sleep(0.5)
        else:
            self.stats.game_active = False
            # 当游戏结束时要重新显示鼠标方便用户点击开始按钮
            pygame.mouse.set_visible(True)  

    # 游戏屏幕
    def _update_screen(self):
        """绘制并显示新的屏幕内容"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blit_ship()           # 画一艘船
        for bullet in self.bullets.sprites(): # 画所有的子弹
            bullet.draw_bullet()
        self.aliens.draw(self.screen)   # 依次画所有的外星人

        # 显示游戏得分
        self.scoreBoard.show_score()

        # 当游戏未开始时，绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    # 运行游戏
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()    # 检查事件

            if self.stats.game_active:
                self.ship.update()      # 更新飞船
                self._update_bullets()  # 更新子弹
                self._update_aliens()   # 依次更新所有外星人
                
            self._update_screen()   # 刷新屏幕
            
if __name__ == "__main__":
    flag = False
    # flag = True
    game = AlienInvasion(flag)
    game.run_game()
