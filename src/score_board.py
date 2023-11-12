import pygame.font as font

class ScoreBoard:
    """记分牌, 显示游戏得分的类"""

    def __init__(self, game):
        """初始化显示得分需要的属性"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.setttings = game.settings
        self.stats = game.stats

        # 显示得分时需要的字体设置
        self.text_color = (30, 30, 30)
        self.font = font.SysFont(None, 48)
        
        # 初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得分转换成渲染图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.setttings.bg_color
        )

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.score_rect.top + 20

    def show_score(self):
        """显示记分牌"""
        self.screen.blit(self.score_image, self.score_rect)
        