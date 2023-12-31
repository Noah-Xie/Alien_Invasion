import pygame

class Settings:
    """存储游戏设置"""
    RIGHT = 1
    LEFT = -1

    def __init__(self):
        """初始化游戏设置"""
        self.high_score_path = './src/data/high_score.txt'
        self.bgm_path = './src/data/bgm.mp3'

        # 游戏的静态设置
        self.initialize_static_settings()

        # 游戏的动态设置
        self.initialize_dynamic_settings()

        self.play_background_music()

    def initialize_static_settings(self):
        """初始化游戏静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.screen_width = 600
        # self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 1
  
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # 外星人设置
        self.alien_drop_speed = 10

        # 游戏节奏速度
        self.speedup_scape = 1.1
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.fleet_direction = Settings.RIGHT

        # 外星人的分值
        self.alien_points = 50

    def increase_game_speed(self):
        """提高速度设置"""
        self.ship_speed   *= self.speedup_scape
        self.bullet_speed *= self.speedup_scape
        self.alien_speed  *= self.speedup_scape
        self.alien_points *= self.score_scale

    def play_background_music(self):
        """播放背景音乐"""
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(self.bgm_path)
            pygame.mixer.music.play(-1)  # -1 plays the music indefinitely
        except Exception as e:
            print("Can not play background music",e)
        
