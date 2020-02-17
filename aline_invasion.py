# coding: GBK 
# �ڱ������У����ߺܶ����������ȫ��Ӣ�ĵ��ʣ����Ǻ���ƴ������д���米��ɫ�����ã�bj_color����
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()                        # ��ʼ����Ϸ������һ����Ļ����
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")  # ������Ϸ���ڱ���
    play_button = Button(ai_settings, screen, "Play")  # ����play��ť
    stats = GameStats(ai_settings)
    # �����洢��Ϸͳ����Ϣ��ʵ�����������Ƿ���
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)     # ����һ�ҷɴ�
    bullets = Group()                    # ����һ�����ڴ洢�ӵ��ı���
    aliens = Group()                     # ����һ�����ڴ洢�����˵ı���
    gf.create_fleet(ai_settings, screen, ship, aliens)  # ����������Ⱥ
    
    while True:                          # ��ʼ��Ϸ��ѭ��
        # ��Ӧ����������¼�
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
            aliens, bullets)
        if stats.game_active:
            ship.update()                # �ƶ��ɴ�λ��
            # ���䲢ɾ������ʧ���ӵ�
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
                bullets)
        # ������Ļͼ�񣬲���ʾ����Ļ
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)
        
run_game()
