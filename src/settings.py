class Settings:
    """存储游戏设置"""
    RIGHT = 1
    LEFT = -1

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # self.screen_width = 600
        # self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5

        # 外星人设置
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        self.fleet_direction = Settings.RIGHT