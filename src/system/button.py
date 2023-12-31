import pygame.font as font
import pygame

class Button:
    """按钮类, 可以用来创建任何按钮"""

    def __init__(self, game, msg):
        """初始化按钮属性"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = font.SysFont(None, 48)

        # 创建按钮的rect对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像, 并在按钮上居中"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮, 绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)