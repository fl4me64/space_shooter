import pygame.font

class HealthStat():
	def __init__(self, screen, settings, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
		
		# Font settings for the rocket's health information.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
