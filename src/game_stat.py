class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, game):
        """初始化统计信息"""
        self.game_active = True
        self.settings = game.settings
        self.reset_stats()

    def reset_stats(self):
        """重置会变化的游戏统计信息"""
        self.ships_left = self.settings.ship_limit