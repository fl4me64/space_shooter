class Settings():
	"""A class to store the settings for the game."""
	
	def __init__(self):
		"""Initialize the game's settings."""
		
		# Screen settings
		self.screen_width = 1920
		self.screen_height = 1080
		self.bg_color = (0, 0, 0)
		
		# Rocket settings
		self.rocket_speed_factor = 2
		self.rocket_health = 10
		
		# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = 0, 0, 255
		self.bullets_allowed = 3
		
		# Star settings
		self.star_speed_factor = 0.5
		
		# UFO settings
		self.ufo_speed_factor = 0.2
		
		# Scoring
		self.ufo_points = 10
		
		# Asteroid settings
		self.asteroid_speed_factor = 0.5
