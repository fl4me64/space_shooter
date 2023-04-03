class GameStats():
	def __init__(self, settings):
		self.settings = settings
		
		self.game_active = False
	
	def reset_stats(self):
		self.health = 100
