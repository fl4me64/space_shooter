import pygame
from pygame.sprite import Sprite

class UFO(Sprite):
	"""A class to represent a single UFO."""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/ufo.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		# Start each new UFO near the top right of the screen.
		self.rect.right = self.screen_rect.right - 50
		self.rect.top = self.screen_rect.top + 50
		
		# Store the UFO's exact position.
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""Draw the UFO at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""Move the UFO left."""
		self.x -= self.settings.ufo_speed_factor
		self.rect.x = self.x