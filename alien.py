# coding: GBK 
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r'images/alien.bmp')
        self.rect = self.image.get_rect()  # 设置外星人图像矩形属性
        self.rect.x = self.rect.width      # 每个最初出现的外星人都在屏幕左上角附近
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)        # 存储外星人准确位置
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x
