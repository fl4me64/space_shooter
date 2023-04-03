import pygame

class Rocket():
	def __init__(self, screen, settings):
		# Initialize the rocket and set its starting position.
		self.screen = screen
		self.settings = settings
		
		# Load the rocket image and get its rect.
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Set the rocket at the middle left of the screen.
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		
		# Store a decimal value for the rocket's center.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def update_position(self):
		# Update the rocket's position based on the movement flag.
		if self.moving_right and self.rect.right <= self.screen_rect.right:
			self.centerx += self.settings.rocket_speed_factor
		if self.moving_left and self.rect.left >= 0:
			self.centerx -= self.settings.rocket_speed_factor
		if self.moving_up and self.rect.top >= 0:
			self.centery -= self.settings.rocket_speed_factor
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.centery += self.settings.rocket_speed_factor
		
		# Update rect object from self.centerx/y
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def blitme(self):
		# Draw the rocket at its current location.
		self.screen.blit(self.image, self.rect)
