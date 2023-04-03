import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from rocket import Rocket
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
	# Initialize the game and create a settings and screen object.
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Space Shooter")
	play_button = Button(screen, "Play!")
	stats = GameStats(settings)
	
	# Create a rocket, a group of bullets, and a starry background.
	rocket = Rocket(screen, settings)
	bullets = Group()
	stars = Group()
	ufos = Group()
	
	gf.create_stars(screen, settings, stars)
	gf.create_ufos(screen, settings, ufos)
	
	# Start the game's main loop.
	while True:
		# Check for keyboard events.
		gf.check_events(rocket, screen, settings, bullets, play_button, stats)
		
		if stats.game_active:
			# Update the rocket's position.
			rocket.update_position()
		
			# Update bullet positions and remove old bullets.
			gf.update_bullets(bullets, screen, ufos, settings)
		
			# gf.update_stars(stars, screen, settings)
		
			gf.update_ufos(ufos)
		
		# Update the screen after all changes have been made to the rocket and bullets.
		gf.update_screen(screen, settings, bullets, stars, rocket, ufos, stats, play_button)

run_game()
