# coding: GBK 
# 在本程序中，编者很多变量并非完全是英文单词，而是汉语拼音的缩写（如背景色的设置：bj_color）。
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()                        # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  # 创建游戏窗口标题
    play_button = Button(ai_settings, screen, "Play")  # 创建play按钮
    stats = GameStats(ai_settings)
    # 创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)     # 创建一艘飞船
    bullets = Group()                    # 创建一个用于存储子弹的编组
    aliens = Group()                     # 创建一个用于存储外星人的编组
    gf.create_fleet(ai_settings, screen, ship, aliens)  # 创建外星人群
    
    while True:                          # 开始游戏主循环
        # 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        if stats.game_active:
            ship.update()                # 移动飞船位置
            # 发射并删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
        # 更新屏幕图像，并显示新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)
        
run_game()
