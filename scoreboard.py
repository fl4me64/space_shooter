
import pygame.font

class Scoreboard():
	"""A class to report scoring information."""
	
	def __init__(self, screen, settings, stats):
		# Initialize socrekeeping attributes.
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
		
		# Font settings for scoring information.
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 40)
		
		self.prep_health()
		self.prep_score()
		self.prep_game_over()
	
	def prep_health(self):
		# Turn the health into a rendered image.
		health_str = "Health: " + str(self.stats.rocket_health_remaining)
		self.health_image = self.font.render(health_str, True, self.text_color, self.settings.bg_color)
		
		# Display the health at the top left of the screen.
		self.health_rect = self.health_image.get_rect()
		self.health_rect.left = self.screen_rect.left + 20
		self.health_rect.top = 20
	
	def show_health(self):
		# Draw the health to the screen.
		self.screen.blit(self.health_image, self.health_rect)
	
	def prep_score(self):
		# Turn the score into a rendered image.
		score_str = "Score: " + str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		
		# Display the score at the top left of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def show_score(self):
		# Draw the score to the screen.
		self.screen.blit(self.score_image, self.score_rect)
	
	def prep_game_over(self):
		game_over_str = "Game Over!"
		self.game_over_image = self.font.render(game_over_str, True, self.text_color, self.settings.bg_color)
		
		self.game_over_rect = self.game_over_image.get_rect()
		self.game_over_rect.centerx = self.screen_rect.centerx
		self.game_over_rect.top = self.screen_rect.centery - 100
	
	def show_game_over(self):
		self.screen.blit(self.game_over_image, self.game_over_rect)
