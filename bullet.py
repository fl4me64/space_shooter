import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Manage bullets fired from the rocket"""
	
	def __init__(self, screen, settings, rocket):
		super().__init__()
		self.screen = screen
		
		# Create a bullet rect at (0, 0) and then set the correct position.
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centery = rocket.rect.centery
		self.rect.right = rocket.rect.right
		
		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)
		
		# Set the bullet's color and speed factor.
		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor
	
	def update(self):
		"""Move the bullet across the screen."""
		# Update the bullet's decimal position.
		self.x += self.speed_factor
		# Update the bullet's rect position.
		self.rect.x = self.x
	
	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
