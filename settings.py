# coding: GBK 
# 创建的设置类
class Settings():
    """存储《外星人入侵》的所有设置"""
    
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000         # 游戏窗口宽度
        self.screen_height = 600         # 游戏窗口高度
        self.bj_color = (230, 230, 230)  # 游戏窗口背景色
        # 飞船速度设置（初始基数为每次移动 1 像素）
        self.ship_limit = 3              # 飞船设置
        # 子弹设置
        self.bullet_width = 3            # 子弹rect的宽
        self.bullet_height = 15          # 子弹rect的高
        self.bullet_color = 60, 60, 60   # 子弹颜色
        self.bullets_allowed = 2         # 子弹数量
        # 外星人设置
        self.fleet_drop_speed = 10       # 外星人舰队下降速度
        
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外新人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction值为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1         # 外星人舰队移动方向
        self.alien_points = 50           # 记分

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
