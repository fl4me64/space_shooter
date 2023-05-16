class GameStats():
	"""Track statistics for the game."""
	
	def __init__(self, settings):
		"""Initialize statistics."""
		self.settings = settings
		self.reset_stats()
		self.game_active = False
	
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.rocket_health_remaining = self.settings.rocket_health
		self.score = 0
		self.game_over = False
