
import pygame
from pygame.sprite import Sprite

class Asteroid(Sprite):
	"""A class to represent an asteroid."""
	
	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		# Load the asteroid image and set its rect position.
		self.image = pygame.image.load('images/asteroid.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Position the asteroid.
		self.rect.centerx = self.screen_rect.right - 50
		self.rect.centery = self.screen_rect.centery
		
		# Store the asteroid's exact position.
		self.x = float(self.rect.x)
		
	def blitme(self):
		# Draw the asteroid at its current location.
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		# Move the asteroid to the left.
		self.x -= self.settings.asteroid_speed_factor
		self.rect.x = self.x
