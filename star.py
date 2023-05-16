import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to represent a single star."""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		
		# Load the star image and set its rect attribute.
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()
		
		# Start each new star at the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the star's exact position.
		self.x = float(self.rect.x)
	
	def check_disappeared(self):
		if self.rect.right < 0:
			return True
		else:
			return False
	
	def update(self):
		self.x -= self.settings.star_speed_factor
		self.rect.x = self.x