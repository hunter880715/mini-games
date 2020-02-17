# coding: GBK 
# ������������
class Settings():
    """�洢�����������֡�����������"""
    
    def __init__(self):
        """��ʼ����Ϸ����"""
        # ��Ļ����
        self.screen_width = 1000         # ��Ϸ���ڿ��
        self.screen_height = 600         # ��Ϸ���ڸ߶�
        self.bj_color = (230, 230, 230)  # ��Ϸ���ڱ���ɫ
        # �ɴ��ٶ����ã���ʼ����Ϊÿ���ƶ� 1 ���أ�
        self.ship_limit = 3              # �ɴ�����
        # �ӵ�����
        self.bullet_width = 3            # �ӵ�rect�Ŀ�
        self.bullet_height = 15          # �ӵ�rect�ĸ�
        self.bullet_color = 60, 60, 60   # �ӵ���ɫ
        self.bullets_allowed = 2         # �ӵ�����
        # ����������
        self.fleet_drop_speed = 10       # �����˽����½��ٶ�
        
        # ��ʲô�����ٶȼӿ���Ϸ����
        self.speedup_scale = 1.1
        # �����˵���������ٶ�
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """��ʼ������Ϸ���ж��仯������"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_directionֵΪ1��ʾ�����ƶ���-1��ʾ�����ƶ�
        self.fleet_direction = 1         # �����˽����ƶ�����
        self.alien_points = 50           # �Ƿ�

    def increase_speed(self):
        """����ٶ�����"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
