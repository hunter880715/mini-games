# coding: GBK 
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """��Ӧ����"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:    # ��Ӧ����������q���ر���Ϸ��
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """�����û�е������ƣ��ͷ���һ���ӵ�"""
    # ����һ���ӵ���������������bullets��
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def get_number_aliens_x(ai_settings, alien_width):
    """����ÿ�����ɶ���������"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """������Ļ�������ɶ�����������"""
    available_speca_y = (ai_settings.screen_height - 
                            (3 * alien_height) - ship_height)
    number_rows = int(available_speca_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """����һ�������˲�������ڵ�ǰ��"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
        
def create_fleet(ai_settings, screen, ship, aliens):
    """����������Ⱥ"""
    # ����һ�������ˣ�������һ�п����ɶ��ٸ�������
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, 
        alien.rect.height)
    # ������һ��������
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
        bullets):
    """��Ӧ����������¼�"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, 
                ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
        bullets, mouse_x, mouse_y):
    """����ҵ���Play��ťʱ��ʼ����Ϸ"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()  # ������Ϸ����
        pygame.mouse.set_visible(False)  # ���ع��

        stats.reset_stats()              # ������Ϸͳ����Ϣ
        stats.game_active = True

        sb.prep_score()                  # ���üǷ���ͼ��
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()                   # ����������б�
        bullets.empty()                  # ����ӵ��б�
        # ����һȺ�µ������ˣ����÷ɴ�����
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
        play_button):
    """������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
    screen.fill(ai_settings.bj_color)    # ÿ��ѭ����Ҫ���»�����Ļ
    for bullet in bullets.sprites():     # �ڷɴ��������˺����ػ������ӵ�
        bullet.draw_bullet()

    ship.blitme()                        # ���Ʒɴ�
    aliens.draw(screen)                  # ���Ʊ����е�ÿ��������
    sb.show_score()                      # ��ʾ�÷�

    if not stats.game_active:            # �����Ϸ���ڷǻ״̬���ͻ���play��ť
        play_button.draw_button()

    pygame.display.flip()                # ��������Ƶ���Ļ�ɼ�
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """�����ӵ�λ�ã���ɾ������ʧ���ӵ�"""
    bullets.update()               # �����ƶ��ӵ�
    for bullet in bullets.copy():  # ɾ������ʧ���ӵ�
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets)
            
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
        aliens, bullets):
    """��Ӧ�ӵ��������˵���ײ"""
    # ����Ƿ����ӵ�������������
    # ��������ˣ���ɾ����Ӧ���ӵ���������
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # ɾ�����е��ӵ�,�ӿ���Ϸ���࣬���½�һȺ������
        aliens.empty()
        bullets.empty()
        ai_settings.increase_speed()
        # ��ߵȼ�
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)
        
def check_fleet_edges(ai_settings, aliens):
    """�������˵����Եʱ��ȡ��Ӧ�Ĵ�ʩ"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    """����Ⱥ���������ƣ����ı����ǵķ���"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """��Ӧ��������ײ���ķɴ�"""
    if stats.ships_left > 0:
        stats.ships_left -= 1    # ��ship_left��1
        sb.prep_ships()          # ���¼Ƿ���
        aliens.empty()           # ��������˺��ӵ��б�
        bullets.empty()
        # ����һȺ�������ˣ������ɴ��ŵ���Ļ�׶�����
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)               # ��ͣһ���
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, 
        bullets):
    """����Ƿ��������˵�������Ļ�ײ�"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # ��ɴ���ײ��һ������
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
            
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    ����Ƿ���������λ����Ļ��Ե
    ������������Ⱥ�����������˵�λ��
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # ��������˺ͷɴ�֮�����ײ
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    # ����Ƿ��������˵ִ���Ļ�׶�
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """����Ƿ������µ���ߵ÷�"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()