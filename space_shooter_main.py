import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from rocket import Rocket
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

def run_game():
	# Initialize the game and create a settings and screen object.
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Space Shooter")
	
	play_button = Button(screen, "Play!")
	
	# Create a rocket, a group of bullets, and a group of stars.
	rocket = Rocket(screen, settings)
	bullets = Group()
	stars = Group()
	ufos = Group()
	asteroids = Group()
	
	# Create a starry background and UFOs.
	gf.create_stars(screen, settings, stars)
	# gf.create_ufos(screen, settings, ufos)
	gf.create_fleet(screen, settings, ufos)
	gf.create_asteroid(screen, settings, asteroids)
	
	# Create an instance to store game statistics.
	stats = GameStats(settings)
	scoreboard = Scoreboard(screen, settings, stats)
	
	# Start the game's main loop.
	while True:
		# Check for keyboard events.
		gf.check_events(rocket, screen, settings, bullets, play_button, stats, scoreboard, ufos, asteroids)
		
		# Update the screen after all changes have been made to the rocket and bullets.
		gf.update_screen(screen, settings, bullets, stars, rocket, asteroids, ufos, scoreboard, stats, play_button)
		
		if stats.game_active:
			# Update the rocket's position.
			rocket.update_position()
		
			# Update bullet positions and remove old bullets.
			gf.update_bullets(bullets, screen, ufos, asteroids, stats, settings, scoreboard)
		
			# gf.update_stars(stars, screen, settings)
	
			gf.update_ufos(ufos, rocket, stats, scoreboard)
			
			gf.update_asteroid(asteroids, rocket, stats, scoreboard)

run_game()