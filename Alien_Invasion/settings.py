class Settings:
    #A class to store all settings for Allien Invasion.

    def __init__(self):
        #Initialize the game's statistics settings.
        #Screen settings.
        self.screen_width = 1000
        self.screen_height = 600
        

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 10

        #Ship settings
        self.ship_limit = 3

        #Alien settings
        self.fleet_drop_speed = 10

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 2.0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 8
        self.bullet_speed = 30
        self.alien_speed = 6

        #Fleet_direction of represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring settings
        self.alien_points = 100

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)